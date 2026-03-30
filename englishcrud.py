import csv
import os

DATA_FILE = os.path.join("data", "data.csv")


def read_products():
    if not os.path.isfile(DATA_FILE):
        return []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def create_product(product_data):
    products = read_products()

    for product in products:
        if product["id"] == str(product_data["id"]):
            print("Error: A product with this ID already exists.")
            return False

    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=product_data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(product_data)

    return True


def update_product(id_value, id_field, new_data):
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
    products = read_products()

    for product in products:
        if product[id_field] == str(id_value):
            return product

    return None


def find_product_by_name(name):
    products = read_products()
    return [p for p in products if p["name"].lower() == name.lower()]


def delete_product_by_name(name):
    products = read_products()
    new_products = [p for p in products if p["name"].lower() != name.lower()]

    if len(new_products) != len(products):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(new_products)
        return True

    return False


def alert_low_stock():
    products = read_products()
    low_stock = [p for p in products if int(p["stock"]) < 5]

    if not low_stock:
        print("✅ No products with low stock.")
        return

    print("\n⚠️ LOW STOCK PRODUCTS:")
    for p in low_stock:
        if int(p["stock"]) <= 2:
            print(f"🔴 CRITICAL: ID: {p['id']} | {p['name']} | Stock: {p['stock']}")
        else:
            print(f"🟡 LOW: ID: {p['id']} | {p['name']} | Stock: {p['stock']}")
