# Store Inventory Management System (CSV)

This project is a command-line application that allows store employees to manage product inventory using CRUD operations (Create, Read, Update, Delete). Data is stored persistently in a CSV file.

---

## Features

- Add new products (unique ID validation)
- View all products
- Update product information
- Delete products (by ID or name)
- Search products (by ID or name)
- Low stock alert system:
  - Warning if stock < 5
  - Critical if stock <= 2

---

## Project Structure

- `main.py` → User interface and input handling
- `crud.py` → Business logic and CSV operations
- `data/data.csv` → Data storage file

---

## Requirements

- Python 3.x

---

## How to Run

```bash
python main.py
```
## Data Structure

Each product contains:

- id (int)
- nombre (string)
- Precio (float)
- categoria (string)
- cantidad (int)

---

## Key Concepts

### CSV Storage
Data is stored in rows and columns using `csv.DictWriter` and `csv.DictReader`.

### CRUD Operations
- Create → Add new product
- Read → Load all products
- Update → Modify existing data
- Delete → Remove product

### Input Validation
- Ensures correct data types
- Prevents empty values
- Validates formats using regex

---

## Notes
- CSV stores values as strings internally
- The file is automatically created if it does not exist
- IDs must be unique

---

## Possible Improvements
- Partial search by name
- GUI interface
- Database integration
- Export to JSON
- Logging system

---

## Author
Developed as a practical project for learning file handling, validation, and CRUD systems in Python.