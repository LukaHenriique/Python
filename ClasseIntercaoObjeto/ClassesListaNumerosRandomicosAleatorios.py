# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:23:36 2020

@author: Lucas
"""
lista =[]
novalista =[]
class cauculos():
    
    def __init__(self, lista):
        self.lista = lista

        for i in range(3):
            lista.append(input("digite numeros aleatorios:"))
     
    def atualizarlista(self, novalista):
        self.novalista = novalista
        
    
    def soma(self):
        print("soma da lista " + sum(self.lista) + len(self.novalista))
 
    def menor(self):
       print(" menor lista 1 " + min(self.lista1) + " menor nova lista " + min(self.novalista))
    
    
    def media(self):
        if len(self.lista)==0 or len(self.novalista)==0:
           print("a media das lista e de:" + sum(self.lista1) / len(self.novalista))
           
    def getlistaaleatoria(self):
        listaaleatoria = " minha lista aleatoria " + str(self.lista[:])  +  " quantidade de numeros " + str(len(self.lista)) + " o inicio da lista e " + str(min(self.lista)) + " fim da minha lista " + str(max(self.lista))  
        return listaaleatoria


minhalista = cauculos(lista)
listaaleatoria = minhalista.getlistaaleatoria()
print(listaaleatoria)
        
                          