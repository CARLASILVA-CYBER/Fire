const canvas = document.getElementById("fireCanvas");
const ctx = canvas.getContext("2d");

const gridSize = 20;
const cellSize = canvas.width / gridSize;

let fireMap = [];
let wind = 1;
let humidity = 0.3;
let flammability = 0.6;

// Initialize fire map
function initializeMap() {
    fireMap = [];
    for (let i = 0; i < gridSize; i++) {
        let row = [];
        for (let j = 0; j < gridSize; j++) {
            row.push(Math.random() < 0.05 ? 1 : 0); // 5% chance of fire
        }
        fireMap.push(row);
    }
}

// Draw the grid on the canvas
function drawMap() {
    for (let i = 0; i < gridSize; i++) {
        for (let j = 0; j < gridSize; j++) {
            if (fireMap[i][j] === 1) {
                ctx.fillStyle = "red"; // Fire
            } else {
                ctx.fillStyle = "green"; // No fire
            }
            ctx.fillRect(j * cellSize, i * cellSize, cellSize, cellSize);
        }
    }
}

// Simulate fire spreading
function simulateFire() {
    let newMap = JSON.parse(JSON.stringify(fireMap)); // Deep copy of fireMap
    for (let i = 0; i < gridSize; i++) {
        for (let j = 0; j < gridSize; j++) {
            if (fireMap[i][j] === 1) { // Fire in this cell
                // Spread fire to neighbors
                spreadFire(newMap, i - 1, j); // Up
                spreadFire(newMap, i + 1, j); // Down
                spreadFire(newMap, i, j - 1); // Left
                spreadFire(newMap, i, j + 1); // Right
            }
        }
    }
    fireMap = newMap;
    drawMap();
}

// Function to spread fire based on conditions
function spreadFire(map, i, j) {
    if (i >= 0 && i < gridSize && j >= 0 && j < gridSize && map[i][j] === 0) {
        let spreadChance = flammability * (1 - humidity);
        // Adjust by wind
        if (wind === 1 && j > 0) spreadChance *= 1.5; // Wind to right
        if (wind === -1 && j < gridSize - 1) spreadChance *= 0.5; // Wind to left
        if (Math.random() < spreadChance) {
            map[i][j] = 1; // Spread fire to this cell
        }
    }
}

// Start the simulation
function startSimulation() {
    wind = parseFloat(document.getElementById("wind").value);
    humidity = parseFloat(document.getElementById("humidity").value);
    flammability = parseFloat(document.getElementById("flammability").value);

    initializeMap();
    drawMap();

    // Simulate fire propagation over time
    let interval = setInterval(() => {
        simulateFire();
    }, 500); // Update every 500ms
}
