import 'https://maps.googleapis.com/maps/api/js?key=AIzaSyAx7YrWFehCJR6T_ko2EhO_kpwfUzviVIs&callback=console.debug&libraries=maps,marker&v=beta'

const initMap = async (id) => {
    const mapElement = document.getElementById(id || 'map');
    await customElements.whenDefined('gmp-map');
    return mapElement.innerMap;
}

const loadGeoJSON = async (map, geoJsonUrl) => {
    const response = await fetch(geoJsonUrl);
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const geoJsonData = await response.json();
    const features = map.data.addGeoJson(geoJsonData);
    return features;
}

const fitBounds = (map) => {
    const bounds = new google.maps.LatLngBounds();
    map.data.forEach(function (feature) {
        const geometry = feature.getGeometry();
        geometry.forEachLatLng(function (latLng) {
            bounds.extend(latLng);
        });
    });
    map.fitBounds(bounds);
}

const applyStyle = (map, style) => {
    map.data.setStyle((feature) => {
        return {
            fillColor: style.fillColor,
            fillOpacity: style.fillOpacity,
            strokeColor: style.strokeColor,
            strokeWeight: style.strokeWeight,
            clickable: true
        };
    });
}

export { initMap, loadGeoJSON, fitBounds, applyStyle };