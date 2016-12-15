#coding: utf-8
import networkx as nx #Biblioteca para se trabalhar com grafos
import numpy as np #Trabalhar com vetores 
import matplotlib.pyplot as plt 
import pylab as p 
import random #Biblioteca para gerar numeros aleatorios
import collections #biblioteca utilizada para ordenar um dicionario 


G = nx.read_gml('C:/Users/Claudio/Desktop/trabalhografo/dolphins.gml') #Importando o grafo 



passos=100 #Definindo o numero de passos a ser dado (Prof passou este valor)
i=0 #contador para fazer o for 
grafoV=G.nodes() #Atribuo a variavel grafoV todos os vertices
visitas={x:0 for x in G.nodes()} #Atribuindo a todos estes vertices o valor 0 para serem o dicionario de visitas 
inicio=(random.choice(grafoV)) #Professor deixou decidirmos qual seria o inicio, porem preferi definir aleatoriamente. 

#vizinhos=(G.neighbors(inicio))#Função devolve os vizinhos do grafo inicial / fiz apenas para teste 

#contador=0 #Contador para saber se foram feitas todas as iterações,  


for i in range(passos): #laçõ de repetição que varree de i=0 até o tamanho dos passos, função range faz o i ser um vetor de 0 a 100 posições 

	visitas[inicio]+=1 #Incremento o vertice inicial com uma visita,
	vizinhos=(G.neighbors(inicio)) #Verifico os vizinhos deste vertice
	inicio=(random.choice(vizinhos)) #inicio recebe um destes vizinhos, e repete o laço 
	
print("----------------------------------------")
print(" ")
print('Numero de visitas de cada vertice') 
print(" ")
print(collections.OrderedDict(sorted(visitas.items())))
print(" ")


visitas.update((x, y /(passos)*100) for x, y in visitas.items()) #utilizo a função .update novamente no dicionario visitas, onde tenho o vertice o numero de vezes que passamos por ele
																 #X é o vertice e Y o numero de visitas, novamente faço a conta iterando o valor Y/passos e multiplico por 100 para 
																 #encontrar a % que estas visitas equivalem na caminhada de bebado, como são 100 passos fica similar a nao * 100. 


print("----------------------------------------")
print(" ")
print('Porcentagem equivalente a quantidade de visitas')
print(" ")
print(collections.OrderedDict(sorted(visitas.items()))) #mostra dicionario ja calculado com a % de cada vistias 
print(" ")

print("----------------------------------------")
print(" ")
print('Soma da porcentagem de todas as visitas')
print(" ")
print(sum(visitas.values())) #soma todos os valores para conferir se chegam a 100 % 
print(" ")

print("----------------------------------------")
print(" ")
print('Maior numero de visitas')
print(" ")
print(max(visitas, key=visitas.get))#Retira do dicionario o maior valor 


#Plotagem do grafico 


y_axis =visitas.values()#define valores para Y do grafico, os valores de cada vertice
x_axis = range(len(y_axis))#tamanho do eixo X , range dos valores 
width_n=0.5 # tamanho das barras
bar_color='red'#cor das barras 

legenda=visitas.keys() # legenda de cada barra, sua correspondente chave 

ax=plt.axes() #ax para eixos, facilitar programçaão 

grafico = plt.bar(x_axis,y_axis, width=width_n,color=bar_color) #define o grafico(eixox,eixoy,tamanho,cor)


ax.set_xticks(x_axis)#define que para cada barra havera uma legenda, define o espaçamento delas. 

ax.set_xticklabels(legenda,rotation='vertical') #atribui a legenda os nomes dos vertices rotacionando para vertical 

plt.xlabel('Vertices') #label x = vertice 
plt.ylabel('Numero de visitas') # label y = valores 
plt.title('Relacao de vertice de um grafo e seu numero de visitas no andar de bebado') #titulo 

plt.grid(True) #coloque grid = sim 

plt.show() #mostre o grafico. 