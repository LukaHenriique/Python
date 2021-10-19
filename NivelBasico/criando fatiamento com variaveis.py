# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:16:54 2020

@author: Lucas
"""

listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [11,12,13,14,15,16,17,18,19,20]

meuSlice = slice(2,7) # -->  se usa a "notação de fatia" (slice notation) para delimitar um subconjunto de uma sequência, como uma lista ou uma string. os numeros entre (definira o inicio e ate onde ira os numero entre listaA e listaB)

print(listaA[meuSlice])
print(listaB[meuSlice])