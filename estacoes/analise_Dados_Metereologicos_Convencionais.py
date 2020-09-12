# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:33:32 2020

@author: Daniel Alves
"""

import pandas as pd
import matplotlib.pyplot as plt


#transformando meses para ficar mais legível 
def meses(db):
    for i in range(len(db)):
        ver = db.loc[i ,'Data Medicao'].split('-')

        if ver[1] == '01':
            db.loc[i ,'Data Medicao'] = 'JAN ' + ver[0]   
        elif ver[1] == '02':
            db.loc[i ,'Data Medicao'] = 'FEV ' + ver[0] 
        elif ver[1] == '03':
            db.loc[i ,'Data Medicao'] = 'MAR ' + ver[0] 
        elif ver[1] == '04':
            db.loc[i ,'Data Medicao'] = 'ABR ' + ver[0] 
        elif ver[1] == '05':
            db.loc[i ,'Data Medicao'] = 'MAI ' + ver[0] 
        elif ver[1] == '06':
            db.loc[i ,'Data Medicao'] = 'JUN ' + ver[0] 
        elif ver[1] == '07':
            db.loc[i ,'Data Medicao'] = 'JUL ' + ver[0] 
        elif ver[1] == '08':
            db.loc[i ,'Data Medicao'] = 'AGO ' + ver[0] 
        elif ver[1] == '09':
            db.loc[i ,'Data Medicao'] = 'SET ' + ver[0] 
        elif ver[1] == '10':
            db.loc[i ,'Data Medicao'] = 'OUT ' + ver[0] 
        elif ver[1] == '11':
            db.loc[i ,'Data Medicao'] = 'NOV ' + ver[0] 
        elif ver[1] == '12':
            db.loc[i ,'Data Medicao'] = 'DEZ ' + ver[0] 


#criando gráficos
def plot_map(df_ano, atributo, ano):
    df_ano = df_ano.reset_index()
    for i in range(len(df_ano)):    
        data = df_ano.loc[i, 'Data Medicao']
        data = data.split()
        df_ano.loc[i, 'Data Medicao'] =  str(data[0])
        
    plt.bar(df_ano['Data Medicao'], df_ano[atributo], color='#37777D')
    
    
    plt.xticks(df_ano['Data Medicao'])
    plt.ylabel(atributo)
    plt.title(atributo + ' por mês do ano '+ ano)
    
    plt.savefig(atributo+ str(ano) +'.png')
    
    plt.close()


def main():
    #dataframe das cidades
    df_Estacao_Morro = pd.read_csv('.\\convencionais\\dados_83184_M_2015-01-01_2020-07-31.csv')
    df_Estacao_Lencois = pd.read_csv('.\\convencionais\\dados_83242_M_2015-01-01_2020-07-31.csv')
    
    meses(df_Estacao_Morro)
    meses(df_Estacao_Lencois)
    
    #armazenando nomes das colunas
    colunas = df_Estacao_Morro.columns.values
    
    for i in range(1, 18):
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2015")], colunas[i], '2015')        
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2016")], colunas[i], '2016')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2017")], colunas[i], '2017')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2018")], colunas[i], '2018')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2019")], colunas[i], '2019')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2020")], colunas[i], '2020')

if __name__ == '__main__': # chamada da funcao principal
    main() 
