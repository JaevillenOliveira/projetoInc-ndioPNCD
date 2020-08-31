import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def plt_freq(focos_municipios, ano):
	focos_municipios = focos_municipios.sort_values()
	freqs = Counter (focos_municipios)

	xvals = range(len(freqs.values()))
	plt.cla() 
	
	plt.bar(xvals, freqs.values() , color='#37777D')
	plt.xticks(xvals, freqs.keys(), rotation=15)
	plt.ylabel('Número de Focos por ano')
	plt.title('Focos por municipio por ano')
	plt.savefig('Focos_por_municipio_'+str(ano)+'.png')

for ano in range (2015, 2020):
	focos_municipios = pd.read_csv('Focos_'+str(ano)+'-01-01_'+str(ano)+'-12-31.csv')
	plt_freq(focos_municipios["municipio"], ano)

focos_municipios_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv')
plt_freq(focos_municipios_2020["municipio"],2020)


