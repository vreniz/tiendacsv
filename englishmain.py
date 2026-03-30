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

        valid = True
        for c in text:
            if not (c.isalpha() or c.isdigit() or c.isspace()):
                valid = False
                break

        if not valid:
            print("Invalid format. Only letters, numbers, and spaces.")
            continue

        return text


def get_product_data():
    return {
        "id": read_positive_int("ID: "),
        "name": read_text("Name: "),
        "price": read_float("Price: "),
        "category": read_text("Category: "),
        "stock": read_positive_int("Stock: "),
    }


def get_update_data():
    return {
        "name": read_text("Name: "),
        "price": read_float("Price: "),
        "category": read_text("Category: "),
        "stock": read_positive_int("Stock: "),
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
            if products:
                for p in products:
                    print(p)
            else:
                print("No products found.")

        elif option == "3":
            try:
                product_id = int(input("Enter ID to update: "))
                if product_id <= 0:
                    print("ID must be positive.")
                    continue
                updated = update_product(product_id, "id", get_update_data())
                print("Updated." if updated else "Not found.")
            except ValueError:
                print("Invalid ID.")

        elif option == "4":
            mode = input("(1) Delete by ID or (2) by name: ")

            if mode == "1":
                try:
                    product_id = int(input("ID: "))
                    if product_id <= 0:
                        print("ID must be positive.")
                        continue
                    print("Deleted." if delete_product(product_id, "id") else "Not found.")
                except ValueError:
                    print("Invalid ID.")

            elif mode == "2":
                name = input("Name: ").strip()
                print("Deleted." if delete_product_by_name(name) else "Not found.")

        elif option == "5":
            mode = input("(1) ID or (2) Name: ")

            if mode == "1":
                try:
                    print(find_product_by_id(int(input("ID: "))) or "Not found.")
                except ValueError:
                    print("Invalid ID.")
            else:
                print(find_product_by_name(input("Name: ")) or "No results.")

        elif option == "6":
            print("Goodbye!")
            break

        elif option == "7":
            alert_low_stock()

        else:
            print("Invalid option.")
