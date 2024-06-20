import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import is_primo_circular, all_numbers_different, text_chain_based_on_digit_sum, CustomString, max_subsecuencia

## EJERCICIO 1

def test_is_primo_circular():
    assert is_primo_circular(1) == False
    assert is_primo_circular(2) == True
    assert is_primo_circular(7) == True
    assert is_primo_circular(197) == True # Ejemplo del enunciado
    assert is_primo_circular(1193) == True 
    assert is_primo_circular(23) == False # El 23 es primo pero el 32 no

## EJERCICIO 2

def test_all_numbers_different():
    assert all_numbers_different(123) == True # Ejemplo del enunciado
    assert all_numbers_different(222) == False # Ejemplo del enunciado
    assert all_numbers_different(1123) == False
    assert all_numbers_different(9876543210) == True
    assert all_numbers_different(122) == False

## EJERCICIO 3

def test_text_chain_based_on_digit_sum():
    assert text_chain_based_on_digit_sum(69810) == '669810' # Ejemplo del enunciado
    assert text_chain_based_on_digit_sum(3201) == '63201' # Ejemplo del enunciado
    assert text_chain_based_on_digit_sum(1234) == '11234'
    assert text_chain_based_on_digit_sum(987) == '6987'
    assert text_chain_based_on_digit_sum(5) == '55'

## EJERCICIO 4

def test_CustomString():
    cadena_inicial = CustomString("Ho,la")
    assert str(cadena_inicial) == "Hola"
    cadena2 = cadena_inicial + ","
    assert str(cadena2) == "Hola"
    cadena3 = cadena2 + " mundo"
    assert str(cadena3) == "Hola mundo"

## EJERCICIO 5

def test_max_subsecuencia():
    assert max_subsecuencia([-8, -4, 6, 8, -6, 10, -4, -4]) == ([6, 8, -6, 10], 18)
    assert max_subsecuencia([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == ([4, -1, 2, 1], 6)
    assert max_subsecuencia([1, 2, 3, 4, 5]) == ([1, 2, 3, 4, 5], 15)
    assert max_subsecuencia([-2, -3, 4, -1, -2, 1, 5, -3]) == ([4, -1, -2, 1, 5], 7)