import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join

#Pegando todos os arquivos de um diretório (percorrer arquivos em csv)
dirName = 'SplitMonth'
fileNames = [f for f in listdir(dirName) if isfile(join(dirName, f))]

"""Função genérica para percorrer e processar todos os arquivos csv.
:param func: Função que vai ser recebida por parametro para processar o arquivo
:param params: parametros da função
"""
def percorrerGenerico(func, params):
    for fileName in fileNames:
        params['fileName'] = fileName
        func(params)

"""Função para pegar o ano do arquivo
A fução percorre o nome do arquivo até achar o número 2 (anos de 2015 a 2020)
e pega ele e mais os 3 caracteres seguintes

#Requerido: params.fileName

:param params: parametros da função
:return: ano
"""
def getAnoArquivo(fileName):
    fileName 
    i = 0
    while i < len(fileName):
        if fileName[i] == '2':
            return fileName[i:i+4]
        i = i + 1;
        
"""Pegar o nome do arquivo em csv
Retira os4 ultimos caracteres do nome do arquivo (.csv)

:param fileName: Nome do arquivo
:return: Nome do arquivo sem .csv
"""
def getNomeArquivoCSV(fileName):
    return fileName[:(len(fileName) - 4)]

        
"""Função Que pega uma coluna do dataframe

#Requerido: params.fileName, params.col

:param params: parametros da função
:return: Dataframe com somente a coluna passada por parâmetro
"""
def filtroDeColunaDataFrame(params):
    fileName = params['fileName']
    col = params['col']
    return pd.read_csv((dirName + '/' + fileName), usecols=[col])

"""Função para gerar as plotagem

Requerido: params.fileName, params.col

:param params: parametros da função
:return: Dataframe com somente a coluna passada por parâmetro
"""
def plotHist(params):
    df = filtroDeColunaDataFrame(params)
    df.plot.hist()
    plt.ylabel(params['label'])
    fileName = getNomeArquivoCSV(params['fileName'])
    plt.title(params['label'] + ' ' + fileName)
    
    plt.savefig('Plots-'+ dirName + '/'+ params['col'] + '/' +'Plot-' + fileName +'.png')
    
"""Gerar histograma

Requerido: params.col

:param params: parametros da função
:return: Dataframe com somente a coluna passada por parâmetro
"""
def gerarHistograma(label, colName):
    params = {}
    params['col'] = colName
    params['label'] = label
    percorrerGenerico(plotHist, params)

gerarHistograma("Dias sem chuva", "diasemchuva")
gerarHistograma("Precipitação", "precipitacao")
gerarHistograma("Risco de fogo", "riscofogo")
