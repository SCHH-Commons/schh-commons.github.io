---
# the default layout is 'page'
title: Events Calendar
icon: fas fa-calendar-alt
layout: page
permalink: /events
order: 2
published: true
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
        border: 1px solid green;
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
    iframe {
        margin-left: -1em;
        width: calc(100% + 2em);
        height: 100%;
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

<iframe src="https://calendar.google.com/calendar/embed?src=pmn8t3cndno6s002tvukskmvq0mkfehm@import.calendar.google.com&ctz=America%2FNew_York&mode=agenda" style="border: 0" frameborder="0" scrolling="no"></iframe>