---
title: AI Assistant
layout: page
published: true
permalink: /chatbase
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@latest/cdn/themes/light.css" />

<script type="module">
  import { setBasePath } from 'https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@latest/cdn/utilities/base-path.js';
  setBasePath('https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@latest/cdn/');
</script>

<script src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@latest/cdn/components/button/button.js" type="module"></script>
<script src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@latest/cdn/components/dialog/dialog.js" type="module"></script>

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
    #main-wrapper .container main article .content {
        display: flex;
        flex-direction: column;
    }
    iframe {
        margin-left: -1em;
        width: calc(100% + 2em);
        height: 100%;
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
    #feedback {
        margin-top: -6px;
        margin-bottom: 6px;
        text-align: center;
    }
    .contact-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 0 1rem 1rem 1rem;
}

sl-dialog {
    display: none;
}
sl-dialog::part(body) {
    padding: 0;
}

.contact-form label {
    font-weight: 600;
    margin-bottom: 0.25rem;
}

.contact-form input,
.contact-form textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: inherit;
    font-size: 1rem;
}

.contact-form button {
    padding: 0.75rem 1.5rem;
    background: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
}

.contact-form button:hover {
    background: #0052a3;
}


</style>

<iframe src="https://www.chatbase.co/chatbot-iframe/TsC-X_BP0qiFBYG_ZKRZk"></iframe>

<div id="feedback">
    <a href="#">Report an error or missing content.</a>
</div>

<sl-dialog id="dialog" label="AI Assistant Feedback">
    <form class="contact-form" action="https://formsubmit.co/admin@schh-commons.org" method="POST">

        <label for="message">Describe the error or missing content </label>
        <textarea id="message" name="message" rows="6" required></textarea>

        <!-- hidden options -->
        <input type="hidden" name="email" value="feedback@schh-commons.org">
        <input type="hidden" name="_subject" value="Website contact form">
        <input type="text" name="_honey" style="display:none">
        <input type="hidden" name="_captcha" value="false">

        <button type="submit">Send</button>
    </form>
</sl-dialog>

<script type="module">
    // const isMobile = ('ontouchstart' in document.documentElement && /mobi/i.test(navigator.userAgent) );
    const dialog = document.getElementById('dialog');
    dialog.style.display = 'block';
    // if (isMobile) dialog.setAttribute('style', '--width: 100dvw;');
    document.getElementById('feedback').addEventListener('click', (e) => { dialog.show(); });
</script>
