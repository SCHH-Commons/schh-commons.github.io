// ==UserScript==
// @name         SCHH Assistant Link
// @namespace    https://www.schh-commons.org
// @version      1.1
// @description  Adds a floating “Ask SCHH Assistant” button on suncityhiltonhead.org pages
// @author       SCHH Commons
// @match        https://suncityhiltonhead.org/*
// @icon         https://www.schh-commons.org/favicon.ico
// @run-at       document-end
// @grant        none
// ==/UserScript==

(function () {
    /** Injects the button if not already present */
    function addAssistantButton() {
        if (document.getElementById('schh-assistant-button')) return;

        const btn = document.createElement('button');
        btn.id = 'schh-assistant-button';
        btn.textContent = 'Ask SCHH Assistant';

        Object.assign(btn.style, {
            position: 'fixed',
            right: '16px',
            bottom: '16px',
            zIndex: 999999,
            padding: '10px 16px',
            font: '15px system-ui, sans-serif',
            borderRadius: '8px',
            border: 'none',
            background: '#0a66c2',
            color: '#fff',
            cursor: 'pointer',
            boxShadow: '0 2px 8px rgba(0,0,0,.25)',
        });

        btn.addEventListener('click', () => {
            const sel = window.getSelection ? String(getSelection()) : '';
            const u = encodeURIComponent(location.href);
            const q = encodeURIComponent(sel || document.title);
            window.open(
                `https://www.schh-commons.org/chatbot?source=${u}&q=${q}`,
                '_blank',
                'noopener'
            );
        });

        document.body.appendChild(btn);
    }

    // Initial injection
    addAssistantButton();

    // Re-inject if the page dynamically changes (single-page app)
    new MutationObserver(addAssistantButton).observe(document.body, {
        childList: true,
        subtree: true,
    });
})();