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
    
    pivot = arr[-1]  
    left  = [x for x in arr[:-1] if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + mid + quick_sort(right)


def cycle_sort(arr):
    n = len(arr)
    for cycle_start in range(0, n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

# TESTE DE TEMPO
def medir_tempo(func, arr):
    A = arr.copy()
    inicio = time.time()
    if func == quick_sort:
        quick_sort(A)
    else:
        func(A)
    return time.time() - inicio

tamanhos = [1000, 10000, 20000, 30000, 40000, 50000]

algoritmos = [
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort, cycle_sort
]

nomes = [
    "Bubble", "Selection", "Insertion",
    "Merge", "Quick", "Cycle"
]


resultados = {nome: [] for nome in nomes}

for n in tamanhos:
    base = [random.randint(1, 1000000) for _ in range(n)]
    for alg, nome in zip(algoritmos, nomes):
        resultados[nome].append(medir_tempo(alg, base))

plt.figure(figsize=(10,6))
for nome in nomes:
    plt.plot(tamanhos, resultados[nome], label=nome)
plt.title("Tempo de Execução – Listas Randômicas")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo (s)")
plt.legend()
plt.grid(True)
plt.show()

desc = list(range(50000, 0, -1))
tempos_desc = []
for alg in algoritmos:
    tempos_desc.append(medir_tempo(alg, desc))

plt.figure(figsize=(8,5))
plt.bar(nomes, tempos_desc)
plt.title("Tempo em Lista Descendente – 50.000 elementos")
plt.ylabel("Tempo (s)")
plt.grid(True, axis='y')
plt.show()

for nome, t in zip(nomes, tempos_desc):
    print(nome, f"{t:.4f}s")


