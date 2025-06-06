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

# Definimos la funcion que hara el metodo por "burbujeo" comparando los elementos por el campo "nombre" y devuelve una nueva lista ordenada sin modificar la original
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
    if len(lista) <= 1:
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
        menores = [x for x in lista[1:] if x["nombre"] <= pivote["nombre"]]
        mayores = [x for x in lista[1:] if x["nombre"] > pivote["nombre"]]
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


# #--------------#
# Prueba de codigo
# #--------------#

# Generar datos
longitud_lista = int(input("Ingrese la cantidad de elementos que desea que tenga la lista de medicamentos: "))
lista_meds = generar_medicamentos(longitud_lista)
objetivo = random.choice(lista_meds)["nombre"]

print(f"\n Buscando medicamento: {objetivo}")

# Se realiza la búsqueda del medicamento en distintos escenarios para comparar eficiencia:
# 1. Búsqueda lineal sobre lista desordenada.
# 2. Ordenamiento + búsqueda binaria con Burbuja.
# 3. Ordenamiento + búsqueda binaria con Merge Sort.
# 4. Ordenamiento + búsqueda binaria con Quick Sort.
# 5. Usamos time.perf_counter() ya que es ideal para medir cuánto tarda en ejecutarse un algoritmo o comparar rendimiento

# --- Búsqueda lineal en lista desordenada ---
tiempo_inicial = time.perf_counter()
resultado_lineal = busqueda_lineal(lista_meds, objetivo)
tiempo_final = time.perf_counter()
print("\n Búsqueda lineal:")
print(f"Resultado: {resultado_lineal}")
print(f"Tiempo de Busqueda: {tiempo_final - tiempo_inicial:.15f} segundos")

# --- Ordenar con Burbuja + Búsqueda binaria ---
tiempo_inicial_ordenamiento = time.perf_counter()
lista_burbuja = burbuja_medicamentos(lista_meds)
tiempo_final_ordenamiento = time.perf_counter()

tiempo_inicial = time.perf_counter()
resultado_burbuja = busqueda_binaria(lista_burbuja, objetivo)
tiempo_final = time.perf_counter()
print("\n Ordenamiento Burbuja + Búsqueda binaria:")
print(f"Resultado: {resultado_burbuja}")
print(f"Tiempo de Ordenamiento: {tiempo_final_ordenamiento - tiempo_inicial_ordenamiento:.15f} segundos")
print(f"Tiempo de Busqueda: {tiempo_final - tiempo_inicial:.15f} segundos")

# --- Ordenar con Merge Sort + Búsqueda binaria ---
tiempo_inicial_ordenamiento = time.perf_counter()
lista_merge = merge_sort_medicamentos(lista_meds)
tiempo_final_ordenamiento = time.perf_counter()

tiempo_inicial = time.perf_counter()
resultado_merge = busqueda_binaria(lista_merge, objetivo)
tiempo_final = time.perf_counter()
print("\n Ordenamiento Merge Sort + Búsqueda binaria:")
print(f"Resultado: {resultado_merge}")
print(f"Tiempo de Ordenamiento: {tiempo_final_ordenamiento - tiempo_inicial_ordenamiento:.15f} segundos")
print(f"Tiempo de Busqueda: {tiempo_final - tiempo_inicial:.15f} segundos")

# --- Ordenar con Quick Sort + Búsqueda binaria ---
tiempo_inicial_ordenamiento = time.perf_counter()
lista_quick = quick_sort_medicamentos(lista_meds)
tiempo_final_ordenamiento = time.perf_counter()

tiempo_inicial = time.perf_counter()
resultado_quick = busqueda_binaria(lista_quick, objetivo)
tiempo_final = time.perf_counter()
print("\n Ordenamiento Quick Sort + Búsqueda binaria:")
print(f"Resultado: {resultado_quick}")
print(f"Tiempo de Ordenamiento: {tiempo_final_ordenamiento - tiempo_inicial_ordenamiento:.15f} segundos")
print(f"Tiempo de Busqueda: {tiempo_final - tiempo_inicial:.15f} segundos")

# Conclusión esperada:
# - La búsqueda binaria es mucho más rápida que la lineal, pero requiere ordenamiento previo.
# - Merge y Quick Sort son más eficientes que Burbuja, especialmente con listas grandes.