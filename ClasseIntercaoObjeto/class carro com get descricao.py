# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:19:58 2020

@author: Lucas
"""

class Carro():
    def __init__(self, marca, modelo, ano, cor ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
#--> get significa que tera um retorno
    def getdescricao(self):
     descricao = " meu carro e uma " +self.marca + " o modelo e " + self.modelo + " do ano " + str(self.ano) + " da cor " + self.cor         
     return descricao
  
carro = Carro("BMW", "X1", 2020, "BRANCO")
descricao = carro.getdescricao()
print(carro.getdescricao())
