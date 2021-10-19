# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:15:38 2020

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
        print(self.nome +" tem "+str(self.idade) +" anos de idade ")
        
    def getdescricao(self):
        descricao = " o nome do meu cachorro e " + self.nome + " ele tem " + str(self.idade) + " anos de idade "
        return descricao
         
#--> aqui tambem ele recebeu o nome e idade no printe captura meu cachorro captura nome idade e depois getdescrissao todas as informacoes contidas no get descricao
meucachorro = cachorro(" pitoco " ,2 )
print(meucachorro.getdescricao())


#--> aqui ele puxa informacao do getdescricao e logo esse cachorro recebe o nome de spyke pode perceber na linha 32 seu cachorro receber nome 
#--> print sao todas as respostas que estao na descricao porem com nome diferente agora 
seucachorro = cachorro(" spyke " ,3 )
descricao = seucachorro.getdescricao()
print(descricao)