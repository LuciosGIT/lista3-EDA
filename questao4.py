def existe_par_com_soma(lista, alvo):
    vistos = set()  
    
    for num in lista:
        complemento = alvo - num
        
        
        if complemento in vistos:
            return True
        vistos.add(num)
    
    return False


lista = [10, 5, 3, 7, 2]
alvo = 12
print(existe_par_com_soma(lista, alvo))


def existe_par_com_soma2(lista, alvo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                return True
    return False


lista = [10, 5, 3, 7, 2]
alvo = 12
print(existe_par_com_soma2(lista, alvo))

