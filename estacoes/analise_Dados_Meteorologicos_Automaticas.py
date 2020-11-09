# -- coding: utf-8 --
"""
Created on Mon Sep 14 19:26:56 2020

@author: Adlla Katarine
"""

import pandas as pd
import matplotlib.pyplot as plt
import os as aqv
import numpy as np


def main():
    lista_arquivos = aqv.listdir('.\\automaticas')
    ano = 2015
    for arquivo in lista_arquivos:
        
        df_Estacao_Lencois = pd.read_csv('.\\automaticas\\' + arquivo)
        meses(df_Estacao_Lencois, ano)
        tratarDados(df_Estacao_Lencois)
        colunas = df_Estacao_Lencois.columns.tolist()
        colunas.remove(df_Estacao_Lencois.columns[0])
        colunas.remove(df_Estacao_Lencois.columns[1])
        colunas.remove('Latitude')
        colunas.remove('Longitude')
        
        for i in range(len(colunas)):
            plot_map(df_Estacao_Lencois, colunas[i], ano)
        
        ano = ano + 1


''' Transformando meses para ficar mais legível . '''
def meses(df_Estacao_Lencois, ano):
    for i in range(len(df_Estacao_Lencois)):
        ver = None
        if(ano < 2019):
            ver = df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]].split('-')
        else:
            ver = df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]].split('/')

        if ver[1] == '01':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'JAN'
        elif ver[1] == '02':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'FEV'
        elif ver[1] == '03':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'MAR'
        elif ver[1] == '04':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'ABR'
        elif ver[1] == '05':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'MAI'
        elif ver[1] == '06':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'JUN'
        elif ver[1] == '07':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'JUL'
        elif ver[1] == '08':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'AGO'
        elif ver[1] == '09':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'SET'
        elif ver[1] == '10':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'OUT'
        elif ver[1] == '11':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'NOV'
        elif ver[1] == '12':
            df_Estacao_Lencois.loc[i ,df_Estacao_Lencois.columns[0]] = 'DEZ'
        
''' Trata os dados com valores inconsistentes para NaN. '''
def tratarDados(df_Estacao_Lencois):
    df_Estacao_Lencois = df_Estacao_Lencois.replace(-9999.0, np.nan)


#criando gráficos
def plot_map(df_Estacao_Lencois, atributo, ano):
    mesGeral = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    mesJUL = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL']
    
    media = []
    mes = []
    if(ano < 2020):
        mes = mesGeral
    else:
        mes = mesJUL

    for i in mes:
        df_mes = df_Estacao_Lencois[df_Estacao_Lencois[df_Estacao_Lencois.columns[0]].str.contains(i)]  
        media.append(df_mes[atributo].median())
    
    plt.bar(mes, media, color='#37777D')
    
    plt.xticks(mes)
    plt.ylabel(atributo)
    plt.title(atributo + ' por mês do ano '+ str(ano))
    atributo = atributo.replace('/', '-')
    plt.savefig(atributo + str(ano) +'.png', format='png')
    
    plt.close()

if __name__ == '__main__': # chamada da funcao principal
    main()