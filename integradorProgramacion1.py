import random
import time

# "random" es una libreria que sera utilizada par aleatorizar la generacion de datos para este TP
# "time" es una libreria que sera utilizada para medir los tiempos de ejecucion de estos algoritmos de busqueda y ordenamientos


# Vamos a crear las listas que usaremos de bases para generar "medicamentos" aleatoriamente
drogas = ["Enalapril", "Losartan", "Carvedilol", "Espironolactona", "Atenolol", "Diclofenac", "Meloxicam", "Rosuvastatina", "Simvastatina", "Pregabalina", "Metformina", "Clonazepam", "Alprazolam", "Quetiapina", "Tamsulosina", "Atorvastatina", "Zolpidem", "Levotiroxina", "Bisoprolol", "Amlodipina"]

laboratorios = ["Bayer", "Roche", "Pfizer", "Novartis", "GSK", "Sanofi", "Abbvie", "Merck", "AstraZeneca", "Teva"]

# Declaramos funcion que genera una lista de diccionarios, donde cada diccionario representa un medicamento con un nombre (droga + laboratorio), un correo generado automáticamente y un número de teléfono aleatorio.
def generar_medicamentos(cantidad):
    medicamentos = []
    for _ in range(cantidad):
        droga = random.choice(drogas)
        laboratorio = random.choice(laboratorios)
        nombre = f"{droga} {laboratorio}"
        correo = f"{droga.lower()}{laboratorio.lower()}@gmail.com"
        telefono = f"11-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        medicamento = {
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono
        }
        medicamentos.append(medicamento)
    return medicamentos

# Ejemplo de Lista con diccionarios visual:
# listaMed:[
#     {'nombre': 'Metformina AstraZeneca', 'correo': 'metforminaastrazeneca@gmail.com', 'telefono': '11-9972-3997'},
#     {'nombre': 'Amoxicilina Teva', 'correo': 'amoxicilinateva@gmail.com', 'telefono': '11-2939-8505'},
#     {'nombre': 'Levotiroxina Teva', 'correo': 'levotiroxinateva@gmail.com', 'telefono': '11-5174-3649'},
#     {'nombre': 'Ibuprofeno Roche', 'correo': 'ibuprofenoroche@gmail.com', 'telefono': '11-4340-4663'},
#     {'nombre': 'Amoxicilina Pfizer', 'correo': 'amoxicilinapfizer@gmail.com', 'telefono': '11-1900-6975'}
#]

# #--------------#
# Ahora definiremos las funciones de ORDENAMIENTO
# #--------------#

# Definimos la funcion que hara el ordenamiento por metodo de "burbujeo" comparando los elementos "vecinos" por el campo "nombre" y devuelve una nueva lista ordenada sin modificar la original
def burbuja_medicamentos(lista):
    nueva_lista = lista.copy()
    n = len(nueva_lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nueva_lista[j]["nombre"] > nueva_lista[j + 1]["nombre"]:
                nueva_lista[j], nueva_lista[j + 1] = nueva_lista[j + 1], nueva_lista[j]
    return nueva_lista


# Definimos la funcion que hara el ordenamiento por "Merge Sort" usando el concepto de recursividad y dividiendo la lista en mitades y devuelve una nueva lista ordenada sin modificar la original
def merge_sort_medicamentos(lista):
    if len(lista) <= 1: # CASO BASE: listas de 0 o 1 elemento ya están ordenadas
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort_medicamentos(lista[:medio])
    derecha = merge_sort_medicamentos(lista[medio:])
    
    return merge(izquierda, derecha)

# Función auxiliar para combinar dos listas ordenadas en una sola lista ordenada.
def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i]["nombre"] <= der[j]["nombre"]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado

# Puntos a tener en cuenta de Merge Sort:
    # Eficiente para listas grandes.
    # Tiempo de ejecución garantizado: O(n log n) en todos los casos.
    # Estable (conserva el orden relativo de elementos con claves iguales).
    # Uso de memoria extra: requiere espacio adicional para las sublistas.



# Definimos la funcion que hara el ordenamiento por "Quick Sort" usando el concepto de recursividad y eligiendo el primer elemento como pivote. Devuelve una nueva lista ordenada sin modificar la original.
def quick_sort_medicamentos(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]

        menores = []
        mayores = []

        for i in lista[1:]:
            if i["nombre"] <= pivote["nombre"]:
                menores.append(i)
            else:
                mayores.append(i)


        return quick_sort_medicamentos(menores) + [pivote] + quick_sort_medicamentos(mayores)

# Puntos a tener en cuenta de Quick Sort:
    # Ventaja: Muy rápido en la práctica.
    # Desventaja: Peor caso costoso si el pivote siempre es el mínimo o máximo.
    # No es estable.



# #--------------#
# Ahora definiremos las funciones de BUSQUEDA
# #--------------#

# Busqueda desordenada. Recorre la lista secuencialmente para encontrar el medicamento buscado.
def busqueda_lineal(lista, objetivo):
    for medicamento in lista:
        if medicamento["nombre"] == objetivo:
            return medicamento
    return None

# Busqueda Ordenada. Realiza una busqueda sobre una lista previamente ordenada por el campo "nombre".
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = lista[medio]["nombre"]

        if nombre_medio == objetivo:
            return lista[medio]
        elif nombre_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

