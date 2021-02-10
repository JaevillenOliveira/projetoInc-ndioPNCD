# -- coding: utf-8 --
"""
Created on Wed Aug 26 15:33:32 2020

@author: Adlla Katarine e Daniel Alves
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import six
import math



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
        st = '             ' + df['Ano Medicao'][0] + ' |' + df['Ano Medicao'][12]+ ' |' + df['Ano Medicao'][24] + ' |' + df['Ano Medicao'][36] +' |'+ df['Ano Medicao'][48] + '\n'
        frases.append(st)         
        
        
        #meses
        for i in range(0, 12):
            st = str(df['Data Medicao'][i]) + '    ||    ' + str(round(df[colunas[j]][i], 3)) +'|'+ str(round(df[colunas[j]][i+12], 3))+ '|'+ str(round(df[colunas[j]][i+24], 3)) +'|'+ str(round(df[colunas[j]][i+36], 3)) +'|'+ str(round(df[colunas[j]][i+48], 3)) + '\n'
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



#separar estações do ano na tabela da estação
def estacoes_estacoes(cidade, df, atributo, ano, anos):
    #separando os meses para estação "VERÃO"
    aux1 = cidade.loc[0, atributo]
    aux2 = cidade.loc[1, atributo]
    aux3 = cidade.loc[2, atributo]
    
    df.loc['VERAO', atributo] += round((aux1+aux2+aux3)/3, 4)
    if ano == 2019:
        df.loc['VERAO', atributo] = df.loc['VERAO', atributo]/len(anos)
        
    #separando os meses para estação "OUTONO"
    aux1 = cidade.loc[3, atributo]
    aux2 = cidade.loc[4, atributo]
    aux3 = cidade.loc[5, atributo]
    
    
    if(math.isnan(aux1)):
        df.loc['OUTONO', atributo] += round((aux2+aux3)/3, 4)
        #print('aqui')
    else:
        df.loc['OUTONO', atributo] += round((aux1+aux2+aux3)/3, 4)
    if ano == 2019:
        df.loc['OUTONO', atributo] = df.loc['OUTONO', atributo]/len(anos)

    #separando os meses para estação "INVERNO"
    aux1 = cidade.loc[6, atributo]
    aux2 = cidade.loc[7, atributo]
    aux3 = cidade.loc[8, atributo]
    
    if(math.isnan(aux2)):
        df.loc['INVERNO', atributo] += round((aux1+aux3)/3, 4)
        #print('aqui')
    else:
        df.loc['INVERNO', atributo] += round((aux1+aux2+aux3)/3, 4)
    if ano == 2019:
        df.loc['INVERNO', atributo] = df.loc['INVERNO', atributo]/len(anos)
    
    #separando os meses para estação "PRIMAVERA"
    aux1 = cidade.loc[9, atributo]
    aux2 = cidade.loc[10, atributo]
    aux3 = cidade.loc[11, atributo]
    
    if(math.isnan(aux2)):
        df.loc['PRIMAVERA', atributo] += round((aux1+aux3)/3, 4)
        #print('aqui')
    else:
        df.loc['PRIMAVERA', atributo] += round((aux1+aux2+aux3)/3, 4)

    if ano == 2019:
        df.loc['PRIMAVERA', atributo] = df.loc['PRIMAVERA', atributo]/len(anos)

#separar estações do ano na tabela de ocorrências
def estacoes_ocorrencia(ocorrencias, df, ano, anos):
    #separando os meses para estação "VERÃO"
    aux1 = ocorrencias[0]
    aux2 = ocorrencias[1]
    aux3 = ocorrencias[2]

    
    df.loc['VERAO', 'OCORRENCIAS'] += round((aux1+aux2+aux3), 4)
    '''if ano == 2019:
        df.loc['VERAO', 'OCORRENCIAS'] = df.loc['VERAO', 'OCORRENCIAS']/len(anos)'''
    
    #separando os meses para estação "OUTONO"
    aux1 = ocorrencias[3]
    aux2 = ocorrencias[4]
    aux3 = ocorrencias[5]

    df.loc['OUTONO', 'OCORRENCIAS'] += round((aux1+aux2+aux3), 4)
    #print(df.loc['OUTONO', 'OCORRENCIAS'])
    '''if ano == 2019:
        df.loc['OUTONO', 'OCORRENCIAS'] = df.loc['OUTONO', 'OCORRENCIAS']/len(anos)'''
    
    #separando os meses para estação "INVERNO"
    aux1 = ocorrencias[6]
    aux2 = ocorrencias[7]
    aux3 = ocorrencias[8]
    
    df.loc['INVERNO', 'OCORRENCIAS'] += round((aux1+aux2+aux3), 4)
    '''if ano == 2019:
        df.loc['INVERNO', 'OCORRENCIAS'] = df.loc['INVERNO', 'OCORRENCIAS']/len(anos)'''
    
    #separando os meses para estação "PRIMAVERA"
    aux1 = ocorrencias[9]
    aux2 = ocorrencias[10]
    aux3 = ocorrencias[11]
    
    df.loc['PRIMAVERA', 'OCORRENCIAS'] += round((aux1+aux2+aux3), 4)
    '''if ano == 2019:
        df.loc['PRIMAVERA', 'OCORRENCIAS'] = df.loc['PRIMAVERA', 'OCORRENCIAS']/len(anos)'''



#tabela relacionando com as estações do ano
def plot_estacoes(cidade, ocorrencias):
    cidade = cidade.reset_index(drop=True) #resetando o index da cidade que recebe a cada ano
    ocorrencias = ocorrencias.reset_index(drop=True) #resetando o index das ocorrencias que recebe a cada ano
    
    columns = ['PRECIPITACAO TOTAL; MENSAL(mm)', 'OCORRENCIAS']
    rows = ['VERAO', 'OUTONO', 'INVERNO', 'PRIMAVERA']
    
    #criação do dataframe
    df = pd.DataFrame(index=rows, columns=columns) 
    
    percorrer = ['PRECIPITACAO TOTAL; MENSAL(mm)']
    
    for atributo in percorrer:
        estacoes_estacoes(cidade, df, atributo)
     
        estacoes_ocorrencia(ocorrencias, df)
    
        df.reset_index(level=0, inplace=True)

        #renomeando colunas
        df.rename(columns={'PRECIPITACAO TOTAL; MENSAL(mm)': 'PRECIPITACAO'}, inplace = True)

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



''' Cria dataFrame de um atributo e suas ocorrencias por estação e adiciona os seus valores. '''
def atributoEstacao(atributo, df_lencois, df_piata, df_itirucu, ocorrencias, anos):
    #splitAtributo = atributo.split(';')
    columns = [atributo, 'OCORRENCIAS']
    rows = ['VERAO', 'OUTONO', 'INVERNO', 'PRIMAVERA']
        
    #criação do dataframe
    dfLencois = pd.DataFrame(index=rows, columns=columns)
    dfLencois.fillna(0,inplace=True)
    dfPiata = pd.DataFrame(index=rows, columns=columns)
    dfPiata.fillna(0,inplace=True)
    dfItirucu = pd.DataFrame(index=rows, columns=columns)
    dfItirucu.fillna(0,inplace=True)
    
    
    for ano in anos:
        ocorrenciaEstacoes(df_lencois.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)], atributo, dfLencois, ano, anos)
        if(atributo != 'INSOLACAO TOTAL; MENSAL(h)'):
            ocorrenciaEstacoes(df_piata.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)], atributo, dfPiata, ano, anos)
            ocorrenciaEstacoes(df_itirucu.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)], atributo, dfItirucu, ano, anos)
    dfLencois.reset_index(level=0, inplace=True)
    if(atributo != 'INSOLACAO TOTAL; MENSAL(h)'):
        dfPiata.reset_index(level=0, inplace=True)
        dfItirucu.reset_index(level=0, inplace=True)
    
    plotOcorrenciaEstacoes(dfLencois, dfPiata, dfItirucu, rows, atributo, 'Estacao')



''' Add os valores das estações e ocorrências no dataFrame de estações atraves de duas outras funções. '''
def ocorrenciaEstacoes(cidade, ocorrencias, atributo, df, ano, anos):
    cidade = cidade.reset_index(drop=True) #resetando o index da cidade que recebe a cada ano
    ocorrencias = ocorrencias.reset_index(drop=True) #resetando o index das ocorrencias que recebe a cada ano
    
    estacoes_estacoes(cidade, df, atributo, ano, anos)
    estacoes_ocorrencia(ocorrencias, df, ano, anos)
    
    
    
''' Cria dataFrame de um atributo e suas ocorrencias por mes e adiciona os seus valores. '''
def atributoAno(atributo, df_lencois, df_piata, df_itirucu, ocorrencias, anos):
    columns = [atributo, 'OCORRENCIAS']
    rows = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    dfLencois = pd.DataFrame(index=rows, columns=columns)
    dfLencois.fillna(0,inplace=True)
    dfPiata = pd.DataFrame(index=rows, columns=columns)
    dfPiata.fillna(0,inplace=True)
    dfItirucu = pd.DataFrame(index=rows, columns=columns)
    dfItirucu.fillna(0,inplace=True)
    
    ocorrenciaMeses(ocorrencias[str('Ocorrências')], atributo, df_lencois, dfLencois, rows, anos)
    if(atributo != 'INSOLACAO TOTAL; MENSAL(h)'):
        ocorrenciaMeses(ocorrencias[str('Ocorrências')], atributo, df_piata, dfPiata, rows, anos)
        ocorrenciaMeses(ocorrencias[str('Ocorrências')], atributo, df_itirucu, dfItirucu, rows, anos)
    
    dfLencois.reset_index(level=0, inplace=True)
    if(atributo != 'INSOLACAO TOTAL; MENSAL(h)'):
        dfPiata.reset_index(level=0, inplace=True)
        dfItirucu.reset_index(level=0, inplace=True)
    plotOcorrenciaEstacoes(dfLencois, dfPiata, dfItirucu, rows, atributo, 'Mes')



''' Add os valores dos meses e ocorrências no dataFrame de mes. '''
def ocorrenciaMeses(ocorrencias, atributo, df, dfOcorrencias, rows, anos):
    for i in range(12):
        df_mes = df[df[df.columns[0]].str.contains(rows[i])]
        
        dfOcorrencias.loc[rows[i], atributo] = df_mes[atributo].mean()
        dfOcorrencias.loc[rows[i], 'OCORRENCIAS'] = ocorrencias[i]
    

''' Cria o gráfico de Ocorrências x Mês/Estação. '''
def plotOcorrenciaEstacoes(df, df2, df3, rows, atributo, aux):
    splitAtributo = atributo.split(';')
    splitAtributo = splitAtributo[0]
    auxAtributo = atributo.split('MENSAL')
    auxAtributo = auxAtributo[1]
    
    
    fig, ax1 = plt.subplots()
    # primeiro defino a sequência (numérica) do eixo x 
    # (lembrando xticks não recebem strings)4
    auxL = []
    if len(rows) == 12:
        auxL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    else:
        auxL = [0, 1, 2, 3]
    ax1.set_xticks(auxL)
    # Agora coloco os nomes dos estados como estiquetas
    ax1.set_xticklabels(df.index.tolist())
    # Duplico e vinculo o novo axe `ax2` ao orginal `ax1`
    ax2 = ax1.twinx()
    # Plotar
   
    ax1.bar(rows, df['OCORRENCIAS'], color='#37777D', label = 'Ocorrências')
    ax1.set_ylabel("OCORRENCIAS")
    ax2.plot(rows, df[atributo], color='r', marker='^', linestyle='-', linewidth=2, label = splitAtributo.capitalize() + auxAtributo + ' - Lençóis')
    if(atributo != 'INSOLACAO TOTAL; MENSAL(h)'):
        ax2.plot(rows, df2[atributo], color='g', marker='s', linestyle='-', linewidth=2, label = splitAtributo.capitalize() + auxAtributo + ' - Piatã')
        ax2.plot(rows, df3[atributo], color='m', marker='o', linestyle='-', linewidth=2, label = splitAtributo.capitalize() + auxAtributo + ' - Itiruçu')
    #ax1.legend(loc=0)
    ax2.set_ylabel(str(splitAtributo  + auxAtributo))
    
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc="upper right")
    #ax2.legend(loc=0)
    #plt.title('Ocorrências x ' + str(splitAtributo) + ' 2015 - 2019')
    #plt.legend(loc="upper left")
    plt.savefig(splitAtributo + '_' + aux + '.png')

    # Plotando o Gráfico
    plt.figure();
'''

lns1 = ax.plot(time, Swdown, '-', label = 'Swdown')
lns2 = ax.plot(time, Rn, '-', label = 'Rn')
ax2 = ax.twinx()
lns3 = ax2.plot(time, temp, '-r', label = 'temp')

# added these three lines
lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)

lns = ax1 + ax2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)

'''


def main():
    '''
    #dataframe das cidades
    #df_Estacao_Morro = pd.read_csv('.\\convencionais\\dados_83184_M_2015-01-01_2020-07-31.csv')
    df_Estacao_Lencois = pd.read_csv('.\\estacoes\\convencionais\\dados_83242_M_2015-01-01_2020-07-31.csv')
    
    #meses(df_Estacao_Morro)
    meses(df_Estacao_Lencois)
    
    
    #criação tabela e do csv
    #plot_dados(df_Estacao_Morro, 'Morro')
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
    #df_morro =  pd.read_csv('.\\estacoes\\dados_Morro.csv')
    df_lencois =  pd.read_csv('.\\estacoes\\dados_Lencois.csv')
    df_lencois = df_lencois.rename(columns={'TEMPERATURA MEDIA COMPENSADA; MENSAL(°C)': 'TEMPERATURA MEDIA; MENSAL(°C)'})
    
    df_piata =  pd.read_csv('.\\estacoes\\dados_Piata.csv')
    df_piata = df_piata.rename(columns={'Mes': 'Data Medicao'})
    df_piata = df_piata.rename(columns={'Ano': 'Ano Medicao'})
    df_piata = df_piata.rename(columns={'PRECIPITACAO TOTAL; DIARIO (AUT)(mm)': 'PRECIPITACAO TOTAL; MENSAL(mm)'})
    df_piata = df_piata.rename(columns={'TEMPERATURA MEDIA; DIARIA (AUT)(Â°C)': 'TEMPERATURA MEDIA; MENSAL(°C)'})
    df_piata = df_piata.rename(columns={'UMIDADE RELATIVA DO AR; MEDIA DIARIA (AUT)(%)': 'UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)'})
    
    df_piata = df_piata[['Data Medicao','PRECIPITACAO TOTAL; MENSAL(mm)','TEMPERATURA MEDIA; MENSAL(°C)','UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)','Ano Medicao']]

    df_itirucu =  pd.read_csv('.\\estacoes\\dados_Itirucu.csv')
    df_itirucu = df_itirucu.rename(columns={'Mes': 'Data Medicao'})
    df_itirucu = df_itirucu.rename(columns={'Ano': 'Ano Medicao'})
    df_itirucu = df_itirucu.rename(columns={'PRECIPITACAO TOTAL; DIARIO (AUT)(mm)': 'PRECIPITACAO TOTAL; MENSAL(mm)'})
    df_itirucu = df_itirucu.rename(columns={'TEMPERATURA MEDIA; DIARIA (AUT)(Â°C)': 'TEMPERATURA MEDIA; MENSAL(°C)'})
    df_itirucu = df_itirucu.rename(columns={'UMIDADE RELATIVA DO AR; MEDIA DIARIA (AUT)(%)': 'UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)'})
    
    df_itirucu = df_itirucu[['Data Medicao','PRECIPITACAO TOTAL; MENSAL(mm)','TEMPERATURA MEDIA; MENSAL(°C)','UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)','Ano Medicao']]
    
    
    #dataframe das ocorrências
    ocorrencias = pd.read_csv('.\\Gráficos_Tabelas\\ocorrencias_por_mes_ano.csv')
    
    
    anos = [2015, 2016, 2017, 2018, 2019]
    
    
    '''
    #criação de tabelas por mês
    
    for ano in anos:
        plot_table(df_morro.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)])
        plot_table(df_lencois.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)])
    ''' 

    #criação de tabelas por estações do ano       
    '''for ano in anos:
        #plot_estacoes(df_morro.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)])
        #plot_estacoes(df_lencois.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)])
        exemplo(df_morro.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)], ano)
        exemplo(df_lencois.query("`Ano Medicao` == " + str(ano)), ocorrencias[' '+ str(ano)], ano)'''
    
    coluna = ['INSOLACAO TOTAL; MENSAL(h)', 'PRECIPITACAO TOTAL; MENSAL(mm)',
              'TEMPERATURA MEDIA; MENSAL(°C)', 'UMIDADE RELATIVA DO AR; MEDIA MENSAL(%)']
    
    for atributo in coluna:
        atributoEstacao(atributo, df_lencois, df_piata, df_itirucu, ocorrencias, anos)
        atributoAno(atributo, df_lencois, df_piata, df_itirucu, ocorrencias, anos)



if __name__ == '__main__': # chamada da funcao principal
    main()