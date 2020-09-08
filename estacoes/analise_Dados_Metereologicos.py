# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:33:32 2020

@author: Daniel Alves
"""

import pandas as pd
import matplotlib.pyplot



#def main():
#dataframe das cidades
df_Estacao_Morro = pd.read_csv('.\\estacoes\\convencionais\\dados_83184_M_2015-01-01_2020-07-31.csv')
df_Estacao_Lencois = pd.read_csv('.\\estacoes\\convencionais\\dados_83242_M_2015-01-01_2020-07-31.csv')

matplotlib.pyplot.plot(df_Estacao_Morro['Data Medicao'], 
                       df_Estacao_Morro['INSOLACAO TOTAL; MENSAL(h)'])

matplotlib.pyplot.show()


matplotlib.pyplot.plot(df_Estacao_Morro['Data Medicao'], 
                       df_Estacao_Morro['PRECIPITACAO TOTAL; MENSAL(mm)'])

matplotlib.pyplot.show()


matplotlib.pyplot.plot(df_Estacao_Morro['Data Medicao'], 
                       df_Estacao_Morro['TEMPERATURA MAXIMA MEDIA; MENSAL(°C)'])

matplotlib.pyplot.show()
#main()