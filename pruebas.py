from email_validator import validate_email, EmailNotValidError

def validar_correo_electronico(correo):
    try:
        # Usamos la función validate_email para validar el correo electrónico
        validador = validate_email(correo)
        # Si la dirección es válida, devuelve True
        return True
    except EmailNotValidError:
        # Si ocurre un error, significa que la dirección no es válida, entonces devuelve False
        return False

# Ejemplo de uso
correo = "usuario@gmail.com"
if validar_correo_electronico(correo):
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")
