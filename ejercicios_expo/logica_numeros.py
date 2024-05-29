def num_bin():
    try:
        numero = int()
        binario = bin(numero)[2:]
    except ValueError:
        print("Por favor, introduce un número válido.")

def num_oct():
    try:
        numero = int()
        octal = oct(numero)[2:]
        
    except ValueError:
        print("Por favor, introduce un número válido.")

def num_hex():
    try:
        numero = int()
        hexadecimal = hex(numero)[2:]
    except ValueError:
        print("Por favor, introduce un número válido.")