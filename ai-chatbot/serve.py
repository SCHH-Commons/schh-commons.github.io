#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example Agentic Chat Server using SCHH content and tools
'''

import json, os, secrets
from typing import Optional

### Define LLM ###

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langgraph.prebuilt import create_react_agent

from pinecone import Pinecone

embeddings = OpenAIEmbeddings()
pc = Pinecone()

from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()


### Define tools ###

from langchain_core.tools import tool
from datetime import datetime
from langchain_community.tools import TavilySearchResults

@tool
def current_date():
  """Use this to get the current date."""
  return datetime.today().strftime('%Y-%m-%d')
  
@tool
def schh_weather() -> str:
  """Get the weather forecast for the Sun City Hilton Head region."""
  return TavilySearchResults(
    max_results=3,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True).invoke({"query": "What is the weather forecast for the Sun City Hilton Head region?"})

from langchain_community.tools.tavily_search import TavilySearchResults
search = TavilySearchResults(max_results=2)

tools = [current_date, schh_weather]


### Define Agent ###

_model_name = None
_knowledge_base = None
agent_executor = None
def create_agent(model, knowledge_base):
  global agent_executor, _model_name, _knowledge_base
  if model == _model_name and knowledge_base == _knowledge_base:
    return
  _model_name = model
  _knowledge_base = knowledge_base
  print(f'Creating agent with model={model} knowledge_base={knowledge_base}')
  if 'gpt-4o' in model:
    llm = ChatOpenAI(model=model)
  else:
    print(f'Using Anthropic model: {model} api_key={os.environ.get("ANTHROPIC_API_KEY")}')
    llm = ChatAnthropic(model_name=model)
  pinecone_index = pc.Index(knowledge_base)
  vector_store = PineconeVectorStore( pinecone_index, embeddings, 'text' )  

  @tool(response_format="content_and_artifact")
  def upcoming_events():
    """Use this to get event information."""
    print('Tool: upcoming_events')
    query = f'get events'
    retrieved_docs = vector_store.similarity_search(query, k=5)
    
    print(f'\n{query} retrieved={len(retrieved_docs)}\n')
    for doc in retrieved_docs:
      print(json.dumps(doc.metadata))
      # print(doc.page_content + '\n)
  
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs
  
  @tool(response_format="content_and_artifact")
  def retrieve(query: str):
    """Retrieve information related to a query."""
    print('Tool: retrieve')
    retrieved_docs = vector_store.similarity_search(query, k=5)

    print(f'\n{query} retrieved={len(retrieved_docs)}\n')
    for doc in retrieved_docs:
      print(json.dumps(doc.metadata))
      # print(doc.page_content + '\n)
  
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

  agent_executor = create_react_agent(llm, tools + [retrieve], checkpointer=memory)

 
 ### Helpers ###

from langchain_core.messages import HumanMessage

def get_response(messages, config):
  return agent_executor.invoke({'messages': messages}, config)['messages'][-1].content

## Response generator for streaming
async def stream_response(messages, config):
  async for msg, metadata in agent_executor.astream({'messages': messages}, config, stream_mode='messages'):
    if (
        msg.content
        and not isinstance(msg, HumanMessage)
        and metadata['langgraph_node'] == 'agent' 
    ):
        yield msg.content
 
 
 ### Setup FastAPI server and define endpoints ###
 
from fastapi import FastAPI, Request
from fastapi.responses import Response, StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class CacheControlStaticFiles(StaticFiles):
  def file_response(self, *args, **kwargs) -> Response:
    response = super().file_response(*args, **kwargs)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
app.mount("/static", CacheControlStaticFiles(directory="static"), name="static")
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

@app.get('/')
async def root():
  return FileResponse('index.html')

@app.get('/chat/{prompt}')
@app.post('/chat/')
@app.post('/chat')
async def chat(
  request: Request, 
  prompt: Optional[str] = None, 
  sessionid: Optional[str] = secrets.token_hex(4),
  model: Optional[str] = 'gpt-4o-mini',
  index: Optional[str] = 'schh',
  stream: Optional[bool] = False): 
  if request.method == 'POST':
    body = await request.body()
    payload = json.loads(body)
    print(json.dumps(payload, indent=2))
    prompt = payload.get('prompt', '')
    stream = payload.get('stream', False)
    sessionid = payload.get('sessionid', secrets.token_hex(4))
  
  print(f'chat prompt={prompt} sessionid={sessionid} model={model} index={index} stream={stream}')
  
  create_agent(model, index)

  config = {'configurable': {'thread_id': sessionid}}
  messages = [{'role': 'user', 'content': prompt}]
  
  if stream:
    return StreamingResponse(stream_response(messages, config), media_type='text/event-stream')
  else:
    return Response(content=get_response(messages, config), media_type='text/plain')  

if __name__ == '__main__':
  import uvicorn

  uvicorn.run(app, host='0.0.0.0', port=8080)