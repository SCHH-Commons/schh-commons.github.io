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
    #tail-wrapper footer {
        margin-top: 0;
        padding: 0;
        height: 4rem;
    }
    iframe {
        height: calc(100dvh - 240px); 
        width: 100%;
        box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
    }
    @media (max-width: calc(849px)) {
        #main-wrapper > .container {
            min-height: unset;
        }
        h1.dynamic-title~.content {
            margin-top: 0;
        }
        iframe {
            height: calc(100dvh - 122px); 
            margin-left: -16px; 
            width: 100dvw;
            box-shadow: none;
        }
    }
</style>

<iframe src="https://calendar.google.com/calendar/embed?src=cbhph5hgjv492pn9usop0uuacg533kpf@import.calendar.google.com&ctz=America%2FNew_York&mode=agenda" style="border: 0" frameborder="0" scrolling="no"></iframe>