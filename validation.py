"""
def leer_float(mensaje):
    while True:
        entrada = input(mensaje).strip()

        if not entrada:
            print("El valor no puede estar vacío.")
            continue

        # contar separadores
        if entrada.count(".") + entrada.count(",") > 1:
            print("Formato inválido. Solo un separador decimal.")
            continue

        valido = True

        for c in entrada:
            if not (c.isdigit() or c in ".,"):
                valido = False
                break

        if not valido:
            print("Formato inválido. Solo números y un separador decimal.")
            continue

        # evitar casos como "." o ","
        if entrada in [".", ","]:
            print("Formato inválido.")
            continue

        # normalizar coma a punto
        entrada = entrada.replace(",", ".")

        try:
            valor = float(entrada)
        except ValueError:
            print("Número inválido.")
            continue

        if valor <= 0:
            print("Debe ser mayor que 0.")
            continue

        return valor

        #OTRA VALIDATION SINO AHORA DE EMAIL

        def leer_email(mensaje):
    while True:
        email = input(mensaje).strip()

        # vacío
        if not email:
            print("El email no puede estar vacío.")
            continue

        # espacios
        if " " in email:
            print("El email no puede contener espacios.")
            continue

        # un solo @
        if email.count("@") != 1:
            print("Debe contener un solo '@'.")
            continue

        # ❌ puntos consecutivos
        if ".." in email:
            print("No se permiten puntos consecutivos.")
            continue

        usuario, dominio = email.split("@")

        # validar usuario
        if not usuario:
            print("El email debe tener texto antes del '@'.")
            continue

        # validar dominio
        if "." not in dominio:
            print("El dominio debe contener un punto (ej: .com).")
            continue

        partes = dominio.split(".")

        if len(partes) < 2:
            print("Dominio inválido.")
            continue

        extension = partes[-1]

        if len(extension) < 2 or not extension.isalpha():
            print("Extensión inválida (ej: .com, .co).")
            continue

        # validar caracteres permitidos
        permitido = True
        for c in email:
            if not (c.isalnum() or c in "._%+-@"):
                permitido = False
                break

        if not permitido:
            print("El email contiene caracteres inválidos.")
            continue

        return email
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
