# Questão 2
def cycle_sort(arr):
    """
    Realiza cycle sort in-place no array arr.
    Retorna o número de escritas feitas no array.
    """
    writes = 0                     
    n = len(arr)                   

    # percorre cada índice como início potencial de um ciclo
    for cycle_start in range(0, n - 1):
        item = arr[cycle_start]     # item que queremos posicionar corretamente

        # encontra a posição correta de item contando quantos elementos são menores
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1

        # se já está na posição correta, pula (nenhuma escrita necessária)
        if pos == cycle_start:
            continue

        # se houver duplicatas do mesmo valor, avançamos para a primeira posição livre
        while item == arr[pos]:
            pos += 1

        # coloca item em arr[pos], trocando com o que estava lá; conta como escrita
        arr[pos], item = item, arr[pos]
        writes += 1

        # agora rotacionamos o resto do ciclo até que voltemos a posição inicial
        while pos != cycle_start:
            pos = cycle_start
            # recalcula a posição correta para o item que foi deslocado
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            # pula duplicatas
            while item == arr[pos]:
                pos += 1
            # troca e conta escrita
            arr[pos], item = item, arr[pos]
            writes += 1

    return writes


if __name__ == "__main__":
    test = [3, 5, 2, 1, 4, 3]
    print("Antes:", test)
    w = cycle_sort(test)
    print("Depois:", test)
    print("Escritas:", w)
