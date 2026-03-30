from englishcrud import *
import re


def show_menu():
    print("\n--- STORE INVENTORY MANAGEMENT ---")
    print("1. Create product")
    print("2. Read products")
    print("3. Update product")
    print("4. Delete product")
    print("5. Search product")
    print("6. Exit")
    print("7. Show low stock products")


def read_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Must be a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Must be an integer.")


def read_float(message):
    pattern = r"^\d+([.,]\d+)?$"

    while True:
        value = input(message).strip()

        if not value:
            print("Value cannot be empty.")
            continue

        if not re.match(pattern, value):
            print("Invalid format (e.g., 10, 10.5, 10,5).")
            continue

        value = float(value.replace(",", "."))

        if value <= 0:
            print("Must be greater than 0.")
        else:
            return value


def read_text(message):
    while True:
        text = input(message).strip()

        if not text:
            print("Field cannot be empty.")
            continue

        if text.isdigit():
            print("Cannot contain only numbers.")
            continue

        for c in text:
            if not (c.isalpha() or c.isdigit() or c.isspace()):
                print("Invalid format. Only letters, numbers, and spaces.")
                break
        else:
            return text


def get_product_data():
    return {
        "id": read_positive_int("ID: "),
        "nombre": read_text("Name: "),
        "Precio": read_float("Price: "),
        "categoria": read_text("Category: "),
        "cantidad": read_positive_int("Stock: "),
    }


def get_update_data():
    return {
        "nombre": read_text("Name: "),
        "Precio": read_float("Price: "),
        "categoria": read_text("Category: "),
        "cantidad": read_positive_int("Stock: "),
    }


if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            data = get_product_data()
            if create_product(data):
                print("Product saved.")

        elif option == "2":
            products = read_products()
            print(products if products else "No products found.")

        elif option == "3":
            product_id = int(input("Enter ID to update: "))
            print(
                "Updated."
                if update_product(product_id, "id", get_update_data())
                else "Not found."
            )

        elif option == "4":
            mode = input("(1) Delete by ID or (2) by name: ")

            if mode == "1":
                product_id = int(input("ID: "))
                print("Deleted." if delete_product(product_id, "id") else "Not found.")
            else:
                name = input("Name: ")
                print("Deleted." if delete_product_by_name(name) else "Not found.")

        elif option == "5":
            mode = input("(1) ID or (2) Name: ")

            if mode == "1":
                print(find_product_by_id(int(input("ID: "))) or "Not found.")
            else:
                print(find_product_by_name(input("Name: ")) or "No results.")

        elif option == "6":
            break

        elif option == "7":
            alert_low_stock()
