document.addEventListener("DOMContentLoaded", function () {
    const mapElement = document.getElementById("project-map");

    if (!mapElement || typeof L === "undefined") {
        return;
    }

    const lat = parseFloat(mapElement.dataset.lat || "-26.494759");
    const lng = parseFloat(mapElement.dataset.lng || "-55.273071");
    const zoom = parseInt(mapElement.dataset.zoom || "14", 10);
    const title = mapElement.dataset.title || "Proyecto";

    const map = L.map(mapElement).setView([lat, lng], zoom);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors',
    }).addTo(map);

    const marker = L.marker([lat, lng]).addTo(map);
    marker.bindPopup(`<strong>${title}</strong><br>${lat}, ${lng}`).openPopup();
});