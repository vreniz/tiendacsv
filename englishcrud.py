import csv
import os

# Path where the CSV file will be stored
DATA_FILE = os.path.join("data", "data.csv")


def read_products():
    """
    Reads all product records from the CSV file.

    Returns:
        list: A list of dictionaries (products).
              Returns an empty list if the file does not exist.
    """
    if not os.path.isfile(DATA_FILE):
        return []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def create_product(product_data):
    """
    Adds a new product to the CSV file.

    Validates that the product ID is unique.

    Args:
        product_data (dict): Product information.

    Returns:
        bool: True if created successfully, False if duplicate ID exists.
    """
    products = read_products()

    # Prevent duplicate IDs
    for product in products:
        if product["id"] == str(product_data["id"]):
            print("Error: A product with this ID already exists.")
            return False

    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=product_data.keys())

        # Write header only if file is new
        if not file_exists:
            writer.writeheader()

        writer.writerow(product_data)

    return True


def update_product(id_value, id_field, new_data):
    """
    Updates an existing product by ID.

    Args:
        id_value (int): ID of the product to update
        id_field (str): Field used as identifier ("id")
        new_data (dict): Updated product data

    Returns:
        bool: True if updated, False if not found
    """
    products = read_products()
    updated = False

    for product in products:
        if product[id_field] == str(id_value):
            product.update(new_data)
            updated = True

    if updated:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(products)

    return updated


def delete_product(id_value, id_field):
    """
    Deletes a product by ID.

    Returns:
        bool: True if deleted, False if not found
    """
    products = read_products()

    new_products = [p for p in products if p[id_field] != str(id_value)]

    if len(new_products) != len(products):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(new_products)
        return True

    return False


def find_product_by_id(id_value, id_field="id"):
    """
    Searches for a product by ID.

    Returns:
        dict | None
    """
    products = read_products()

    for product in products:
        if product[id_field] == str(id_value):
            return product

    return None


def find_product_by_name(name):
    """
    Searches products by exact name (case insensitive).

    Returns:
        list
    """
    products = read_products()
    results = []

    for product in products:
        if product["nombre"].lower() == name.lower():
            results.append(product)

    return results


def delete_product_by_name(name):
    """
    Deletes products by name.

    Returns:
        bool
    """
    products = read_products()

    new_products = [p for p in products if p["nombre"].lower() != name.lower()]

    if len(new_products) != len(products):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(new_products)
        return True

    return False


def alert_low_stock():
    """
    Displays products with low stock.

    - Warning: stock < 5
    - Critical: stock <= 2
    """
    products = read_products()

    low_stock = [p for p in products if int(p["cantidad"]) < 5]

    if not low_stock:
        print("✅ No products with low stock.")
        return

    print("\n⚠️ LOW STOCK PRODUCTS:")
    for p in low_stock:
        if int(p["cantidad"]) <= 2:
            print(
                f"🔴 CRITICAL: ID: {p['id']} | {p['nombre']} | Stock: {p['cantidad']}"
            )
        else:
            print(f"🟡 LOW: ID: {p['id']} | {p['nombre']} | Stock: {p['cantidad']}")
