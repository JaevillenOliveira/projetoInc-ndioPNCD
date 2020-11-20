
# Esse script é para plotar os histogramas dos diasemchuva, precipitação e riscofogo por ano.
# O histograma serve para analisarmos a distribuição dos dados. 

import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt

# Este método recebe um dataframe com os dados e plota seu histograma
# Os parâmetros ano e name são para identificar as imagens geradas
def plt_hist(df, ano, name):
	df.plot.hist()
	
	plt.xlabel(name)
	plt.title(name + 'por ano')
	plt.savefig(name+'_'+str(ano)+'.png')

# Este método separa a coluna de diasemchuva dos demais dados e passa para o método
# plt_hist(df, ano, name) para plotar o histograma
def diasemchuva_ano():
	for ano in range (2015, 2020):
		diasemchuva_df = pd.read_csv('Focos_'+str(ano)+'-01-01_'+str(ano)+'-12-31.csv', usecols=["diasemchuva"])
		plt_hist(diasemchuva_df, ano, 'Dias sem chuva')

	diasemchuva_df_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv', usecols=["diasemchuva"])
	plt_hist(diasemchuva_df_2020, 2020, 'Dias sem chuva')

# Este método separa a coluna de precipitacao dos demais dados e passa para o método
# plt_hist(df, ano, name) para plotar o histograma
def precipitacao_ano():
	for ano in range (2015, 2020):
		precipitacao_df = pd.read_csv('Focos_'+str(ano)+'-01-01_'+str(ano)+'-12-31.csv', usecols=["precipitacao"])
		plt_hist(precipitacao_df, ano, 'Precipitação')

	precipitacao_df_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv', usecols=["precipitacao"])
	plt_hist(precipitacao_df_2020, 2020, 'Precipitação')


# Este método separa a coluna de riscofogo dos demais dados e passa para o método
# plt_hist(df, ano, name) para plotar o histograma
def riscofogo_ano():
	for ano in range (2015, 2020):
		riscofogo_df = pd.read_csv('Focos_'+str(ano)+'-01-01_'+str(ano)+'-12-31.csv', usecols=["riscofogo"])
		plt_hist(riscofogo_df, ano, 'Risco de fogo')

	riscofogo_df_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv', usecols=["riscofogo"])
	plt_hist(riscofogo_df_2020, 2020, 'Risco de fogo')


precipitacao_ano()
diasemchuva_ano()
riscofogo_ano()


