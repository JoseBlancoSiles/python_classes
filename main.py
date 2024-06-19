# FUNCIONES

## FUNCIONES EJERCICIO 1

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

## FUNCIONES EJERCICIO 2

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