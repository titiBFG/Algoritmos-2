def permutaciones(lista):
    resultados = []

    def backtrack(solucion_parcial, restantes):
        # Caso base: si no quedan elementos por agregar
        if not restantes:
            resultados.append(solucion_parcial[:])  # copiar lista
            return
        # Caso recursivo: probar cada opción
        for i in range(len(restantes)):
            # Elegimos un elemento
            elegido = restantes[i]
            # Avanzamos: lo agregamos a la solución parcial
            solucion_parcial.append(elegido)
            # Llamada recursiva con los restantes sin el elegido
            backtrack(solucion_parcial, restantes[:i] + restantes[i+1:])
            # Backtrack: deshacemos la elección
            solucion_parcial.pop()

    backtrack([], lista)
    return resultados

# Ejemplo de uso
print(permutaciones([6,2,3]))