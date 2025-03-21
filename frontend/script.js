document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const toggleFiltersButton = document.getElementById('toggleFiltersButton');
    const filtersSection = document.getElementById('filtersSection');
    const priceRange = document.getElementById('priceRange');
    const priceValue = document.getElementById('priceValue');
    const fuelType = document.getElementById('fuelType');
    const transmission = document.getElementById('transmission');
    const powerRange = document.getElementById('powerRange');
    const powerValue = document.getElementById('powerValue');
    const resultsDiv = document.getElementById('results');


    let searchTimeout;
    let filtersVisible = false;


    const toggleFilters = () => {
        filtersVisible = !filtersVisible;
        filtersSection.classList.toggle('hidden', !filtersVisible);
        toggleFiltersButton.textContent = filtersVisible ? 'Hide Filters' : 'Show Filters';
    };


    toggleFiltersButton.addEventListener('click', toggleFilters);


    priceRange.addEventListener('input', () => {
        priceValue.textContent = `0 - ${priceRange.value}`;
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(searchAutomobiles, 300);
    });


    powerRange.addEventListener('input', () => {
        powerValue.textContent = `0 - ${powerRange.value}`;
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(searchAutomobiles, 300);
    });


    const fetchAutomobiles = async (filters = {}) => {
        const queryParams = new URLSearchParams(filters).toString();
        const response = await fetch(`http://localhost:5000/api/automobiles/search?${queryParams}`);
        const data = await response.json();
        return data;
    };


    const formatColorName = (color) => {
        return color.replace(/_/g, ' ');
    };


    const displayResults = (data) => {
        console.log(data);
        if (data.length === 0) {
            resultsDiv.innerHTML = "<p>No results found.</p>";
            return;
        }
        resultsDiv.innerHTML = data.map(car => `
        <div class="card mb-3">
            <div class="card-body d-flex flex-column justify-content-between align-items-center">
                <h5 class="card-title text-justify text-center">${car.full_name}</h5>
                
                <div class="d-flex justify-content-start align-items-center align-content-start flex-row mw-100 card-content">                
                    <div>
                        <p class="card-text">Fuel: ${car.fuel}</p>
                        <p class="card-text">Transmission: ${car.transmission}</p>
                        <p class="card-text">Power: ${car.power_hp} HP</p>
                        <p class="card-text">Base Price: €${car.price.toFixed(2)}</p>
                        <p class="card-text mt-2"><strong>Total Price: €<span id="totalPrice-${car.full_name}">${car.price.toFixed(2)}</span></strong></p>
                    </div>
                    
                    <div class="car-image-div d-flex flex-column justify-content-between align-items-center">
                    ${car.colors ? `
                        <label for="colorSelect-${car.full_name}">Select Color:</label>
                        <select class="form-select color-select" id="colorSelect-${car.full_name}">
                            ${Object.keys(car.colors).map(color => `
                                <option value="${color}" data-cost="${car.colors[color].cost}">
                                    ${formatColorName(color)} (€${car.colors[color].cost})
                                </option>
                            `).join('')}
                        </select>
                        <img src="${Object.values(car.colors)[0].image}" alt="${car.full_name}" class="car-image" id="carImage-${car.full_name}">
                    ` : ''}
                    </div>
                </div>
            </div>
        </div>
    `).join('');

        document.querySelectorAll('.color-select').forEach(select => {
            const carName = select.id.replace('colorSelect-', '');

            const savedColor = localStorage.getItem(`color_${carName}`);
            if (savedColor) {
                select.value = savedColor;

                const colorCost = parseFloat(select.selectedOptions[0].getAttribute('data-cost'));
                const basePrice = parseFloat(data.find(car => car.full_name === carName).price);
                const totalPrice = basePrice + colorCost;

                document.getElementById(`carImage-${carName}`).src = data.find(car => car.full_name === carName).colors[savedColor].image;
                document.getElementById(`totalPrice-${carName}`).textContent = totalPrice.toFixed(2);
            }

            select.addEventListener('change', (event) => {
                const selectedColor = event.target.value;
                const colorCost = parseFloat(event.target.selectedOptions[0].getAttribute('data-cost'));
                const basePrice = parseFloat(data.find(car => car.full_name === carName).price);

                const imageUrl = data.find(car => car.full_name === carName).colors[selectedColor].image;
                document.getElementById(`carImage-${carName}`).src = imageUrl;

                const totalPrice = basePrice + colorCost;
                document.getElementById(`totalPrice-${carName}`).textContent = totalPrice.toFixed(2);

                localStorage.setItem(`color_${carName}`, selectedColor);
            });
        });
    };


    const searchAutomobiles = async () => {
        const filters = {
            query: searchInput.value.trim(),
            min_price: 0,
            max_price: priceRange.value,
            fuel: fuelType.value,
            transmission: transmission.value,
            max_power: powerRange.value
        };

        const data = await fetchAutomobiles(filters);
        displayResults(data);
    };


    searchButton.addEventListener('click', searchAutomobiles);
    priceRange.addEventListener('change', searchAutomobiles);
    fuelType.addEventListener('change', searchAutomobiles);
    transmission.addEventListener('change', searchAutomobiles);
    powerRange.addEventListener('change', searchAutomobiles);

    searchAutomobiles();
});
