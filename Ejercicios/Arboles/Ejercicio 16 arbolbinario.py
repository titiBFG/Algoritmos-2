from typing import Any, Generic, TypeVar

class ArbolBinarioEnteros:
    def __init__(self, elemento: int, esMenorFunction = lambda x,y: x < y):
        self.derecha = None
        self.izquierda = None
        self.elemento = elemento
        self.esMenor = esMenorFunction

    def agregarElemento(arbol, elemento):
        if (arbol.esMenor(elemento, arbol.elemento)):
            agregarIzquierda(arbol, elemento)      
        else:
            agregarDerecha(arbol, elemento)

                                              

def agregarIzquierda(arbol, elemento):
    if arbol.izquierda == None:
        arbol.izquierda = ArbolBinario(elemento, arbol.esMenor)
    else:
        agregarElemento(arbol.izquierda, elemento)

        

def agregarDerecha(arbol, elemento):
    if arbol.derecha == None:
        arbol.derecha = ArbolBinario(elemento, arbol.esMenor)
    else:
        agregarElemento(arbol.derecha, elemento)

T = TypeVar('T')

class ArbolBinario:
    def __init__(self, elemento: T, esMenorFunction = lambda x,y: x < y):
        pass