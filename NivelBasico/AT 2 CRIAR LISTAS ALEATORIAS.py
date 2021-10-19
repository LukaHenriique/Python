# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:56:12 2020

@author: Lucas
"""

import random as rd # ---> aqui ele ira importar os numero aleatorios, senpre ele tem que  vim primeiro. ser importado antes de ser ultilizados os numero 

lista =[]
par =[]
impar=[]

for i in range(20): # range() --> sua funcao e ir incrementando e decrementando, que nesse caso ele retornara uma seria de numerica no intervalo enviado 

    valor = rd.randint(50,100) # rd e randi vem da variavel import random quem inportara as variaveis e o int vem porque quero numero inteiro dentro da funcao (50,100) sao os numero que eu quero
    lista.append(valor)         # lista sao os numeros que ele criara o append ira armazenara todo aquele valor da lista(50,100)dentro da variavel valor 
   
    if valor%2 ==0 : # buscara os pares dentro da variavel armazenada valor 
        par.append(valor)  # o append puxara todas as variaveis para e quardara todas dentro da variavel valor 
    else:
        impar.append(valor) # caso se nao for par e for impara aqui o apped quardara tudo detro da variavel valor os numeros impares 
        
print("lista principal")
print(lista)
print("\nlistra numero pares")
print(par)
print("\nlista numero impares")
print(impar)
        
print("\no maior numero da lista:",max(lista)) # aqui o max ira busca na lista de numero o maior valor 
print("\no meno numero da lista:",min(lista)) # aqui o min ira busca na listao menor valor 
print("\na media",sum(lista)/len(lista))  # --> SUM ele retorna os valores numericos da entrada que deu e ele ignora o NULL
                       #---> LEN retonara a quantidade de elementos de qualquer lista retornara a quandidade de elementos contido na lista
    