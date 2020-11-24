import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt
import numpy as np

def plt_all_attr(dic_focos, dic_dsc,dic_prc,dic_rf, ano):
	plt.cla() 
	x = np.arange(len(dic_focos))  # the label locations
	width = 0.4  # the width of the bars

	fig, ax = plt.subplots()
	#focos = ax.bar(x - width/4, dic_focos.values(), width, color='#37777D', align='center')
	dsc = ax.bar(x - 1 - width/2, dic_dsc.values(), width, color='purple',label='Dias sem chuva')
	prc = ax.bar(x + width/2, dic_prc.values(), width, color='orange', label='Precipitacao')
	prc = ax.bar(x + 1 + width/2, dic_rf.values(), width, color='red', label='Risco de fogo')

	ax.set_xticks(x)
	ax.set_xticklabels(dic_focos.keys(), rotation=15)
	ax.legend()

	ax.set_ylabel('Mediana de dias sem chuva')
	ax.set_title('Dias sem chuva por municipio por ano')
	plt.savefig('all_attr_'+str(ano)+'.png')

def relate_all_attr():
	municipios = ['ANDARAI', 'BONINAL', 'IBICOARA', 'IRAMAIA', 'IRAQUARA', 
					'ITAETE', 'LENCOIS', 'MUCUGE', 'NOVA REDENCAO', 'PALMEIRAS']
	for ano in range (2015, 2020):
		dic_focos = {}
		dic_dsc = {}
		dic_prc = {}
		dic_rf = {}

		focos = pd.read_csv('Focos_'+str(ano)+'-01-01_'+str(ano)+'-12-31.csv')
		for mun in municipios:
			data_mun = focos[focos['municipio']==mun]
			if not data_mun.empty:
				dic_focos[mun] = len(data_mun.index)
				dic_dsc[mun+'dsc'] = stats.median(data_mun['diasemchuva'])
				dic_prc[mun+'prc'] = stats.median(data_mun['precipitacao'])
				dic_rf[mun+'rf'] = stats.median(data_mun['riscofogo'])
			else:
				dic_focos[mun] = 0
				dic_dsc[mun+'dsc'] = 0
				dic_prc[mun+'prc'] = 0
				dic_rf[mun+'rf'] = 0

		plt_all_attr(dic_focos, dic_dsc,dic_prc,dic_rf, ano)

	dic_dsc = {}
	focos_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv')
	for mun in municipios:
		data_mun = focos_2020[focos_2020['municipio']==mun]
		if not data_mun.empty:
			dic_focos[mun] = len(data_mun.index)
			dic_dsc[mun+'dsc'] = stats.median(data_mun['diasemchuva'])
			dic_prc[mun+'prc'] = stats.median(data_mun['precipitacao'])
			dic_rf[mun+'rf'] = stats.median(data_mun['riscofogo'])
		else:
			dic_focos[mun] = 0
			dic_dsc[mun+'dsc'] = 0
			dic_prc[mun+'prc'] = 0
			dic_rf[mun+'rf'] = 0
	plt_all_attr(dic_focos, dic_dsc,dic_prc,dic_rf, 2020)


def plt_fires_all_years(dic_anos):
	plt.cla() 
	firstkey = list(dic_anos.keys())[0]
	x = np.arange(len(dic_anos.get(firstkey)))  # the label locations
	width = 0.4  # the width of the bars

	fig, ax = plt.subplots()
	for i in range (len(dic_anos)):
		keyname = list(dic_anos.keys())[i]
		dic = (dic_anos.get(keyname)).values()
		ax.bar(i, dic, width, label=keyname)

	ax.set_xticks(x)
	ax.set_xticklabels((dic_anos.get(firstkey)).keys(), rotation=15)
	ax.legend()

	ax.set_ylabel('Mediana de dias sem chuva')
	ax.set_title('Dias sem chuva por municipio por ano')
	plt.savefig('all_attr_.png')


def fires_all_years():
	municipios = ['ANDARAI', 'BONINAL', 'IBICOARA', 'IRAMAIA', 'IRAQUARA', 
					'ITAETE', 'LENCOIS', 'MUCUGE', 'NOVA REDENCAO', 'PALMEIRAS']
	dic_anos = {}
	for ano in range (2015, 2020):
		dic_focos = {}
		focos = pd.read_csv('Focos_'+str(ano)+'-01-01_'+str(ano)+'-12-31.csv')
		for mun in municipios:
			data_mun = focos[focos['municipio']==mun]
			if not data_mun.empty:
				dic_focos[mun] = len(data_mun.index)
			else:
				dic_focos[mun] = 0
		dic_anos[str(ano)] = dic_focos

	focos_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv')
	dic_focos = {}
	for mun in municipios:
		data_mun = focos_2020[focos_2020['municipio']==mun]
		if not data_mun.empty:
			dic_focos[mun] = len(data_mun.index)
		else:
			dic_focos[mun] = 0
	dic_anos[str(2020)] = dic_focos

	plt_fires_all_years(dic_anos)

fires_all_years()