---
title: "Community Facilities Map"
description: "Interactive map showing all community facilities and amenities."
date: 2024-01-20
layout: map-post
---

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
    #main-wrapper .container div:first-of-type,
    #main-wrapper .container div:first-of-type main,
    #main-wrapper .container div:first-of-type main article,
    #main-wrapper .container div:first-of-type main article .content {
        min-height: 0;
        margin-top: 0;
        height: 100%;
    }
    #topbar-title,
    #main-wrapper .container div:nth-of-type(2) {
        display: none;
    }
    #main-wrapper .container div:first-of-type main article header h1 {
        margin-top: 0;
    }
    #main-wrapper .container div:first-of-type main article header p.post-desc {
        line-height: 1.4;
        margin-bottom: 1em !important;
    }
    article {
        display: flex;
        flex-direction: column;
    }
    article.px-1 {
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    .content {
        padding: 0;
    }
    #tail-wrapper nav.post-navigation {
        display: none !important;
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

</style>

<gmp-map center="32.3044810,-80.9572716" zoom="12.5" map-id="map" id="map">
    <gmp-advanced-marker position="40.12150192260742,-100.45039367675781" title="My location"></gmp-advanced-marker>
</gmp-map>

<script type="module">
    let map;
    let dataLayer;

    const initMap = async () => {
        const mapElement = document.getElementById('map');
        await customElements.whenDefined('gmp-map');
        map = mapElement.innerMap; // Get the map instance
        dataLayer = map.data;  // Initialize the data layer
    }

    const loadGeoJSON = async (geoJsonUrl) => {
        const response = await fetch(geoJsonUrl);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const geoJsonData = await response.json();
        const features = dataLayer.addGeoJson(geoJsonData);
        return features
    }
    
    const fitBounds = () => {
        // Fit the map bounds to the loaded data
        const bounds = new google.maps.LatLngBounds();
        dataLayer.forEach(function(feature) {
            const geometry = feature.getGeometry();
            geometry.forEachLatLng(function(latLng) {
                bounds.extend(latLng);
            });
        });
        map.fitBounds(bounds);
    }

    const applyStyle = (style) => {            
        dataLayer.setStyle((feature) => {
            return {
                fillColor: style.fillColor,
                fillOpacity: style.fillOpacity,
                strokeColor: style.strokeColor,
                strokeWeight: style.strokeWeight,
                clickable: true
            };
        });
    }

    await initMap()
    await loadGeoJSON('https://raw.githubusercontent.com/rsnyder/media/main/geojson/Sun_City,_Hilton_Head.geojson')
    // fitBounds()
    applyStyle({
        fillColor: '#FF0000',
        fillOpacity: 0.3,
        strokeColor: '#FF0000',
        strokeWeight: 1
    })

</script>