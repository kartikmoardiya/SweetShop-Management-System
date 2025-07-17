# Sweet Shop Management System

A web-based inventory management system for sweet shops built with HTML, CSS, and JavaScript.

![Sweet Shop Management System](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.17_d5532e62.jpg-MQuNcTZu0RMYghQ3cMEJxGmQVQ7mHe.jpeg)

## Features

- ✅ Add new sweets to inventory
- ✅ View all sweets in a table
- ✅ Delete sweets from inventory
- ✅ Purchase sweets (reduces stock)
- ✅ Restock sweets (adds stock)
- ✅ Sort by ID, name, category, or price
- ✅ Responsive design for mobile/desktop
- ✅ Data saved in browser storage

## Quick Start

1. Download the project files
2. Open `index.html` in your web browser
3. Start managing your sweet inventory!

## File Structure

```
sweet-shop-frontend/
├── index.html    # Main HTML file
├── styles.css    # CSS styling
└── script.js     # JavaScript functionality
```

## Usage

### Adding Sweets
![Add Sweet](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.26_b585ad18.jpg-C4dWYoVsX6zZcKspviw7OmkmESfdTv.jpeg)
- Click "Add Sweet" tab
- Fill in ID, name, category, price, and quantity
- Categories: chocolate, candy, pastry

### Viewing Inventory
![View Sweets](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.17_d5532e62.jpg-MQuNcTZu0RMYghQ3cMEJxGmQVQ7mHe.jpeg)
- Click "View Sweets" tab
- Use dropdown to sort by different fields
- Click "Delete" to remove items

### Making Purchases
![Purchase](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.33_3b5c4ae4.jpg-Stbo2zl5PDPVKlL9RWl5HtdIGE3kkC.jpeg)
- Click "Purchase" tab
- Enter sweet name and quantity
- Stock automatically updates

### Restocking
![Restock](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.40_5e6f9d2a.jpg-gAQr1G3cxJAM0LkEy9z3lCmJJ0IscL.jpeg)
- Click "Restock" tab
- Enter sweet name and quantity to add
- Inventory increases automatically

## Validation Rules

- **ID**: Must be unique and positive
- **Name**: Cannot be empty
- **Category**: Must be chocolate, candy, or pastry
- **Price**: Must be greater than 0
- **Quantity**: Must be 0 or greater

## Browser Support

Works on all modern browsers:
- Chrome, Firefox, Safari, Edge

## Data Storage

- Uses browser localStorage
- Data persists between sessions
- No server required

---

**Ready to manage your sweet shop inventory!** 🍭

## 🏗️ Project Structure

```
sweet-shop-management/
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── styles.css          # CSS styling
│   └── script.js           # JavaScript functionality
├── backend/
│   ├── sweet.py            # Sweet data model
│   ├── operations_function.py  # Core business logic
│   └── sweetshop_cli.py    # Command-line interface
├── tests/
│   ├── test_operation_add_function.py
│   ├── test_operation_delete_function.py
│   ├── test_operation_view_function.py
│   ├── test_purchase_function.py
│   ├── test_restock_function.py
│   └── test_search_sort_function.py
├── README.md
└── REPORT.md
```

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.7+ (for backend/CLI)

### Frontend Setup
1. Clone the repository
2. Open `frontend/index.html` in your web browser
3. Start managing your sweet inventory!

### Backend Setup
1. Navigate to the backend directory
2. Run the CLI application:
   ```bash
   python sweetshop_cli.py
   ```

### Running Tests
```bash
python -m unittest test_operation_add_function.py
python -m unittest test_operation_delete_function.py
python -m unittest test_operation_view_function.py
python -m unittest test_purchase_function.py
python -m unittest test_restock_function.py
python -m unittest test_search_sort_function.py
```

## 💻 Usage

### Adding a Sweet
![Add Sweet Form](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.26_b585ad18.jpg-C4dWYoVsX6zZcKspviw7OmkmESfdTv.jpeg)

1. Click on the "Add Sweet" tab
2. Fill in the required fields:
   - **Sweet ID**: Unique positive integer
   - **Sweet Name**: Name of the sweet
   - **Category**: Choose from chocolate, candy, or pastry
   - **Price**: Must be greater than 0
   - **Quantity**: Must be 0 or greater
3. Click "Add Sweet" to save

### Viewing Inventory
![View Sweets Table](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.17_d5532e62.jpg-MQuNcTZu0RMYghQ3cMEJxGmQVQ7mHe.jpeg)

- Navigate to "View Sweets" tab
- Use the sort dropdown to organize by ID, name, category, or price
- Click "Delete" to remove items (with confirmation)

### Making a Purchase
![Purchase Form](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.33_3b5c4ae4.jpg-Stbo2zl5PDPVKlL9RWl5HtdIGE3kkC.jpeg)



1. Go to "Purchase" tab
2. Enter the exact sweet name
3. Specify quantity to purchase
4. System validates stock availability

### Restocking Inventory
![Restock Form](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/WhatsApp%20Image%202025-07-17%20at%2023.13.40_5e6f9d2a.jpg-gAQr1G3cxJAM0LkEy9z3lCmJJ0IscL.jpeg)

1. Select "Restock" tab
2. Enter sweet name and quantity to add
3. System updates inventory automatically

## 🎨 Design Features

- **Modern UI**: Clean, professional interface with gradient backgrounds
- **Color-coded Categories**: 
  - 🟢 Chocolate: Green badges
  - 🔴 Candy: Red badges  
  - 🟡 Pastry: Yellow badges
- **Responsive Layout**: Adapts to all screen sizes
- **Interactive Elements**: Hover effects and smooth transitions
- **Toast Notifications**: Success/error messages with auto-dismiss

## 🔧 Technical Implementation

### Frontend Architecture
- **Vanilla JavaScript**: No external dependencies
- **CSS Grid/Flexbox**: Modern layout techniques
- **LocalStorage API**: Client-side data persistence
- **Event-driven**: Responsive user interactions

### Backend Architecture
- **Object-Oriented Design**: Clean class structure
- **Comprehensive Validation**: Input sanitization and error handling
- **Test-Driven Development**: 100% test coverage
- **CLI Interface**: Command-line management option

## 📊 Validation Rules

### Sweet Addition
- ID must be unique and positive
- Name cannot be empty
- Category must be: chocolate, candy, or pastry
- Price must be greater than 0
- Quantity must be 0 or greater

### Purchase/Restock
- Sweet name must exist (case-insensitive)
- Quantity must be positive
- Purchase quantity cannot exceed available stock

## 🧪 Testing

The project includes comprehensive unit tests covering:
- ✅ Add functionality with edge cases
- ✅ Delete operations and error handling
- ✅ View and display operations
- ✅ Purchase validation and stock management
- ✅ Restock functionality
- ✅ Search and sort operations

## 🌟 Future Enhancements

- [ ] Database integration (MySQL/PostgreSQL)
- [ ] User authentication and roles
- [ ] Sales reporting and analytics
- [ ] Barcode scanning support
- [ ] Multi-location inventory
- [ ] Export functionality (CSV/PDF)
- [ ] Dark mode theme

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ for efficient sweet shop management.

---

**Happy Sweet Managing! 🍬**
```