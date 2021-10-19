# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:55:50 2020

@author: Lucas
"""

def somar(*valores): 
    
    reservador=0
    for i in valores: # --> ele ira pecoore todas a variavel valor qua esta dentro dos argumentos 
        reservador =+ i
        
        
    return reservador

resposta = somar(6,5,3,4)
print(resposta)