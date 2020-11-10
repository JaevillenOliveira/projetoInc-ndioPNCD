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
            db.loc[i ,'Data Medicao'] = 'JAN'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '02':
            db.loc[i ,'Data Medicao'] = 'FEV'            
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '03':
            db.loc[i ,'Data Medicao'] = 'MAR' 
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '04':
            db.loc[i ,'Data Medicao'] = 'ABR'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '05':
            db.loc[i ,'Data Medicao'] = 'MAI'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '06':
            db.loc[i ,'Data Medicao'] = 'JUN'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '07':
            db.loc[i ,'Data Medicao'] = 'JUL'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '08':
            db.loc[i ,'Data Medicao'] = 'AGO'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '09':
            db.loc[i ,'Data Medicao'] = 'SET'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '10':
            db.loc[i ,'Data Medicao'] = 'OUT'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '11':
            db.loc[i ,'Data Medicao'] = 'NOV'
            db.loc[i ,'Ano Medicao'] = ver[0]   
        elif ver[1] == '12':
            db.loc[i ,'Data Medicao'] = 'DEZ'
            db.loc[i ,'Ano Medicao'] = ver[0]   



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



#separando dados para criação da tabela
def plot_dados(df_ano, cidade):
    #removendo dados desnecessários
    df_ano = df_ano.drop(columns=['DIRECAO PREDOMINANTE DO VENTO; MENSAL(° (gr))', 'EVAPORACAO DO PICHE; MENSAL(mm)',
                                  'EVAPOTRANSPIRACAO POTENCIAL; BH MENSAL(mm)', 'EVAPOTRANSPIRACAO REAL; BH MENSAL(mm)',
                                  'NUMERO DE DIAS COM PRECIP; PLUV; MENSAL(número)', 'PRECIPITACAO TOTAL; MENSAL(mm)',
                                  'PRESSAO ATMOSFERICA AO NIVEL DO MAR; MEDIA MENSAL(mB)', 'PRESSAO ATMOSFERICA; MEDIA MENSAL(mB)',
                                  'VENTO; VELOCIDADE MAXIMA MENSAL(m/s)',
                                  'VENTO; VELOCIDADE MEDIA MENSAL(m/s)', 'VISIBILIDADE; MEDIA MENSAL(codigo)',
                                  'Unnamed: 18', 'Latitude', 'Longitude'])
    #transformando em um dicionário
    df = df_ano.to_dict()  
    
    #transformando em um dataframe
    df = pd.DataFrame.from_dict(df)
    
    #chamando função para criação do arquivo
    plot_arquivo(df, cidade)  
    
    
    
#criando arquivo com os dados para tabela
def plot_arquivo(df, cidade):
    #abertura do arquivo
    arquivo = open("dados_"+cidade+".txt", "a")
    frases = [] #lista para salvar as linhas
    colunas = df.columns.values #colunas da tabela
    
    #atributos
    for j in range(1, len(colunas)-1): 
        st = '\n' + ' Mês   ||  ' + str(colunas[j]) + '\n'
        frases.append(st)
        frases.append('------------------------------------------------------\n')
        st = '             ' + df['Ano Medicao'][0] + ' |' + df['Ano Medicao'][12] + ' |'+ df['Ano Medicao'][36] +' |'+ df['Ano Medicao'][49] +' |'+ df['Ano Medicao'][60] + '\n'
        frases.append(st)         
        
        p=6 #variável para o ano de 2020, dados até julho
        
        #meses
        for i in range(0, 11):
            st = str(df['Data Medicao'][i]) + '    ||    ' + str(round(df[colunas[j]][i], 3)) +'|'+ str(round(df[colunas[j]][i+12], 3)) +'|'+ str(round(df[colunas[j]][i+36], 3)) +'|'+ str(round(df[colunas[j]][i+49], 3)) +'|'+ str(round(df[colunas[j]][66-p], 3)) + '\n'
            frases.append(st)
            
            p = p - 1 
            if p==0:
                p=1  
                
    arquivo.writelines(frases)

 
 
def main():
    #dataframe das cidades
    df_Estacao_Morro = pd.read_csv('.\\convencionais\\dados_83184_M_2015-01-01_2020-07-31.csv')
    df_Estacao_Lencois = pd.read_csv('.\\convencionais\\dados_83242_M_2015-01-01_2020-07-31.csv')
    
    meses(df_Estacao_Morro)
    meses(df_Estacao_Lencois)
    
    #armazenando nomes das colunas
    colunas = df_Estacao_Morro.columns.values
    
    #criação tabela
    plot_dados(df_Estacao_Morro, 'Morro')
    plot_dados(df_Estacao_Lencois, 'Lencois')
    
    
    '''
    criação de gráficos
    for i in range(1, 18):
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2015")], colunas[i], '2015')        
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2016")], colunas[i], '2016')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2017")], colunas[i], '2017')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2018")], colunas[i], '2018')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2019")], colunas[i], '2019')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2020")], colunas[i], '2020')
    '''

if __name__ == '__main__': # chamada da funcao principal
    main() 
