---
title: Knowledge Base
layout: page
published: true
permalink: /kb
---

<style>
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
</style>

The SCHH Commons Knowledge Base is constructed from official community documents and resident-contributed information.

# Documents
{: #docs}

<script type="module">
    import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";
    const md2Html = (md) => marked.parse(md); // convert markdown to HTML
    console.log('js');

    (async () => {
        console.log('in async');
        let resp = await fetch('https://www.schh-commons.org/knowledge-base/index.md');
        let md = await resp.text();
        const html = md2Html(md);
        console.log(html);
        document.getElementById('docs').innerHTML = md2Html(md);
    })
</script>