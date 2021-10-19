# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:26:50 2020

@author: Lucas
"""

class cachorro():
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =idade
     
    def sentou (self):
        print(self.nome +" sentou")
            
    def latu(self):
        print(self.nome +" latiu")
        
    def anos(self):
        print(self.nome +" tem "+self.idade+" anos de idade ")
        
    def getdescricao(self):
        descricao = " o nome do meu cachorro e " + self.nome + " ele tem " + self.idade + " anos de idade "
        return descricao
         
nome = input("digite o nome do cachorro:\t")
idade = input("digite o idade do cachorro:\t")

meucachorro = cachorro(nome , idade)
print(meucachorro.getdescricao())





