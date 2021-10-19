# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:23:35 2020

@author: Lucas
"""
import random as rd

lista = []
par = []


for i in range(10):
     valor = rd.randint(40,100)
     lista.append(valor)
     
     if i %2==0:
         par.append(valor)
         
print("lista")
print(lista)
print("pares",par)
    