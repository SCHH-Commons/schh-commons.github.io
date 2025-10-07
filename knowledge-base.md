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

<script src="https://cdn.jsdelivr.net/npm/marked/lib/marked.umd.js"></script>
<script>
    fetch('https://www.schh-commons.org/knowledge-base/index.md')
    .then(resp => resp.text())
    .then(md => {
        let docsEl = document.getElementById('docs');
        docsEl.innerHTML = marked.parse(md);
        return docsEl;
    })
    .then(docsEl => {
        docsEl.querySelectorAll('a').forEach(a => { a.setAttribute('target', '_blank'); });
    });
</script>