# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:10:42 2020

@author: Lucas
"""

mult3 = []      # para o programa enteder que e numero devo colocar um numero na variavel --> mult3 =[]

inicial=int(input("entre com um numero"))
final=int(input("entre com um numero"))

for i in range(inicial,final): # esses sao todos os numero  dentro () digitados que a dentro dor for sao armazenaddos o i coletara todos 
     if i%3==0:            # aqui ira passa multiplo de 3 e imprimira somente os multiplos dentro da lista ----> []
        mult3.append(i)  # o (i) dentro da funcao isso que dizer que o append ira pefar todos os numero que dentro do for 
                         # appende adiciona a lista inteira tanto sendo numero ou nome que esteja dentro de uma lista ----> nome =[]
        
print(mult3)        #  imprimira a lista --->[ ] normal de ordem cresente 
print(mult3[::-1]) # esses cochetes representa que imprimira de forma reversa por causa do menos --->  -1
        
      