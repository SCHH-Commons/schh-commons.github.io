---
# the default layout is 'page'
title: AI Assistant
description: Learn about the SCHH AI Assistant — a resident-created tool that helps you find and understand Sun City Hilton Head information more easily.
icon: fas fa-atom
layout: page
order: 1
permalink: /chatbot
published: true
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.18.0/cdn/themes/light.css" />

<style>
  .row {
    justify-content: center;
  }
  main h4 {
    margin: 0;
    font-size: clamp(0.5em, 2vw, 1em);
    font-weight: 400;
  }
  table {
      width: 100%;
      border-collapse: collapse;
      margin: 1em 0;
      font-size: 0.95rem;
      font-family: sans-serif;
  }

  th, td {
      padding: 0.6em 0.8em;
      text-align: left;
      border: 1px solid #ddd;
  }

  th {
      background-color: #f4f4f4;
      font-weight: 600;
  }

  tr:nth-child(even) {
      background-color: #fafafa;
  }

  tr:hover {
      background-color: #f1f7ff;
    }

  th:nth-child(3),
  td:nth-child(3) {
    display: none;
  }
  td {
    line-height: 1.4;
  }

    .button {
      margin-top: 1em;
      position: relative;
      border-radius: 1000px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      min-width: 6rem;
      text-decoration: none;
      transition: color 0.2s, background-color 0.2s, border-color 0.2s;
      border: 0.125rem solid rgb(255, 209, 64);
      font-family: PayPalOpen-Bold, "Helvetica Neue", Arial, sans-serif;
      font-size: 1.125rem;
      line-height: 1.5rem;
      font-weight: 400;
      padding: 0.625rem 1.875rem;
      background: rgb(255, 209, 64);
      color: rgb(0, 48, 135);
    }
    .content a.button:hover {
      color: unset !important;
      border-bottom: #ddd;
    }

    @media (max-width: calc(849px)) {
    h1.dynamic-title~.content {
        margin-top: .5em;
    }

    main h2 {
    margin: 1.5rem 0 1.25rem;
    }

    .button {
      margin-top: 0;
    }
}

</style>

![SCHH AI Assistant](/assets/img/Chatbot.png){: .w-50 .right}

Welcome to the **SCHH AI Assistant** — a friendly, experimental tool created to help Sun City Hilton Head residents (and future neighbors) quickly find the information that matters most. Instead of digging through websites, newsletters, or emails, you can simply **ask questions in plain language** and get helpful answers drawn from reliable community sources. It’s like having a knowledgeable neighbor who’s always ready to help you learn more about life in Sun City.

---

<p style="text-align: center; clear: both;">
<a href="/chatbase" class="button">
  <img src="{{ '/assets/img/chatbase.jpg' | relative_url }}" class="no-lightbox" alt="Start AI Chatbot" style="height: 24px; width: 24px; margin-right: 8px;">Open the SCHH AI Assistant
</a>
</p>

---

The SCHH AI Assistant helps residents and prospective residents easily find and understand information about life in Sun City Hilton Head. It draws on a growing collection of community resources—official documents, SunSations articles, SCTV broadcasts, and more—to provide clear, conversational answers to your questions.

The Assistant is **powered by Chatbase**, a platform that uses **ChatGPT**, one of the most advanced AI language models available. Chatbase connects the Assistant to the SCHH Commons Knowledge Base, allowing it to understand questions, retrieve relevant information from curated Sun City materials, and respond in a friendly, natural way.

> **Note:** *The SCHH AI Assistant is a resident-initiated, community-driven project and is not affiliated with the developer or any official Sun City Hilton Head organization. The tools and resources hosted on the [SCHH Commons](https://www.schh-commons.org) website are provided to help residents more easily find, understand, and use community information.*
{: .prompt-info }

---

# The Knowledge Base
{: #knowledge-base}

The **Knowledge Base** is the foundation of the SCHH AI Assistant. It brings together a growing collection of documents, guides, and resources that help residents better understand life in Sun City Hilton Head.

Sources include:  
- The official **Sun City Hilton Head website** (public and resident-only pages)  
- **SunSations** magazine  
- The **Clubs and Groups Catalog**  
- Documents from the **Association Community Library**  
- **SCTV** broadcasts  
- **Community email announcements** and other communications  
- **AI-assisted Deep Dives** — in-depth explorations that combine AI research tools with curated source material to provide a deeper understanding of key community topics  
- **Resident-contributed content** and insights  


> **Important Note:** *The SCHH Knowledge Base isn’t meant to replace official Sun City websites, association documents, or other authoritative sources. Those remain the final word for community rules, policies, and updates. Instead, the Knowledge Base and AI Assistant serves as a helpful companion to those sources—an added layer that makes it easier to locate, connect, and understand information that matters to residents.*
{: .prompt-warning }

---

## Feedback and Contributions

The SCHH AI Assistant is currently in a pilot phase and continues to evolve as new materials are added. Contact me to identify any errors discovered, to suggest new content to be added, or to contribute a document.

<p style="text-align: center;">
<a href="/contact" class="button">
  <i class="far fa-envelope fa-fw me-1"></i>Contact me
</a>
</p>

## Knowledge Base Documents

The tables below list the documents currently included in the Knowledge Base, each with a link to its source.  (*Viewing resident-only pages or Library materials will require logging into the official Sun City website*)

<section id="docs"></docs>


<script src="https://cdn.jsdelivr.net/npm/marked/lib/marked.umd.js"></script>
<script type="module">
  import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";
  import 'https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace/cdn/components/dialog/dialog.js';
  import 'https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace/cdn/components/button/button.js';

  const isMobile = ('ontouchstart' in document.documentElement && /mobi/i.test(navigator.userAgent) );

  let dialog = document.createElement('sl-dialog');
  dialog.setAttribute('style', `--width: ${isMobile ? '100' : '80'}dvw;`);
  let markdownEl = document.createElement('div');
  dialog.appendChild(markdownEl);
  document.body.appendChild(dialog);

  fetch('https://www.schh-commons.org/knowledge-base/index.md')
  .then(resp => resp.text())
  .then(md => {
      let docsEl = document.getElementById('docs');
      docsEl.innerHTML = marked.parse(md);
      return docsEl;
  })
  .then(docsEl => {
      docsEl.querySelectorAll('a').forEach(a => {
        if (a.href.indexOf('https://www.schh-commons.org/knowledge-base') === 0) {
          a.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            fetch(`${a.href}.md`).then(resp => resp.text()).then(md => {
              markdownEl.innerHTML = marked.parse(md);
              dialog.show();
            });
          });
        } else {
          a.setAttribute('target', '_blank');
        }
      });
  });
</script>