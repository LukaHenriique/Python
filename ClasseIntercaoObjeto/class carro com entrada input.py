# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:35:46 2020

@author: Lucas
"""

class Carro():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        

        
#--> get significa que tera um retorno
    def getdescricao(self):
     descricao = " meu carro e uma " + str(self.marca) + " o modelo e " + self.modelo + " do ano " + str(self.ano) + " da cor " + self.cor          
     return descricao
 
marca = input("didgite a marca do carro:") 
modelo =input("didgite o modelo do carro:") 
ano = int(input("didgite o ano do carro:"))
cor = input("didgite a cor do carro:") 
  
meuCarro = Carro(marca, modelo, ano, cor) # crio uma variavel meuCarro que armazena os atributos que eu dei no carro e quardo numa funcao  ( )
print(meuCarro.getdescricao())