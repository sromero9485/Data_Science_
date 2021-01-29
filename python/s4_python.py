# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Obtener el número mínimo en una lista 
#la entrada : lista de enteros
#la salida : el mínimo de la lista de enteros
#primer paso : iterar en la lista
#segundo paso: comparar el valor actual con el mínimo de los anteriores
#tercer paso: obtener mínimo 

def minimo(lista):
    x = lista[0]
    for i in range(1,len(lista)):
        e = lista[i]
        if e < x:
            x = e
    return x

           
l= [3, -2, 5, -1]    
res = minimo(l)
print(res)

def pos(lista):
    x = lista[0]
    p = 0
    for i in range(1,len(lista)):
        e = lista[i]
        if e < x:
            p=i
            x = e
    return p

           
   
#res = minimo(l)
#print(res)


#Ordenar una lista de menor a mayor 
#la entrada : lista de enteros 
#la salida : lista de enteros ordenada de menor a mayor 
#primer paso: encontrar el mínimo de la lista
#seundo paso: agregar mínimo a Lista ordenada


def ordenada(lista):
    l=lista
    L=[]
    for i in range(len(lista)):
        j = pos(l)
        L.append(l[j])
        lista.pop(j)
    return L
res2 = ordenada(l)
print(res2)   
        
    
    




      