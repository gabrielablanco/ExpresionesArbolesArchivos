from pila import *
from arbol import *
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
    print (linea)
    lista = linea.split(" ")
    print(lista)
    convertir(lista, pila)
    x = str(evaluar(pila.desapilar()))
    archivo_out = guardar_resultado(x)
archivo.close()


#



