# Inicio de sesión (Python)
[ES] Este es un módulo que implementa un sistema de autenticación básico por consola con un número limitado de intentos. Se puede integrar fácilmente como parte de otro proyecto integral, o bien, utilizarse como ejercicio de práctica.

## Funcionamiento:

El programa solicita al usuario que ingrese un nombre de usuario y una contraseña. Antes de validar, se verifica que ninguno de los campos esté vacío. Si se detecta un campo vacío, el sistema muestra un mensaje de advertencia sin descontar un intento.

Si ambos campos contienen información, se procede a verificar las credenciales ingresadas. Si estas no coinciden, se imprime error junto con el número de intentos de acceso restantes. Una vez alcanzado el número de intentos máximo, el acceso queda bloqueado.


## Configuración por defecto:

**Usuario registrado**: `admin`
**Contraseña registrada**: `1234`
**Intentos máximos**: `3`

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
