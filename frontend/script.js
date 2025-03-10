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


    const displayResults = (data) => {
        console.log(data);
        if (data.length === 0) {
            resultsDiv.innerHTML = "<p>No results found.</p>";
            return;
        }
        resultsDiv.innerHTML = data.map(car => `
        <div class="card mb-3">
            <div class="card-body">
                <h5 class="card-title">${car.full_name}</h5>
                <p class="card-text">Price: $${car.price}</p>
                <p class="card-text">Fuel: ${car.fuel}</p>
                <p class="card-text">Transmission: ${car.transmission}</p>
                <p class="card-text">Power: ${car.power_hp} HP</p>
            </div>
        </div>
    `).join('');
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
