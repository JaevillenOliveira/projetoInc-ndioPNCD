# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:18:05 2020

@author: Adlla Katarine e Daniel Alves
"""

import os as aqv
import pandas as pd

listArchives = aqv.listdir('.\\estacoes\\convencionais')

for archive in listArchives:
    
############################################ CONVERTER ARQUIVOS .TXT EM .CSV ############################################
    with open('.\\estacoes\\convencionais\\' + archive, 'r') as archiveTXT:
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
        linha9 = linhas[9]
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
        linhas.remove(linha9)
        linhas.remove(linha10)
    
    #substituindo virgulas dos números float
    for i in range(0, len(linhas)):
        linhas[i] = linhas[i].replace(',', '.')
    
    #substituindo os ';' para ',' possibilitando utilização no pandas
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
    
    #salvando a latitude e longitude como novos atributos no dataset
    df = pd.read_csv(archive)
    df['Latitude'] = linha2.strip('Latitude (graus) : ')
    df['Longitude'] = linha3.strip('Longitude (graus) : ')
    df.to_csv(archive, index = False)
    
