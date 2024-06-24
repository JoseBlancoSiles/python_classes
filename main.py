# IMPORTS

import string
import os

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
    
## EJERCICIO 5

def max_subsecuencia(list_num):
    '''Recibe una lista de enteros y devuelve una tupla(lista_numeros_max_subsecuencia, suma_max_subsecuencia)'''
    suma_actual = list_num[0]
    suma_max = list_num[0]
    izq = temp_izq = der = 0

    for i in range(1, len(list_num)):
        if suma_actual < 0:
            suma_actual = list_num[i]
            temp_izq = i
        else:
            suma_actual += list_num[i]

        if suma_actual > suma_max:
            suma_max = suma_actual
            der = i
            izq = temp_izq

    return (list_num[temp_izq:der + 1], suma_max)

# EJERCICIO 6

def ordenar_0_1(list_num):
    '''Recibe una lista de números entre 0 y 1 y los ordena ascendentemente'''
    num_total = len(list_num)
    num_ceros = list_num.count(0)
    return [0] * num_ceros + [1] * (num_total - num_ceros)

ordenar_0_1([0,1,1,1,0])

# EJERCICIO 7

class Ordenador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
class Sobremesa(Ordenador):
    def __init__(self, marca, modelo, volumen):
        super().__init__(marca, modelo)
        self.volumen = volumen

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Volumen: {self.volumen} L"

class Portatil(Ordenador):
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo)
        self.bateria = bateria

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Batería: {self.bateria} h"
    
# EJERCICIO 8

class Usuario:
    numero_usuarios = 0
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        Usuario.numero_usuarios += 1

    @classmethod
    def contar_numero_usutarios(cls):
        return f"El número de usuarios creados es {cls.numero_usuarios}"
    
# EJERCICIO 9

import os

class Archivos:
    def __init__(self, directorio):
        self.directorio = directorio
        os.makedirs(directorio)
    
    def listar(self):
        for archivo in os.listdir(self.directorio):
            print(archivo)
    
    def crear(self, archivo):
        ruta = os.path.join(self.directorio, archivo) 
        with open(ruta, 'a'):
            pass
    
    def eliminar(self, archivo):
        ruta = os.path.join(self.directorio, archivo) 
        os.remove(ruta)

    @staticmethod
    def obtener_extension(archivo):
        return os.path.splitext(archivo)[1]
    
class ArchivosAudio(Archivos):
    EXTENSIONES = ['.wav', '.mp3']

    def __init__(self, directorio):
        super().__init__(directorio)
    
    def listar(self):
        for archivo in os.listdir(self.directorio):
            if self.extension_valida(archivo):
                print(archivo)
    
    def crear(self, archivo):
        if self.extension_valida(archivo):
            super().crear(archivo)
    
    def eliminar(self, archivo):
        if self.extension_valida(archivo):
            super().eliminar(archivo)

    @staticmethod
    def extension_valida(archivo):
        '''Método para devolver is la extensión es válida y así no tener que comprobarlo para todos los otros métodos'''
        extension = os.path.splitext(archivo)[1]
        return extension in ArchivosAudio.EXTENSIONES
    
# EJERCICIO 10
# TO DO 
# class Producto:
#     def __init__(self, nombre, precio, stock):
#         self.nombre = nombre
#         self.precio = precio
#         self.stock = stock

# class Carrito:
#     def __init__(self):
#         self.productos = []
    
#     def agregar_articulo(self, producto):
#         pass