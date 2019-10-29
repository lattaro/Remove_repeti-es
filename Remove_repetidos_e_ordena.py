def remove_repetidos(lista):
    lista.sort()
    b = 0
    c = 1
    while c <= len(lista):
        if lista [b] == lista [c]:
            del lista [b]
            b = 0
            c = 1
        else:
            b = b + 1
            c = c + 1
            if c >= len(lista):
                return lista
            
    
 
#lista = [1,2,3,7,8,10,4,1,1,1,1,2,4]

#print (remove_repetidos(lista))