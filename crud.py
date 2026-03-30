import csv
import os

DATA_CSV = os.path.join("data", "data.csv")


def crear_producto_csv(diccionario):
    registros = leer_producto_csv()

    # ✅ evitar duplicados
    for reg in registros:
        if reg["id"] == str(diccionario["id"]):
            print("Error: ya existe un producto con ese ID.")
            return False

    existe = os.path.isfile(DATA_CSV)

    with open(DATA_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=diccionario.keys())
        if not existe:
            writer.writeheader()
        writer.writerow(diccionario)

    return True


def leer_producto_csv():
    if not os.path.isfile(DATA_CSV):
        return []

    with open(DATA_CSV, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def actualizar_cliente_csv(id_valor, campo_id, nuevos_datos):
    registros = leer_producto_csv()
    actualizado = False

    for reg in registros:
        if reg[campo_id] == str(id_valor):
            reg.update(nuevos_datos)
            actualizado = True

    if actualizado:
        with open(DATA_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(registros)

    return actualizado


def eliminar_cliente_csv(id_valor, campo_id):
    registros = leer_producto_csv()
    nuevos = [reg for reg in registros if reg[campo_id] != str(id_valor)]

    if len(nuevos) != len(registros):
        with open(DATA_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(nuevos)
        return True

    return False


def buscar_por_id(id_valor, campo_id="id"):
    registros = leer_producto_csv()
    for reg in registros:
        if reg[campo_id] == str(id_valor):
            return reg
    return None


def buscar_por_nombre(nombre):
    registros = leer_producto_csv()
    resultados = []

    for reg in registros:
        if reg["nombre"].lower() == nombre.lower():
            resultados.append(reg)

    return resultados


def eliminar_por_nombre(nombre):
    registros = leer_producto_csv()
    nuevos = [reg for reg in registros if reg["nombre"].lower() != nombre.lower()]

    if len(nuevos) != len(registros):
        with open(DATA_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(nuevos)
        return True

    return False


def alertar_stock_bajo():
    registros = leer_producto_csv()

    bajos = [p for p in registros if int(p["cantidad"]) < 5]

    if not bajos:
        print("✅ No hay productos con stock bajo.")
        return

    print("\n⚠️ PRODUCTOS CON STOCK BAJO:")
    for p in bajos:
        if int(p["cantidad"]) <= 2:
            print(f"🔴 CRÍTICO: ID: {p['id']} | {p['nombre']} | Stock: {p['cantidad']}")
        else:
            print(f"🟡 Bajo:ID: {p['id']} | {p['nombre']} | Stock: {p['cantidad']}")
