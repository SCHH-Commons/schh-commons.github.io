---
title: AI Assistant
layout: page
published: true
permalink: /chatbase
---

<style>

    * {
        box-sizing: border-box;
    }

    :root {
        --safe-top: env(safe-area-inset-top);
        --safe-right: env(safe-area-inset-right);
        --safe-bottom: env(safe-area-inset-bottom);
        --safe-left: env(safe-area-inset-left);
    }

    body {
        height: 100vh;
        padding: env(safe-area-inset-top) env(safe-area-inset-right) 0 env(safe-area-inset-left);
    }
    #main-wrapper,
    #main-wrapper .container,
    #main-wrapper .container main,
    #main-wrapper .container main article,
    #main-wrapper .container main article .content {
        min-height: 0;
        margin-top: 0;
        height: 100%;
    }
    .dynamic-title {
      display: none;
    }
    iframe {
        margin-left: -1em;
        width: calc(100% + 2em);
        height: 99%;
    }
    #tail-wrapper {
        display: none;
    }
    #tail-wrapper footer {
        margin-top: 0;
        padding: 0;
        height: 4rem;
    }
    /* non-PWA mobile styles */
    @media (display-mode: browser) and (max-width: 767px) {
        body {
            height: 100svh;
        }

        /* iOS-only hint if you need it */
        @supports (-webkit-touch-callout: none) {
            /* iOS-specific fixes here if desired */
        }
    }

</style>

<iframe src="https://www.chatbase.co/chatbot-iframe/TsC-X_BP0qiFBYG_ZKRZk"></iframe>
