let map;
let dataLayer;

const initMap = async () => {
    const mapElement = document.getElementById('map');
    await customElements.whenDefined('gmp-map');
    map = mapElement.innerMap;
    dataLayer = map.data;
}

const loadGeoJSON = async (geoJsonUrl) => {
    const response = await fetch(geoJsonUrl);
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const geoJsonData = await response.json();
    const features = dataLayer.addGeoJson(geoJsonData);
    return features;
}

const fitBounds = () => {
    const bounds = new google.maps.LatLngBounds();
    dataLayer.forEach(function (feature) {
        const geometry = feature.getGeometry();
        geometry.forEachLatLng(function (latLng) {
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

(async () => {
    try {
        await initMap();
        await loadGeoJSON('https://raw.githubusercontent.com/rsnyder/media/main/geojson/Sun_City,_Hilton_Head.geojson');
        applyStyle({
            fillColor: '#FF0000',
            fillOpacity: 0.3,
            strokeColor: '#FF0000',
            strokeWeight: 1
        });
    } catch (error) {
        console.error('Error initializing map:', error);
    }
})();