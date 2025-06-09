import random
import time
from integradorProgramacion1 import generar_medicamentos, burbuja_medicamentos, merge_sort_medicamentos, quick_sort_medicamentos, busqueda_lineal, busqueda_binaria

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