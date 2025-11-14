# Questão 3

import random
import time
import matplotlib.pyplot as plt


# ALGORITMOS DE ORDENAÇÃO
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def heap_sort(arr):
    n = len(arr)

    def heapify(arr, n, i):
        largest = i 
        l = 2*i + 1 
        r = 2*i + 2 

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# TESTE DE TEMPO
def medir_tempo(func, arr):
    A = arr.copy()
    inicio = time.time()
    if func == quick_sort:
        quick_sort(A)
    else:
        func(A)
    return time.time() - inicio

tamanhos_pequenos = [1000, 5000, 10000]
tamanhos_grandes = [10000, 20000, 30000, 40000, 50000]

algoritmos_quadraticos = [bubble_sort, selection_sort, insertion_sort]
algoritmos_eficientes = [merge_sort, quick_sort, heap_sort]

nomes_quad = ["Bubble", "Selection", "Insertion"]
nomes_eff  = ["Merge", "Quick", "Heap"]


# TESTE 1 – Listas RANDÔMICAS

resultados_quad = {nome: [] for nome in nomes_quad}
resultados_eff  = {nome: [] for nome in nomes_eff}

print("Rodando testes...")

for n in tamanhos_pequenos:
    base = [random.randint(1, 1000000) for _ in range(n)]
    for alg, nome in zip(algoritmos_quadraticos, nomes_quad):
        resultados_quad[nome].append(medir_tempo(alg, base))

for n in tamanhos_grandes:
    base = [random.randint(1, 1000000) for _ in range(n)]
    for alg, nome in zip(algoritmos_eficientes, nomes_eff):
        resultados_eff[nome].append(medir_tempo(alg, base))


# GRAFICO 1 – Listas Randômicas

plt.figure(figsize=(10,6))
for nome in nomes_quad:
    plt.plot(tamanhos_pequenos, resultados_quad[nome], label=nome)

for nome in nomes_eff:
    plt.plot(tamanhos_grandes, resultados_eff[nome], label=nome)

plt.title("Tempo de Execução – Listas Randômicas")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo (s)")
plt.legend()
plt.grid(True)
plt.show()


# TESTE 2 – Lista de 50.000 DESCENDENTE

desc = list(range(50000, 0, -1))
tempos_desc = []

for alg in algoritmos_eficientes:
    tempos_desc.append(medir_tempo(alg, desc))

plt.figure(figsize=(8,5))
plt.bar(nomes_eff, tempos_desc)
plt.title("Tempo em Lista Descendente – 50.000 elementos")
plt.ylabel("Tempo (s)")
plt.grid(True, axis='y')
plt.show()

print("\nTempos em lista descendente:")
for nome, t in zip(nomes_eff, tempos_desc):
    print(f"{nome}: {t:.4f}s")
