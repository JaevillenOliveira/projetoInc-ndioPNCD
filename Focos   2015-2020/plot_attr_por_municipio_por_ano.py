#
# Este script é para plotar os valores dos atributos por município por ano
#
import pandas as pd
import statistics as stats
from collections import Counter
import matplotlib.pyplot as plt

# Plota a quantidade de focos por município por ano
def plt_focos(focos_municipios, year):
	focos_municipios = focos_municipios.sort_values()
	freqs = Counter (focos_municipios)

	xvals = range(len(freqs.values()))
	plt.cla() 
	
	plt.bar(xvals, freqs.values() , color='#37777D')
	plt.xticks(xvals, freqs.keys(), rotation=15)
	plt.ylabel('Número de Focos por year')
	plt.title('Focos por municipio por year')
	plt.savefig('Focos_por_municipio_'+str(year)+'.png')

# Conta a quantidade de linhas, ou seja, a quantidade de focos por 
# município por ano e passa a informação para o método plt_focos(focos_municipios, ano)
def focos_municipio_ano():
	for year in range (2015, 2020):
		focos_municipios = pd.read_csv('Focos_'+str(year)+'-01-01_'+str(year)+'-12-31.csv')
		plt_focos(focos_municipios["municipio"], year)

	focos_municipios_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv')
	plt_focos(focos_municipios_2020["municipio"],2020)

# Plota os gráficos de um determinado atributo por município por ano
def plt_attr_ano_municipio(dic_attr, year, attr_name):
	plt.cla() 

	plt.bar(range(len(dic_attr)), dic_attr.values() , color='#37777D')
	plt.xticks(range(len(dic_attr)), dic_attr.keys(), rotation=15)
	plt.ylabel('Mediana '+ attr_name)
	plt.title(attr_name+' por ano')
	plt.savefig(attr_name+'_por_municipio_'+str(year)+'.png')

# Separa a coluna de um determinado atributo do restante dos dados, calcula 
# sua mediana (estatística escolhida baseada na distribuição dos dados observada a partir
# de seus histogramas) e passa para o método plt_attr_ano_municipio(dic_attr, year, attr_name)
# que irá plotar a informação
def attr_ano_municipio(attr_name):
	municipios = ['ANDARAI', 'BONINAL', 'IBICOARA', 'IRAMAIA', 'IRAQUARA', 
					'ITAETE', 'LENCOIS', 'MUCUGE', 'NOVA REDENCAO', 'PALMEIRAS']
	for year in range (2015, 2020):
		dic_attr = {}
		focos = pd.read_csv('Focos_'+str(year)+'-01-01_'+str(year)+'-12-31.csv', usecols=[attr_name, 'municipio'])
		for mun in municipios:
			data_mun = focos[focos['municipio']==mun]
			if not data_mun.empty:
				dic_attr[mun] = stats.median(data_mun[attr_name])
		plt_attr_ano_municipio(dic_attr, year, attr_name)

	dic_attr = {}
	focos_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv',usecols=[attr_name, 'municipio'])
	for mun in municipios:
		data_mun = focos_2020[focos_2020['municipio']==mun]
		if not data_mun.empty:
			dic_attr[mun] = stats.median(data_mun[attr_name])
	plt_attr_ano_municipio(dic_attr, 2020, attr_name)

## Aqui são chamados os métodos para plotar todas a informações separadas individualmente
## por munícipio por ano
focos_municipio_ano()
attr_ano_municipio('diasemchuva')
attr_ano_municipio('precipitacao')
attr_ano_municipio('riscofogo')


