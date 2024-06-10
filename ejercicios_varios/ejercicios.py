import random

def leerMatriz():
    while True:
        try:
            nf = int(input('Cantidad de filas matriz -> '))
            nc = int(input('Cantidad de columnas matriz -> '))
            matriz = [[random.randint(1, 10) for _ in range(nc)] for _ in range(nf)]
            return matriz
        except ValueError:
            print("el caracter ingresado no coincide con el caracter pedido, porfavor vuelve a digitarlo")

def leerVectorR():
    while True:
        try:
            cd = int(input('Cantidad de datos lista -> '))
            lista = [random.randint(1, 10) for _ in range(cd)]
            return lista
        except ValueError:
            print("el caracter ingresado no coincide con el caracter pedido, porfavor vuelve a digitarlo")

def fibonacci(valor):
        a=0
        b=1
        t=0
        while t<valor :
            t=a+b
            a=b
            b=t
        if t==valor:
            return True
        else:
            return False

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def factorial(dato):
    factorial=dato
    multiplo=dato-1
    while multiplo>0:
        factorial=factorial*multiplo
        multiplo-=1
    return factorial

def contar_primos_en_matrices(matriz_1, matriz_2):
    diccionario = {}
    
    for fila in matriz_1:
        for numero in fila:
            if primo(numero):
                if numero in diccionario:
                    diccionario[numero] += 1
                else:
                    diccionario[numero] = 1
    
    for fila in matriz_2:
        for numero in fila:
            if primo(numero):
                if numero in diccionario:
                    diccionario[numero] += 1
                else:
                    diccionario[numero] = 1

    return diccionario

def contar_caracteres(cadena):
    diccionario_digito = {}
    diccionario_caracter = {}

    for caracter in cadena:
        if caracter.isdigit():
            if caracter in diccionario_digito:
                diccionario_digito[caracter] += 1
            else:
                diccionario_digito[caracter] = 1
        elif caracter.isalpha():
            if caracter in diccionario_caracter:
                diccionario_caracter[caracter] += 1
            else:
                diccionario_caracter[caracter] = 1

    return diccionario_digito, diccionario_caracter

        