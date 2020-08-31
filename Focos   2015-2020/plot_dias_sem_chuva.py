import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt

def plt_freq(focos_diasemchuva, ano):
	focos_diasemchuva.plot.hist()
	
	plt.ylabel('Dias sem chuva')
	plt.title('Dias sem chuva por ano')
	plt.savefig('Diasemchuva_'+str(ano)+'.png')

dic = {}

for ano in range (2015, 2020):
	focos_diasemchuva = pd.read_csv('Focos_'+str(ano)+'-01-01_'+str(ano)+'-12-31.csv', usecols=["diasemchuva"])
	dic[str(ano)] = stats.mode(focos_diasemchuva)
	plt_freq(focos_diasemchuva, ano)

focos_diasemchuva_2020 = pd.read_csv('Focos_2020-01-01_2020-08-13.csv')
dic[str(2020)] = stats.mode(focos_diasemchuva_2020)
plt_freq(focos_diasemchuva, 2020)




