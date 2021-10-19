# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:00:17 2020

@author: Lucas
"""

#--> CLASS NADA MAIS E QUE UMA CLASE DO CACHORRO ONDE VAMOS DADR PARAMETROS AO CACHORRO PARAMETROS SERIA OQUE O CACHORRO FAZ VOU DAR ATRIBUTOS A ELE 
#--> CACHORRO SENTA LATI NOME DO CACHORRO ESSES SAO OS PARAMERTOS QUE VOU DAR AO CACHORRO
class Cachorro():
    
#--> def seria que e de clase, no def criar uma classe especial que ela execulta automaticamente quando uma classe e "insanciada" = guloso faminto querer mais.
#--> essa clase chama init e depois vem om self o self e uma estancia do init e depois disso vamos passar parametros para ela  diferentes parametros 
  

    def descricao(self):
        print("descrissao cachorro ")
        
#--> aqui seria os atributos do cachorro que eu estou dando a ele para ele fazer ou oque ele ira a fazer 
    def sentar(self):
       print("cachorro sentou ")
#--> aqui seria os atributos do cachorro que eu estou dando a ele para ele fazer ou oque ele ira a fazer 
 
    def latir(self):
        print("cachorro latiu ")
dog = Cachorro()
#--> aqui no caso seria as acoes que o cachorro ira fazer 
dog.sentar()
dog.latir()