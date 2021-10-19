# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:32:52 2020

@author: Lucas
"""

print("\n--------------------------------------------------------------------")

# LEN BUSCA NUMERO DE LETRAS EM UMA VARIAVEL DO TIPO NOME 
# toda vez que tiver coxetes isso que dizer que todos os elementos que tiver la dentro ira envirar uma lista 
def MesagemVisitante(nome = "visitante"):
    
    # nome e a variavel que buscara nome na funcao lembrando que ele esta na posicao 0/ len(nome)vai definir a quantidades de caractere que tera o nome lembrando que ele esta na pocisao 1
   return [nome,len(nome)] # --> essa funcao imprimira o nome dentro de uma lista entre coxetes que dizer que transformou em uma rei e o LEN buscara o nome na funcao e ao encontrar vai no argumentos e o LEN finaliza a quantidades de caracteres que tem seu nome na da pessoa 
   

print(MesagemVisitante('Lucas')[:]) # --> ja aqui dentro desses coxetes eu decido se quero quem a imprenssao de quantidades emprimir na sua pocissao 


print("\n--------------------------------------------------------------------")


def MesagemVisitante(nome = "visitante"):
    
    return [nome,len(nome)]

nome = input("digite seu nome:")

print(MesagemVisitante(nome)[:]) 

print("\n--------------------------------------------------------------------")
lista = [1,2,3,4,5,6,7]
print(lista[0]) # --> imprimira somente o elemento que estiver na pocisaao zero
print(lista) # --> imprimi a lista toda 

print("\n--------------------------------------------------------------------")

lista = [1,2,3,4,5,6,7]
print(lista[:2]) #--> aqui eu defino que ele ira imprimir da pocisao zero ate a posissao 2
print(lista)