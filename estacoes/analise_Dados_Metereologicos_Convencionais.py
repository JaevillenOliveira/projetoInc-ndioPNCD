# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:33:32 2020

@author: Daniel Alves
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import six



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
    df_ano = df_ano.drop(columns=['DIRECAO PREDOMINANTE DO VENTO; MENSAL(° (gr))', 
                                  'EVAPORACAO DO PICHE; MENSAL(mm)',
                                  'EVAPOTRANSPIRACAO POTENCIAL; BH MENSAL(mm)', 'EVAPOTRANSPIRACAO REAL; BH MENSAL(mm)',
                                  'PRESSAO ATMOSFERICA AO NIVEL DO MAR; MEDIA MENSAL(mB)', 'PRESSAO ATMOSFERICA; MEDIA MENSAL(mB)',
                                  'VENTO; VELOCIDADE MAXIMA MENSAL(m/s)',
                                  'VENTO; VELOCIDADE MEDIA MENSAL(m/s)', 'VISIBILIDADE; MEDIA MENSAL(codigo)',
                                  'Unnamed: 18', 'Latitude', 'Longitude'])
    #transformando em um dicionário
    df = df_ano.to_dict()  
    
    #transformando em um dataframe
    df = pd.DataFrame.from_dict(df)
    
    anos = df["Ano Medicao"].str.contains('2020')
    
    for i in range(0, len(anos)):
        if anos[i]:
            df = df.drop(i)
            
    
    #criando csv das informações
    df.to_csv("dados_"+str(cidade)+".csv", index=False)
    
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
        st = '             ' + df['Ano Medicao'][0] + ' |' + df['Ano Medicao'][12] + ' |'+ df['Ano Medicao'][36] +' |'+ df['Ano Medicao'][49] + '\n'
        frases.append(st)         
        
        
        #meses
        for i in range(0, 11):
            st = str(df['Data Medicao'][i]) + '    ||    ' + str(round(df[colunas[j]][i], 3)) +'|'+ str(round(df[colunas[j]][i+12], 3)) +'|'+ str(round(df[colunas[j]][i+36], 3)) +'|'+ str(round(df[colunas[j]][i+49], 3)) + '\n'
            frases.append(st)

                
    arquivo.writelines(frases)



#criando tabela para comparações de atributos
def plot_table(cidade, ocorrencias):
    cidade = cidade.reset_index(drop=True) #resetando o index da cidade que recebe a cada ano
    #colunas do dataframe
    columns = ('INSOLACAO TOTAL; MENSAL(h)', 'PRECIPITACAO TOTAL; MENSAL(mm)', 
               'TEMPERATURA MAXIMA MEDIA; MENSAL(°C)', 'TEMPERATURA MEDIA COMPENSADA; MENSAL(°C)',
               'TEMPERATURA MINIMA MEDIA; MENSAL(°C)', 'UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)', 'OCORRÊNCIAS')
    #linhas do dataframe
    rows = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'TOTAL']
    
    #criação do dataframe
    df = pd.DataFrame(index=rows, columns=columns) 
    
    #atributos
    percorrer = ['INSOLACAO TOTAL; MENSAL(h)', 'PRECIPITACAO TOTAL; MENSAL(mm)', 
                 'TEMPERATURA MAXIMA MEDIA; MENSAL(°C)', 'TEMPERATURA MEDIA COMPENSADA; MENSAL(°C)', 
                 'TEMPERATURA MINIMA MEDIA; MENSAL(°C)', 'UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)']
    
    #adicionando linha de total
    cidade.loc[len(cidade)+1, :] = np.nan
    
    #adicionando valores dos atributos
    for atributo in percorrer:
        total=0
        df[atributo] = cidade[atributo].values
        for i in range(0, len(cidade[atributo].values) - 1):
                total += cidade[atributo].values[i]
                
        df.loc['TOTAL', atributo] = total
                
    df['OCORRÊNCIAS'] = ocorrencias.values

    df.reset_index(level=0, inplace=True)

    #normalizando valores
    for atributo in percorrer:
        for i in range(0, len(df[atributo].values)):
            df.loc[i, atributo] = round(df.loc[i, atributo], 4)
    
    #renomeando colunas
    df.rename(columns={'INSOLACAO TOTAL; MENSAL(h)': 'INSOLACAO', 'PRECIPITACAO TOTAL; MENSAL(mm)': 'PRECIPITACAO',
                       'TEMPERATURA MAXIMA MEDIA; MENSAL(°C)': 'TEMPERATURA MAX', 'TEMPERATURA MEDIA COMPENSADA; MENSAL(°C)': 'TEMPERATURA MED',
                       'TEMPERATURA MINIMA MEDIA; MENSAL(°C)': 'TEMPERATURA MIN', 'UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)': 'UMIDADE AR'}, inplace = True)

    render_mpl_table(df)
    
    
    
#transformando tabela em imagem. Retirado de "https://www.semicolonworld.com/question/58193/how-to-save-the-pandas-dataframe-series-data-as-a-figure"
def render_mpl_table(data, col_width=10, row_height=0.625, font_size=11,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

    render_mpl_table(data, header_columns=0, col_width=2.0)   
    


def main():
    '''
    #dataframe das cidades
    df_Estacao_Morro = pd.read_csv('.\\convencionais\\dados_83184_M_2015-01-01_2020-07-31.csv')
    df_Estacao_Lencois = pd.read_csv('.\\convencionais\\dados_83242_M_2015-01-01_2020-07-31.csv')
    
    meses(df_Estacao_Morro)
    meses(df_Estacao_Lencois)
    
    
    #criação tabela e do csv
    plot_dados(df_Estacao_Morro, 'Morro')
    plot_dados(df_Estacao_Lencois, 'Lencois')
    

    #armazenando nomes das colunas
    colunas = df_Estacao_Morro.columns.values
    
    criação de gráficos
    for i in range(1, 18):
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2015")], colunas[i], '2015')        
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2016")], colunas[i], '2016')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2017")], colunas[i], '2017')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2018")], colunas[i], '2018')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2019")], colunas[i], '2019')
        plot_map(df_Estacao_Morro[df_Estacao_Morro['Data Medicao'].str.contains("2020")], colunas[i], '2020')
    '''
    
    #dataframe das informações
    df_morro =  pd.read_csv('.\\estacoes\\dados_Morro.csv')
    df_lencois =  pd.read_csv('.\\estacoes\\dados_Lencois.csv')

    #dataframe das ocorrências
    ocorrencias = pd.read_csv('.\\Gráficos_Tabelas\\ocorrencias_por_mes_ano.csv')
    
    anos = [2015, 2016, 2017, 2018, 2019]
    for ano in anos:
        #plot_table(df_morro.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)])
        plot_table(df_lencois.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)])
        
    
    
    

    
if __name__ == '__main__': # chamada da funcao principal
    main() 
