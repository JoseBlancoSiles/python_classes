# IMPORTS

import string

## EJERCICIO 1

def is_primo(num):
    '''Función que recibe un número y devuelve True para números primos y false para números no primos'''
    if num <= 1 or (num > 2 and num % 2 == 0):
        return False
    if num == 2:
        return True
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def rotar_numero(num):
    '''Recibe un número y guarda en una lista todas sus rotaciones'''
    rotaciones = []
    s = str(num)
    for i in range(len(s)):
        rotaciones.append(int(s[i:] + s[:i]))
    return rotaciones

def is_primo_circular(num):
    '''Recibe un número y devuelve True si es un primo circular, false si no lo es'''
    if not is_primo(num):
        return False
    for rotacion in rotar_numero(num):
        if not is_primo(rotacion):
            return False
    return True

## EJERCICIO 2

def all_numbers_different(num):
    '''Recibe un número y devuelve True si todos los dígitos son diferentes, false si al menos un número se repite'''
    if num < 10:
        return True
    digitos_vistos = set()
    s = str(num)
    for digito in s:
        if digito in digitos_vistos:
            return False
        digitos_vistos.add(digito)
    return True

## EJERCICIO 3

def text_chain_based_on_digit_sum(num):
    '''Recibe un número, devuelve la última suma válida y la añade a la izquierda del número recibido'''
    suma = sumar_digitos(num)
    while suma > 9:
        suma = sumar_digitos(suma)
    return str(suma) + str(num)

def sumar_digitos(num):
    '''Recibe un número  súma sus dígitos'''
    s = str(num)
    suma = 0
    for digito in s:
        suma += int(digito)
    return suma

## EJERCICO 4

import string

class CustomString:
    def __init__(self, cadena_inicial):
        self.caracteres_permitidos = set(string.ascii_letters + ' ')
        self.value = self.filtrar_string(cadena_inicial)
    
    def filtrar_string(self, s):
        '''Filtra los caracteres no permitidos de una cadena, los muestra y devuelve la cadena filtrada'''
        no_permitidos = []
        permitido = ''
        for caracter in s:
            if caracter not in self.caracteres_permitidos:
                no_permitidos.append(caracter)
            else:
                permitido += caracter
        if no_permitidos: 
            print(f'La instancia creada solo puede contener caracteres de la "a" a la "z". Los caracteres: {no_permitidos} se eliminarán')
        return permitido
    
    def __str__(self):
        return self.value
    
    def __add__(self, s):
        filtrado = self.filtrar_string(s)
        cadena = self.value + filtrado
        return CustomString(cadena)