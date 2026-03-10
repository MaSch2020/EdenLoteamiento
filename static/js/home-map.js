document.addEventListener("DOMContentLoaded", function () {
    const mapElement = document.getElementById("project-map");

    if (!mapElement || typeof L === "undefined") {
        return;
    }

    const lat = parseFloat(mapElement.dataset.lat || "-26.494759");
    const lng = parseFloat(mapElement.dataset.lng || "-55.273071");
    const zoom = parseInt(mapElement.dataset.zoom || "14", 10);
    const title = mapElement.dataset.title || "Proyecto";
    const lotSelect = document.getElementById("id_lot");
    const lotsJsonElement = document.getElementById("lots-map-data");

    let lotsData = [];

    if (lotsJsonElement) {
        try {
            lotsData = JSON.parse(lotsJsonElement.textContent || "[]");
        } catch (error) {
            console.error("No se pudo parsear el GeoJSON de los lotes:", error);
            lotsData = [];
        }
    }

    const map = L.map(mapElement, {
        zoomControl: true,
        scrollWheelZoom: true,
    }).setView([lat, lng], zoom);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 20,
        attribution: '&copy; OpenStreetMap contributors',
    }).addTo(map);

    const projectMarker = L.marker([lat, lng]).addTo(map);
    projectMarker.bindPopup(`<strong>${title}</strong><br>Centro base del proyecto`);

    const statusStyles = {
        available: {
            color: "#1d7f4e",
            fillColor: "#1d7f4e",
            fillOpacity: 0.24,
            weight: 2,
        },
        reserved: {
            color: "#b87a12",
            fillColor: "#b87a12",
            fillOpacity: 0.24,
            weight: 2,
        },
        sold: {
            color: "#b13a3a",
            fillColor: "#b13a3a",
            fillOpacity: 0.24,
            weight: 2,
        },
        default: {
            color: "#123c2f",
            fillColor: "#123c2f",
            fillOpacity: 0.18,
            weight: 2,
        },
        highlight: {
            weight: 3,
            fillOpacity: 0.32,
        },
    };

    function money(value) {
        if (value === null || value === undefined || value === "") {
            return "A consultar";
        }

        const numeric = Number(String(value).replace(/,/g, ""));
        if (Number.isFinite(numeric)) {
            return `Gs. ${numeric.toLocaleString("es-PY")}`;
        }

        return `Gs. ${value}`;
    }

    function installmentText(featureProperties) {
        if (
            !featureProperties.installment_value ||
            !featureProperties.installment_count ||
            Number(featureProperties.installment_count) <= 0
        ) {
            return "A consultar";
        }

        return `${featureProperties.installment_count} x ${money(featureProperties.installment_value)}`;
    }

    function getBaseStyle(status) {
        return statusStyles[status] || statusStyles.default;
    }

    function selectLotInForm(lotId, code) {
        if (!lotSelect || !lotId) {
            return;
        }

        const value = String(lotId);
        const option = Array.from(lotSelect.options).find((item) => item.value === value);

        if (!option) {
            return;
        }

        lotSelect.value = value;
        lotSelect.dispatchEvent(new Event("change", { bubbles: true }));
        lotSelect.focus();

        const contactSection = document.getElementById("contacto");
        if (contactSection) {
            contactSection.scrollIntoView({ behavior: "smooth", block: "start" });
        }

        const messageField = document.getElementById("id_message");
        if (messageField && !messageField.value.trim()) {
            messageField.value = `Hola, me interesa el lote ${code}. Quisiera más información.`;
        }
    }

    function popupContent(properties) {
        return `
            <div class="map-popup">
                <strong>${properties.code || "Lote"}</strong><br>
                Estado: ${properties.status_label || "-"}<br>
                Superficie: ${properties.area_m2 || "-"} m²<br>
                Contado: ${money(properties.price_cash)}<br>
                Cuotas: ${installmentText(properties)}<br>
                <button type="button" class="map-popup-button" data-lot-id="${properties.lot_id || ""}" data-lot-code="${properties.code || ""}">
                    Elegir este lote
                </button>
            </div>
        `;
    }

    function normalizeLotFeature(feature) {
        if (!feature || typeof feature !== "object") {
            return null;
        }

        if (feature.type === "Feature") {
            return feature;
        }

        if (feature.type && feature.coordinates) {
            return {
                type: "Feature",
                geometry: feature,
                properties: {},
            };
        }

        return null;
    }

    const lotsGroup = L.featureGroup().addTo(map);

    lotsData.forEach((lotFeature) => {
        const feature = normalizeLotFeature(lotFeature);
        if (!feature || !feature.geometry) {
            return;
        }

        const properties = feature.properties || {};
        const baseStyle = getBaseStyle(properties.status);

        const layer = L.geoJSON(feature, {
            style: function () {
                return baseStyle;
            },
            pointToLayer: function (_feature, latlng) {
                return L.circleMarker(latlng, {
                    radius: 8,
                    color: baseStyle.color,
                    fillColor: baseStyle.fillColor,
                    fillOpacity: 0.9,
                    weight: 2,
                });
            },
            onEachFeature: function (_innerFeature, innerLayer) {
                innerLayer.bindPopup(popupContent(properties));

                if (typeof innerLayer.setStyle === "function") {
                    innerLayer.on("mouseover", function () {
                        innerLayer.setStyle({
                            ...baseStyle,
                            ...statusStyles.highlight,
                        });
                    });

                    innerLayer.on("mouseout", function () {
                        innerLayer.setStyle(baseStyle);
                    });
                }

                innerLayer.on("click", function () {
                    selectLotInForm(properties.lot_id, properties.code);
                });
            },
        });

        layer.addTo(lotsGroup);
    });

    if (lotsGroup.getLayers().length > 0) {
        map.fitBounds(lotsGroup.getBounds(), {
            padding: [24, 24],
            maxZoom: 18,
        });
    } else {
        projectMarker.openPopup();
    }

    map.whenReady(function () {
        setTimeout(function () {
            map.invalidateSize();
        }, 150);
    });

    window.addEventListener("resize", function () {
        setTimeout(function () {
            map.invalidateSize();
        }, 120);
    });

    map.on("popupopen", function (event) {
        const popupElement = event.popup && event.popup.getElement();
        if (!popupElement) {
            return;
        }

        const button = popupElement.querySelector(".map-popup-button");
        if (!button) {
            return;
        }

        button.addEventListener("click", function () {
            selectLotInForm(button.dataset.lotId, button.dataset.lotCode);
        });
    });
});