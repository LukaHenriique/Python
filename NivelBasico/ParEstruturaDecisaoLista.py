# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:46:02 2020

@author: Lucas
"""
import random as rd

lista =[]
par =[]
impar=[]

for i in range(10): 

    valor = rd.randint(10,50) 
    lista.append(valor)         
   
    if valor%2 ==0 : 
        par.append(valor) 
    else:
        impar.append(valor)  
        
print("lista principal")
print(lista)
print("\nlistra numero pares")
print(par)
print("\nlista numero impares")
print(impar)
        
print("\no maior numero da lista:",max(lista)) 
print("\no meno numero da lista:",min(lista)) 
print("\na media",sum(lista)/len(lista))  