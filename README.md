"# Sweet Shop Management System" 
# Sweet Shop Management System

A simple command-line application to manage a sweet shop's inventory, including adding, deleting, viewing, purchasing, restocking, and sorting sweets.

## Features

- Add new sweets with ID, name, category, price, and quantity
- Delete sweets by ID
- View all sweets in the shop
- Purchase sweets and update stock
- Restock sweets and update stock
- Search and sort sweets by various attributes (ID, name, category, price, quantity)
- Input validation and error handling

## Requirements

- Python 3.7 or higher

## Usage

1. **Clone or download this repository.**
2. Open a terminal and navigate to the `Sweet Shop Management System` directory.
3. Run the CLI application:

   ```sh
   python sweetshop_cli.py
   ```

4. Follow the on-screen menu to manage the sweet shop.

## Project Structure

```
Sweet Shop Management System/
│
├── sweetshop_cli.py              # Main CLI application
├── operations_function.py        # Business logic for sweet operations
├── sweet.py                      # Sweet class definition
├── test_operation_add_function.py
├── test_operation_delete_function.py
├── test_operation_view_function.py
├── test_purchase_function.py
├── test_restock_function.py
├── test_search_sort_function.py
└── README.md
```

## Running Tests

To run all tests, execute:

```sh
python -m unittest discover -s . -p "test_*.py"
```
