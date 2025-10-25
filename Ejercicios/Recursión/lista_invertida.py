def anota(func):
    def wrapper(*args, **kwargs):
        # Imprimir nombre de la función y argumentos
        print(f"Llamando a: {func.__name__}")
        print(f"Args: {args}")
        # Ejecutar la función original
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper

@anota
def invertir_lista_rec(lista):
    if len(lista) <= 1:
        return lista
    else:
        lista_invertida = lista[:1]
        sublista = lista[1:]
        return invertir_lista_rec(sublista) + lista_invertida

print(invertir_lista_rec([1,2,3,4,5]))