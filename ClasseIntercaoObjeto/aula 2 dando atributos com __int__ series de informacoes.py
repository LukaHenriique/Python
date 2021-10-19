# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:16:05 2020

@author: Lucas
"""

class Cachorro():
#--> esse metodo seria o metodo de inicializacao contrutor ele ira construair o objeto de uma forma
#--> self e a estancia que ele ira receber
#--> aqui passo as informacoes 
    def __init__(self, nome, idade):
     
#-->self e estancia que ira receber o nome do cachorro idade e isso a gente iguala = o nome do cachorro 
#--> que no casso estou criando um classe de atributos que o cachorro ira fazer, nesse caso ele ira receber nome 
#--> self.nome e um atributo que a clase vai ter e == nome que dizer que ele recebera nome   
     
     self.nome = nome
     self.idade = idade
#-->  =nome idade todos que esticer aqui so vale ate aqui quando passa  da qui ela ja nao vale mais para o resto do codigo ela some 


#--> eleestasentado e a class cachorro() o __init__self criou uma serie de atributos infomacoes que ao eu criar self.nome aqui ou em outro lugar o self ira busca 
#--> esse atributo que eu dei a ele seja nome idade e logo a frente no print coloco oque o cachorro ira fazer  entre aspas " " mas com a chamada self.nome + "e o que ele ira fazez" 


##-------------temos aqui todas as acoes do cachorro---------------------##
    def sentar(self):
        print(self.nome +" esta sentado")
        
    def latiu(self):
        print(self.nome +" ele latiu")
        
    def anos(self):
        print(self.nome +" tem "+ str(self.idade) + " anos de idade")
        
print("------------------------------------------------------------------------")
print("acima do codigo e apenas um bolo represrntado como class cachorro\ndepois dessa class darei a ele suas funcoes oque ele ira fazer atraves de parametros e informacoes dada a ele\n")
print("------------------------------------------------------------------------")
print("abaixo e os nomes que eu darei para cada tido de coisa do bolo ele pode\n ter muitas caracteriscas esse polo e eu posso dar o nome diferente para cada\n caracteristica do bolo nome idade etc")
print("------------------------------------------------------------------------")

# --> essa seria a estancia do cachorro  acoes objeto, dog receber todas as clases do cachorro que eu dei para ele, o def faz tudo isso a classe fucionar que foi os parametros que eu dei ao cachorro
#--> cachorro ea estancia e dog recebe a estancia de cachorro
#--> aqui posso criar dog dog1 dog2 dog3 dog4 todos eles vai receber as acoes do cachorro 
#--> aqui seria definicao do cachorro
print("\n\n\ntemos aqui todas as caracteristicas de diversos cachorros oque cada cachorro tem dinheiro casa se e casado etc")
dog = Cachorro("toto ",3)
dog.sentar()
dog.latiu()
dog.anos()
print("\no meu cachorro chama "+dog.nome+" ele tem "+str(dog.idade)+" anos de idade")

#--> lembrando que aqui posso criar varias objetod do que o cachorro vai fazer com uma unica clase de cachorro tipo aqui posso criar cachorro 1 2 3 4 5 e assim por diante posso dar nomes diferentes ao meu cachorro  idade
 
meucachorro =Cachorro("spyque",2)
meucachorro.sentar()
meucachorro.latiu()
meucachorro.anos()

cachorrorose = Cachorro("pitoco",5)
cachorrorose.sentar()
cachorrorose.latiu()
cachorrorose.anos()

