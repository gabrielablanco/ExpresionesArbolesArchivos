from pila import *
from arbol import *
from diccionario import *
from expresiones_out import *


def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0], nodo_izq, nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:], pila)


def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)


pila = Pila()
archivo = open("expresionesin.txt" , "r")

for linea in archivo.readlines():
    linea = linea.strip("\n")
    lista = linea.split(" ")
    for i in lista: # Se hace un for para realizar la comparación de caracter por caracter
        numero = i
        if not isinstance(i, (str)): #Si es alfabético se busca en el diccionario el número
           numero = buscar_diccionario("'" + i + "'")
        # FALTA ASIGNARLE EL NUMERO RETORNADO EN LA VARIABLE NUMERO A LA POSICION DE LA LISTA
    convertir(lista, pila)
    x = str(evaluar(pila.desapilar()))
    archivo_out = guardar_resultado(x)

archivo.close()


#



