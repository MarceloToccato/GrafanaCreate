# O código a seguir tem a utilidade de criar um arquivo .json, com intuito de importalo para o grafana
# Fazendo o grafana criar um dashboard já pronto

# Usar template no zabbix 'Qlik Sense - Central Node'

###########################################Criando as variaveis para Do host e do grupo dohost######################################



Hostgroup = ''  # Altere para o grupo de host que seu host se encontra'
Hostname = '' # Altere para o nome do seu Host 



#################################################Criador do Id aleatório###########################################################




# O código a baixo serve para  criar um ID unico para o uid q é definido como f'{code}' no código



import random as rm #Importando a biblioteca random
code = [] #Criando uma array onde a O ID unico ficara



# Todos os caracteres que podem ser utilizados no ID unico
Caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



for i in range (7): #Loop para adicionar os caracteres aleatorios na array code
         
         
            simbolos = rm.choice(Caracteres) #Escolhendo caracter
         
            code.append(simbolos) #Adiciona o caracter na array code


code = (''.join(code)) #Define que code é um texto tudo junto sem espaço entre os itens
#Fazendo com que ele forme um ID unico



#################################################Importando o .json###########################################################



# Essa variável 'grafanajson' é um .json que caso importado cria um dashboard no grafana
# Porém nos lugares onde se coloca o Hostgroup e o Hostname colocamos os seguintes comandos 
# f'{Hostgroup}' e f'{hostname} para importar as variávels já definidas

# caso queira importa seu proprio .json faça os seguintes passos
# altere todos os True,False,None e para true,false,null
# altere o nome do group host e o host para f'{Hostgroup}' e f'{Hostname}
# altere a uid para f'{code}'

grafanajson = None



###############################################Criando arquivo .json e abrindo a pasta json#####################################



# Os códigos seguinte tem o intuito de:
# Salvar a variavel grafanajson em um arquivo .json 
# Abrir o explorador de arquivos onde o tal arquivo se encontra 

import os #   Importa uma biblioteca para conseguir mexer no sistema operacional via python
import json # Importa uma biblioteca para conseguir mexer com json

folder_path = 'json' #Define a pasta onde o arquivo será salvo

file_name = f'{Hostname}'+'.json' #Define o nome que o arquivo terá, juntando o nome do host com o .json


file_path = os.path.join(folder_path, file_name) #cria o caminho onde o arquivo será salvo


with open (file_path,'w') as grafana: #abre um arquivo onde a variavel a cima definiu
  #escreve o conteudo da variável 'grafanajson'
  json.dump(grafanajson, grafana)

  #Caso o arquivo não esteja nesse direcionamente altere para onde a pasta com o código se encontra 
diretorio = 'C:\\Users\\User\\Desktop\\projetos\\GrafanaCreate\\json' #defina o diretório onde o json foi salvo  

os.startfile(diretorio) 
#abre o explorador de arquivos onde o json está. 
#para apenas ter que arrastar o arquivo para a aba de importar do grafana



############################################################################################################