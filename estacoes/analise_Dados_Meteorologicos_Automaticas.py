# -- coding: utf-8 --
"""
Created on Mon Sep 14 19:26:56 2020

@author: Adlla Katarine e Daniel Alves
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
  
        df_Estacao = pd.read_csv('dados_A407_D_2015-01-01_2019-12-31.csv')
        
        #criando colunas
        df_Estacao['Ano'] = 'NaN'
        df_Estacao['Mes'] = 'NaN'
        
        #separando mês e ano 
        for i in range(0, len(df_Estacao)):
            df_Estacao['Ano'][i] = df_Estacao['Data Medicao'][i].split('-')[0]
            df_Estacao['Mes'][i] = df_Estacao['Data Medicao'][i].split('-')[1]
        
        #excluindo datas
        df_Estacao = df_Estacao.drop(columns=['Data Medicao'])
        
        meses(df_Estacao)
        
        df_Estacao = separarMeses(df_Estacao)
        
        #df_Estacao.to_csv('dados_Itirucu.csv', index = False)

        #tratarDados(df_Estacao)
        #colunas = df_Estacao.columns.tolist()
        #colunas.remove(df_Estacao.columns[0])
        #colunas.remove('Latitude')
        #colunas.remove('Longitude')
        
        #for i in range(len(colunas)):
            #plot_map(df_Estacao, colunas[i])
        
        
''' Média dos dias do mês '''
def separarMeses(df):
    dt = pd.DataFrame(columns=['Ano', 'Mes', 'PRECIPITACAO TOTAL; DIARIO (AUT)(mm)', 'TEMPERATURA MEDIA; DIARIA (AUT)(Â°C)', 'UMIDADE RELATIVA DO AR; MEDIA DIARIA (AUT)(%)'])

    for i in [2015, 2016, 2017, 2018, 2019]:        
        for j in ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']:
            dftemp = df.loc[(df['Ano'] == str(i)) & (df['Mes'] == j)]
            dftemp.reset_index(level=0, inplace=True)
            dftemp = dftemp.drop(columns=['index'])
            
            dftemp['ptemp ' + str(i)] = dftemp['PRECIPITACAO TOTAL; DIARIO (AUT)(mm)'].mean(skipna = True)
            dftemp['ttemp ' + str(i)] = dftemp['TEMPERATURA MEDIA; DIARIA (AUT)(Â°C)'].mean(skipna = True)
            dftemp['utemp ' + str(i)] = dftemp['UMIDADE RELATIVA DO AR; MEDIA DIARIA (AUT)(%)'].mean(skipna = True)
            data = [i, j, dftemp['ptemp ' + str(i)][0], dftemp['ttemp ' + str(i)][0], dftemp['utemp ' + str(i)][0]]
            dtemp = pd.DataFrame([data], columns=['Ano', 'Mes', 'PRECIPITACAO TOTAL; DIARIO (AUT)(mm)', 'TEMPERATURA MEDIA; DIARIA (AUT)(Â°C)', 'UMIDADE RELATIVA DO AR; MEDIA DIARIA (AUT)(%)'])
            dt = dt.append(dtemp, ignore_index=True)
            
    return dt

''' Transformando meses para ficar mais legível . '''
def meses(df_Estacao):
    for i in range(len(df_Estacao)):

        if df_Estacao['Mes'][i] == '01':
            df_Estacao['Mes'][i] = 'JAN'
        elif df_Estacao['Mes'][i] == '02':
            df_Estacao['Mes'][i] = 'FEV'
        elif df_Estacao['Mes'][i] == '03':
            df_Estacao['Mes'][i] = 'MAR'
        elif df_Estacao['Mes'][i] == '04':
            df_Estacao['Mes'][i] = 'ABR'
        elif df_Estacao['Mes'][i] == '05':
            df_Estacao['Mes'][i] = 'MAI'
        elif df_Estacao['Mes'][i] == '06':
            df_Estacao['Mes'][i] = 'JUN'
        elif df_Estacao['Mes'][i] == '07':
            df_Estacao['Mes'][i] = 'JUL'
        elif df_Estacao['Mes'][i] == '08':
            df_Estacao['Mes'][i] = 'AGO'
        elif df_Estacao['Mes'][i] == '09':
            df_Estacao['Mes'][i] = 'SET'
        elif df_Estacao['Mes'][i] == '10':
            df_Estacao['Mes'][i] = 'OUT'
        elif df_Estacao['Mes'][i] == '11':
            df_Estacao['Mes'][i] = 'NOV'
        elif df_Estacao['Mes'][i] == '12':
            df_Estacao['Mes'][i] = 'DEZ'
        
        
''' Trata os dados com valores inconsistentes para NaN. '''
def tratarDados(df_Estacao):
    df_Estacao = df_Estacao.replace(-9999.0, np.nan)


#criando gráficos
def plot_map(df_Estacao, atributo, ano):
    mesGeral = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    mesJUL = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL']
    
    media = []
    mes = []
    if(ano < 2020):
        mes = mesGeral
    else:
        mes = mesJUL

    for i in mes:
        df_mes = df_Estacao[df_Estacao[df_Estacao.columns[0]].str.contains(i)]  
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