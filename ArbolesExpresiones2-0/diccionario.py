#Los siguientes caracteres serán numerados dependiendo de su posición en el alfabeto.

d = {'a':1,
     'b':2,
     'c':3,
     'd':4,
     'e':5,
     'f':6,
     'g':7,
     'h':8,
     'i':9,
     'j':10,
     'k':11,
     'l':12,
     'm':13,
     'n':14,
     'ñ':15,
     'o':16,
     'p':17,
     'q':18,
     'r':19,
     's':20,
     't':21,
     'u':22,
     'v':23,
     'w':24,
     'x':25,
     'y':26,
     'z':27
     }
#Ya no se almacenan índices en la variable d, sino claves que deberán tener algún valor

#Ahora se crea una función que busque el valor que se necesite en el diccionario
def buscar_diccionario(valor):
     resultado = d.get(valor, valor)
     return str(resultado)
