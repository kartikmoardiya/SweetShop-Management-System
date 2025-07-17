// Sweet class - JavaScript equivalent of the Python Sweet class
class Sweet {
    constructor(id, name, category, price, quantity) {
        this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
        this.quantity = quantity;
    }
}

// SweetOperator class - JavaScript equivalent of the Python SweetOperator class
class SweetOperator {
    constructor() {
        this.sweets = [];
        this.loadFromStorage();
    }

    // Save to localStorage
    saveToStorage() {
        localStorage.setItem('sweetShopData', JSON.stringify(this.sweets));
    }

    // Load from localStorage
    loadFromStorage() {
        const data = localStorage.getItem('sweetShopData');
        if (data) {
            const sweetData = JSON.parse(data);
            this.sweets = sweetData.map(s => new Sweet(s.id, s.name, s.category, s.price, s.quantity));
        }
    }

    // Check if ID exists
    idExists(id) {
        return this.sweets.some(sweet => sweet.id === id);
    }

    // Check if category is valid
    categoryExists(category) {
        const validCategories = ["chocolate", "candy", "pastry"];
        return validCategories.includes(category.trim().toLowerCase());
    }

    // Add sweet
    addSweet(id = null, name = "", category = "", price = 0, quantity = -1) {
        if (id === null || this.idExists(id) || id < 0) {
            return "Invalid ID";
        }

        if (name.length <= 0) {
            return "Invalid Name";
        }

        if (!this.categoryExists(category) || category.length <= 0) {
            return "Invalid Category";
        }

        if (price <= 0) {
            return "Invalid Price";
        }

        if (quantity < 0) {
            return "Invalid Quantity";
        }

        const sweet = new Sweet(id, name, category.toLowerCase(), price, quantity);
        this.sweets.push(sweet);
        this.saveToStorage();

        return "Sweet Added Successfully";
    }

    // Get all sweets
    getSweets() {
        return this.sweets;
    }

    // Delete sweet by ID
    deleteSweets(id = -1) {
        if (!this.idExists(id)) {
            return "Invalid ID";
        }
        this.sweets = this.sweets.filter(sweet => sweet.id !== id);
        this.saveToStorage();
        return "Sweet Deleted Successfully";
    }

    // View sweets (returns a copy)
    viewSweets() {
        return [...this.sweets];
    }

    // Search/Sort sweets
    sweetSearch(sort = "name") {
        sort = sort.trim().toLowerCase();
        if (!["id", "name", "category", "price", "quantity"].includes(sort)) {
            return "Invalid Sort Parameter";
        }
        return [...this.sweets].sort((a, b) => {
            if (typeof a[sort] === 'string') {
                return a[sort].localeCompare(b[sort]);
            }
            return a[sort] - b[sort];
        });
    }

    // Purchase sweet
    sweetPurchase(name, quantityToPurchase = 1) {
        if (!this.sweets || this.sweets.length === 0) {
            return "No Sweets Available";
        }

        if (quantityToPurchase <= 0) {
            return "Invalid Purchase Quantity";
        }

        const sweetFound = this.sweets.find(sweet => 
            sweet.name.toLowerCase() === name.toLowerCase()
        );

        if (!sweetFound) {
            return "Sweet Not Found";
        }

        if (sweetFound.quantity < quantityToPurchase) {
            return "Insufficient Stock";
        }

        sweetFound.quantity -= quantityToPurchase;
        this.saveToStorage();

        return `Purchase Successful. ${quantityToPurchase} ${name}(s) purchased. Remaining stock: ${sweetFound.quantity}`;
    }

    // Restock sweet
    restockSweets(name, quantityToRestock) {
        if (!this.sweets || this.sweets.length === 0) {
            return "No Sweets Available";
        }

        if (quantityToRestock <= 0) {
            return "Invalid Restock Quantity";
        }

        const sweetFound = this.sweets.find(sweet => 
            sweet.name.toLowerCase() === name.toLowerCase()
        );

        if (!sweetFound) {
            return "Sweet Not Found";
        }

        sweetFound.quantity += quantityToRestock;
        this.saveToStorage();

        return `Restock Successful. ${quantityToRestock} ${name}(s) restocked. Current stock: ${sweetFound.quantity}`;
    }
}

// Global variables
let sweetShop = new SweetOperator();

// DOM Elements
const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');
const sweetsTableBody = document.getElementById('sweetsTableBody');
const noSweetsMessage = document.getElementById('noSweetsMessage');
const messageContainer = document.getElementById('messageContainer');

// Forms
const addSweetForm = document.getElementById('addSweetForm');
const purchaseForm = document.getElementById('purchaseForm');
const restockForm = document.getElementById('restockForm');
const sortBtn = document.getElementById('sortBtn');
const sortSelect = document.getElementById('sortSelect');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeTabs();
    initializeForms();
    displaySweets();
});

// Tab functionality
function initializeTabs() {
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabName = button.getAttribute('data-tab');
            switchTab(tabName);
        });
    });
}

function switchTab(tabName) {
    // Remove active class from all tabs and contents
    tabButtons.forEach(btn => btn.classList.remove('active'));
    tabContents.forEach(content => content.classList.remove('active'));

    // Add active class to selected tab and content
    document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
    document.getElementById(`${tabName}-tab`).classList.add('active');

    // Refresh sweets display when switching to view tab
    if (tabName === 'view') {
        displaySweets();
    }
}

// Form initialization
function initializeForms() {
    addSweetForm.addEventListener('submit', handleAddSweet);
    purchaseForm.addEventListener('submit', handlePurchase);
    restockForm.addEventListener('submit', handleRestock);
    sortBtn.addEventListener('click', handleSort);
}

// Handle add sweet form submission
function handleAddSweet(e) {
    e.preventDefault();
    
    const id = parseInt(document.getElementById('sweetId').value);
    const name = document.getElementById('sweetName').value.trim();
    const category = document.getElementById('sweetCategory').value;
    const price = parseFloat(document.getElementById('sweetPrice').value);
    const quantity = parseInt(document.getElementById('sweetQuantity').value);

    const result = sweetShop.addSweet(id, name, category, price, quantity);
    
    if (result === "Sweet Added Successfully") {
        showMessage(result, 'success');
        addSweetForm.reset();
        displaySweets();
    } else {
        showMessage(result, 'error');
    }
}

// Handle purchase form submission
function handlePurchase(e) {
    e.preventDefault();
    
    const name = document.getElementById('purchaseName').value.trim();
    const quantity = parseInt(document.getElementById('purchaseQuantity').value);

    const result = sweetShop.sweetPurchase(name, quantity);
    
    if (result.includes("Purchase Successful")) {
        showMessage(result, 'success');
        purchaseForm.reset();
        displaySweets();
    } else {
        showMessage(result, 'error');
    }
}

// Handle restock form submission
function handleRestock(e) {
    e.preventDefault();
    
    const name = document.getElementById('restockName').value.trim();
    const quantity = parseInt(document.getElementById('restockQuantity').value);

    const result = sweetShop.restockSweets(name, quantity);
    
    if (result.includes("Restock Successful")) {
        showMessage(result, 'success');
        restockForm.reset();
        displaySweets();
    } else {
        showMessage(result, 'error');
    }
}

// Handle sort functionality
function handleSort() {
    const sortBy = sortSelect.value;
    const result = sweetShop.sweetSearch(sortBy);
    
    if (typeof result === 'string') {
        showMessage(result, 'error');
    } else {
        displaySweets(result);
        showMessage(`Sweets sorted by ${sortBy}`, 'info');
    }
}

// Display sweets in table
function displaySweets(sweetsToDisplay = null) {
    const sweets = sweetsToDisplay || sweetShop.viewSweets();
    
    if (sweets.length === 0) {
        sweetsTableBody.innerHTML = '';
        noSweetsMessage.style.display = 'block';
        document.querySelector('.sweets-table').style.display = 'none';
        return;
    }

    noSweetsMessage.style.display = 'none';
    document.querySelector('.sweets-table').style.display = 'table';

    sweetsTableBody.innerHTML = sweets.map(sweet => `
        <tr>
            <td>${sweet.id}</td>
            <td>${sweet.name}</td>
            <td>
                <span class="category-badge category-${sweet.category}">
                    ${sweet.category}
                </span>
            </td>
            <td>₹${sweet.price.toFixed(2)}</td>
            <td>${sweet.quantity}</td>
            <td>
                <button class="btn btn-danger" onclick="deleteSweet(${sweet.id})">
                    <i class="fas fa-trash"></i> Delete
                </button>
            </td>
        </tr>
    `).join('');
}

// Delete sweet function
function deleteSweet(id) {
    if (confirm('Are you sure you want to delete this sweet?')) {
        const result = sweetShop.deleteSweets(id);
        
        if (result === "Sweet Deleted Successfully") {
            showMessage(result, 'success');
            displaySweets();
        } else {
            showMessage(result, 'error');
        }
    }
}

// Show message function
function showMessage(message, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${type}`;
    messageDiv.textContent = message;
    
    messageContainer.appendChild(messageDiv);
    
    // Auto remove message after 5 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.parentNode.removeChild(messageDiv);
        }
    }, 5000);
    
    // Allow manual removal by clicking
    messageDiv.addEventListener('click', () => {
        if (messageDiv.parentNode) {
            messageDiv.parentNode.removeChild(messageDiv);
        }
    });
}

// Add some sample data for demonstration
function addSampleData() {
    sweetShop.addSweet(1, "Chocolate Truffle", "chocolate", 25.99, 50);
    sweetShop.addSweet(2, "Gummy Bears", "candy", 12.50, 100);
    sweetShop.addSweet(3, "Chocolate Croissant", "pastry", 18.75, 30);
    sweetShop.addSweet(4, "Lollipop", "candy", 5.99, 200);
    sweetShop.addSweet(5, "Dark Chocolate Bar", "chocolate", 15.99, 75);
    displaySweets();
    showMessage("Sample data added!", 'info');
}

// Add sample data button (you can call this function from console or add a button)
// Uncomment the next line to automatically add sample data on page load
// addSampleData();