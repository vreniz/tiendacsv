# pylint: disable=missing-function-docstring
from crud import *
import re


def menu():
    print("\n--- GESTION DE PRODUCTOS TIENDA PABLITO ---")
    print("1. Crear Producto")
    print("2. Leer Productos")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Buscar Producto")
    print("6. Salir")
    print("7. Ver productos con stock bajo")
    print("------------------------------")


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Debe ser un número entero no negativo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")


def leer_float(mensaje):
    patron = r"^\d+([.,]\d+)?$"  # 👈 solo números + un separador decimal válido

    while True:
        entrada = input(mensaje).strip()

        if not entrada:
            print("El valor no puede estar vacío.")
            continue

        if not re.match(patron, entrada):
            print("Formato inválido. Use número válido (ej: 10, 10.5, 10,5).")
            continue

        entrada = entrada.replace(",", ".")  # 👈 normalizamos

        valor = float(entrada)

        if valor <= 0:
            print("Debe ser mayor que 0.")
        else:
            return valor


"""
def leer_float_no_negativo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Debe ser un número no negativo y diferente de 0.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debe ser un número válido.")
"""

# import re  # 👈 descomentar si vas a usar validación de email

# def leer_email(mensaje):
#     """
#     Función para solicitar y validar un correo electrónico.
#     - No permite vacío
#     - Valida formato básico: texto@texto.dominio
#     - Evita espacios y caracteres inválidos
#     """
#
#     patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#
#     while True:
#         email = input(mensaje).strip()
#
#         # ❌ vacío
#         if not email:
#             print("El email no puede estar vacío.")
#             continue
#
#         # ❌ espacios internos
#         if " " in email:
#             print("El email no puede contener espacios.")
#             continue
#
#         # ❌ formato inválido
#         if not re.match(patron, email):
#             print("Formato inválido. Ej: usuario@gmail.com")
#             continue
#
#         # ✅ válido
#         return email


def leer_texto1(mensaje):
    while True:
        texto = input(mensaje)

        if texto is None:
            print("Entrada inválida.")
            continue

        texto = texto.strip()

        if texto == "":
            print("El campo no puede estar vacío.")
            continue

        if texto.isdigit():
            print("No puede contener solo números.")
            continue

        return texto


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if not texto:
            print("El campo no puede estar vacío.")
            continue

        if texto.isdigit():
            print("No puede contener solo números.")
            continue

        valido = True

        for c in texto:
            if not (c.isalpha() or c.isdigit() or c.isspace()):
                valido = False
                break

        if not valido:
            print("Formato inválido. Solo letras, números y espacios.")
            continue

        return texto


""" EXPRESIONES REGULARES
def leer_texto(mensaje):
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+( [A-Za-zÁÉÍÓÚáéíóúÑñ0-9]+)*$"

    while True:
        texto = input(mensaje).strip()

        if not texto:
            print("El campo no puede estar vacío.")
            continue

        if texto.isdigit():
            print("No puede contener solo números.")
            continue

        if not re.match(patron, texto):
            print("Formato inválido. Ej: Tomate, Tomate Chonto, Iphone 11")
            continue

        return texto
"""

"""        
def pedir_datos():
    try:
        id = int(input("ID: "))
        if id <= 0:
            print("El ID no puede ser negativo o 0.")
            return None
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: "))
        if precio <= 0:
            print("El precio no puede ser negativo o 0.")
            return None
        cantidad = int(input("Ingerese la cantidad en stock: "))
        if cantidad <= 0:
            print("Cantidad no puede ser un numero negativo o 0")
            return None
    except ValueError:
        print("Error: ID y cantidad deben ser números enteros no negativos.")
        print("Nota: ID no puede ser un numero decimal")
        return None
    categoria = input("Ingrese la categoría: ").strip()

    return {
        "id": id,
        "nombre": nombre,
        "Precio": precio,
        "categoria": categoria,
        "cantidad": cantidad,
    }"""


def pedir_datos():
    id = leer_entero_positivo("ID: ")
    nombre = leer_texto("Nombre: ").strip()
    precio = leer_float("Precio: ")
    categoria = leer_texto("Categoria: ").strip()
    cantidad = leer_entero_positivo("Cantidad: ")

    return {
        "id": id,
        "nombre": nombre,
        "Precio": precio,
        "categoria": categoria,
        "cantidad": cantidad,
    }


def pedir_datos_update():
    nombre = leer_texto("Nombre: ")
    precio = leer_float("Precio: ")
    categoria = leer_texto("Categoria: ")
    cantidad = leer_entero_positivo("Cantidad: ")

    return {
        "nombre": nombre,
        "Precio": precio,
        "categoria": categoria,
        "cantidad": cantidad,
    }


if __name__ == "__main__":
    while True:
        menu()
        op = input("Elige una opción: ")

        if op == "1":
            datos = pedir_datos()
            if datos:
                guardado = crear_producto_csv(datos)  # ✅ CAMBIO
                if guardado:
                    print("Producto guardado en CSV.")

        elif op == "2":
            registros = leer_producto_csv()  # ✅ CAMBIO
            if registros:
                print("\nProductos:")
                for r in registros:
                    print(r)
            else:
                print("No hay Productos registrados en el Tienda")

        elif op == "3":
            id_valor = int(input("ID del producto a actualizar: "))
            nuevos = pedir_datos_update()
            ok = actualizar_cliente_csv(id_valor, "id", nuevos)  # ✅ CAMBIO
            print("Actualizado." if ok else "No encontrado producto no existe2.")

        elif op == "4":
            tipo = input("Eliminar por (1) ID o (2) Nombre: ")
            if tipo == "1":
                try:
                    id_valor = int(input("ID del producto a eliminar: "))
                    if id_valor <= 0:
                        print("El ID debe ser positivo diferente de 0.")
                    else:
                        ok = eliminar_cliente_csv(id_valor, "id")
                        print("Eliminado." if ok else "No encontrado.")
                except ValueError:
                    print("Error: el ID debe ser un número entero válido.")
            elif tipo == "2":
                nombre = input("Nombre del producto a eliminar: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                else:
                    ok = eliminar_por_nombre(nombre)
                    print("Eliminado." if ok else "No encontrado.")

        elif op == "5":
            tipo = input("Buscar por (1) ID o (2) Nombre: ")

            if tipo == "1":
                id_valor = int(input("Ingrese ID: "))
                cliente = buscar_por_id(id_valor)

                if cliente:
                    print("\nProducto encontrado:")
                    print(cliente)
                else:
                    print("No encontrado.")

            elif tipo == "2":
                nombre = input("Ingrese nombre: ").strip().lower()
                resultados = buscar_por_nombre(nombre)

                if resultados:
                    print("\nProductos encontrados:")
                    for r in resultados:
                        print(r)
                else:
                    print("No se encontraron Productos.")

        elif op == "6":
            print("¡Hasta luego!")
            break
        elif op == "7":
            alertar_stock_bajo()

        else:
            print("Opción inválida.")
