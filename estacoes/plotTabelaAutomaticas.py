# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:44:49 2020

@author: adlla
"""
import pandas as pd
import os as aqv
import numpy as np


def main():
    #abertura do arquivo
    arquivoL = open("dados_Lençois_Automaticas.txt", "a")
    frases = [] #lista para salvar as linhas
    anosDados = ['2015', '2016', '2017', '2018', '2019', '2020']
        
        
    lista_arquivos = aqv.listdir('.\\automaticas')
    df_listaColunas = pd.read_csv('.\\automaticas\\' + lista_arquivos[0])
    listaColunas = df_listaColunas.columns.tolist()
    listaColunas.remove(df_listaColunas.columns[0])
    listaColunas.remove(df_listaColunas.columns[1])
    listaColunas.remove('Latitude')
    listaColunas.remove('Longitude')
    listaColunas.remove('Unnamed: 19')
    print(listaColunas)
    print(len(listaColunas))
    
    
    for i in range(len(listaColunas)):
        ano = 2015
        listaAno = []
        for arquivo in lista_arquivos:
                
            df_Estacao_Lencois = pd.read_csv('.\\automaticas\\' + arquivo)
            meses(df_Estacao_Lencois, ano)
            tratarDados(df_Estacao_Lencois)
            '''colunas = df_Estacao_Lencois.columns.tolist()
            colunas.remove(df_Estacao_Lencois.columns[0])
            colunas.remove(df_Estacao_Lencois.columns[1])
            colunas.remove('Latitude')
            colunas.remove('Longitude')'''
                
            listaAux = []
            listaAux = mediaAno(df_Estacao_Lencois, listaColunas[i], ano)
            listaAno.append(dictDadosAno(listaAux[0], listaAux[1]))
            #print(ano)
            ano = ano + 1
        #print('chegou aqui')
        #atributos
        st = '\n' + ' Mês   ||  ' + str(listaColunas[i]) + '\n'
        print(st)
        #print(listaColunas[i])
        frases.append(st)
        frases.append('------------------------------------------------------\n')
        print('------------------------------------------------------\n')
        st = '             ' + anosDados[0] + ' |' + anosDados[1] + ' |'+ anosDados[2] +' |'+ anosDados[3] +' |'+ anosDados[4] +' |'+ anosDados[5] +  '\n'
        frases.append(st)         
        print(st)        
        mesGeral = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        #print('st')
        #print(st)
        #meses
        for i in range(0, 12):
            st = mesGeral[i] + '    ||    '
            for media in listaAno:
                #print(media[mesGeral[i]])
                st = st + str(media[mesGeral[i]]) + '|'
            st = st + '\n'
            frases.append(st)
        print(st)
        print('')
    arquivoL.writelines(frases)


''' Trata os dados com valores inconsistentes para NaN. '''
def tratarDados(df_Estacao_Lencois):
    df_Estacao_Lencois = df_Estacao_Lencois.replace(-9999.0, np.nan)
    
    
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


def mediaAno(df_Estacao_Lencois, atributo, ano):
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
        '''print('VALOR:')
        print(df_mes[atributo].median())
        print(df_mes[atributo])'''
        media.append(df_mes[atributo].median())
        #print(media[i])
    listaMM = []
    listaMM.append(mes)
    listaMM.append(media)
    return listaMM


def dictDadosAno(ano, media):
    if(len(media) == 12):
        mediaAno = {'Ano': ano, 'JAN': media[0], 'FEV': media[1], 'MAR': media[2], 'ABR': media[3], 'MAI': media[4], 'JUN': media[5], 'JUL': media[6], 'AGO': media[7], 'SET': media[8], 'OUT': media[9], 'NOV': media[10], 'DEZ': media[11]}
    else:
        mediaAno = {'Ano': ano, 'JAN': media[0], 'FEV': media[1], 'MAR': media[2], 'ABR': media[3], 'MAI': media[4], 'JUN': media[5], 'JUL': media[6], 'AGO': None, 'SET': None, 'OUT': None, 'NOV': None, 'DEZ': None}
    return mediaAno 


if __name__ == '__main__': # chamada da funcao principal
    main()