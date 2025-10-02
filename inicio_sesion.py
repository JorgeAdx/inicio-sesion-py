""" 
Este módulo es un sistema de inicio de sesión con datos de acceso
preconfigurados. Se puede cambiar el nombre de usuario, clave de acceso,
así como el número de intentos máximos de ingreso al sistema.

El programa tratará de ejecutar el programa hasta que el usuario ingrese
las credenciales correctas, o hasta que se alcance el número de intentos
máximo de acceso.

Autor: JorgeAdx
Fecha: 22 de septiembre de 2025
"""
# --- Configuración global ---
USUARIO_REGISTRADO = "admin"
CONTRASENA_REGISTRADA = "1234"
INTENTOS_MAXIMOS = 3

def solicitar_credenciales():
    """Pide usuario y contraseña al usuario"""
    usuario = input("Usuario: ").strip()    # .strip() elimina campos vacíos
    contrasena = input("Contraseña: ").strip()
    return usuario, contrasena

def validar_credenciales(usuario, contrasena):
    """Valida si las credenciales coinciden con las registradas"""
    if usuario == USUARIO_REGISTRADO and contrasena == CONTRASENA_REGISTRADA:
        return None    # Credenciales correctas
    return "Usuario o contraseña incorrectos."

def manejar_intentos(intentos_restantes):
    """Muestra los intentos restantes o bloquea el acceso"""
    if intentos_restantes > 0:
        print(f"Intentos restantes: {intentos_restantes}")
    else:
        print("Has alcanzado el número máximo de intentos. Acceso bloqueado.")

def inicio_sesion():
    """Define función principal del módulo"""
    print("\n--- Sistema de Inicio de Sesión ---")
    intentos_acceso = 0

    while intentos_acceso < INTENTOS_MAXIMOS:    # Bucle para solicitar credenciales
        usuario, contrasena = solicitar_credenciales()

        # Validar campos vacíos sin contar como intento
        if not usuario or not contrasena:
            print("Error de autenticación: No se permiten campos vacíos.")
            continue  # Vuelve a pedir credenciales sin aumentar contador

        # Validar credenciales
        error = validar_credenciales(usuario, contrasena)
        if error:
            print(error)
            intentos_acceso += 1
            intentos_restantes = INTENTOS_MAXIMOS - intentos_acceso
            manejar_intentos(intentos_restantes)
        else:
            print("Acceso concedido. ¡Bienvenido!")
            break

# Ejecutar función principal
inicio_sesion()
