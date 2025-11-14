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
