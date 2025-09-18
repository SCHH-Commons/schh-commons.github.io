---
title: "Community Facilities Map"
description: "Interactive map showing all community facilities and amenities."
date: 2024-01-20
# image: /assets/img/facilities-map.jpg
map_embed: "<iframe src='...' width='100%' height='400'></iframe>"
---

Explore all the amazing facilities SCHH has to offer...

<script async src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAx7YrWFehCJR6T_ko2EhO_kpwfUzviVIs&callback=console.debug&libraries=maps,marker&v=beta"></script>

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
    
    /* Always set the map height explicitly to define the size of the div
    * element that contains the map. */
    gmp-map {
        height: 100%;
    }

    /* Optional: Makes the sample page fill the window. */
    html,
    body {
        height: 100%;
        margin: 0;
        padding: 0;
    }
</style>

<gmp-map center="32.301314300250375,-80.96083639954215" zoom="14" map-id="DEMO_MAP_ID">
    <gmp-advanced-marker position="40.12150192260742,-100.45039367675781" title="My location"></gmp-advanced-marker>
</gmp-map>
