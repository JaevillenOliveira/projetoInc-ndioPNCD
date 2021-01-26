# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:05:40 2020

@author: Adlla Katarine e Daniel Alves
"""


import os as aqv
import pandas as pd

#df = pd.read_csv('INMET_NE_BA_A425_LENCOIS_01-01-2020_A_31-07-2020.CSV')

listArchives = aqv.listdir('.//automaticas')
#print(listArchives)

for archive in listArchives:

############################################ CONVERTER ARQUIVOS .TXT EM .CSV ############################################
    with open('.//automaticas//' + archive, 'r') as archiveTXT:
        print(archive)
        linhas = archiveTXT.readlines() #cada linha é um elemento da lista linhas
        linha0 = linhas[0]
        linha1 = linhas[1]
        linha2 = linhas[2]
        linha3 = linhas[3]
        
        linha4 = linhas[4]
        linha5 = linhas[5]
        
        linha6 = linhas[6]
        linha7 = linhas[7]
        linha8 = linhas[8]
        linha10 = linhas[10]
        linhas.remove(linha0)
        linhas.remove(linha1)
        linhas.remove(linha2)
        linhas.remove(linha3)
        linhas.remove(linha4)
        linhas.remove(linha5)
        linhas.remove(linha6)
        linhas.remove(linha7)
        linhas.remove(linha8)
        linhas.remove(linha10)
        
    for i in range(0, len(linhas)):
        linhas[i] = linhas[i].replace(',', '.')
    
    for i in range(0, len(linhas)):
        linhas[i] = linhas[i].replace(';', ',')
    
    #formantando a linha de atributos
    linha10 = linha10.replace(',', '.')
    linha10 = linha10.replace(';', ',')
    linha10 = linha10.replace('.', ';')
    
    #salvando o arquivo com atributos e dados já formatados
    with open(archive, 'w') as arquivo:
        arquivo.writelines(linha10)
        
        arquivo.writelines(linhas)
    
    df = pd.read_csv(archive, encoding= 'unicode_escape')
    #df = df.drop(columns=['0'])
    df['Latitude'] = float(linha2.strip('Latitude: '))
    df['Longitude'] = float(linha3.strip('Longitude: '))
    
    df = df.drop(columns=['Unnamed: 4'])
    df.to_csv(archive, index = False)