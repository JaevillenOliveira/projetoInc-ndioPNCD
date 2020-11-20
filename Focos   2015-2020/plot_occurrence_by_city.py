import pandas as pd


focosAno = [
    "Focos_2015-01-01_2015-12-31.csv", "Focos_2016-01-01_2016-12-31.csv",
    "Focos_2017-01-01_2017-12-31.csv", "Focos_2018-01-01_2018-12-31.csv",
    "Focos_2019-01-01_2019-12-31.csv",
]

data = {}

for foco in focosAno:
    df = pd.read_csv(foco)
    for index, row in df.iterrows():
        city = row['municipio']
        if city in data:
            data[city] += 1
        else: data[city] = 1
        
        
qtd = data.values()
cities = data.keys()

df = pd.DataFrame(qtd, index=cities)

#df.to_csv("../Gráficos_Tabelas/ocorrencias_total_por_cidade.csv")

#### plot data

import matplotlib.pyplot as plt

x_units = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y_units = qtd

newlist = []
for i in cities:
    newlist.append(i)

tick_label = newlist

plt.barh(x_units, y_units, tick_label=tick_label)

plt.xlabel('Ocorrências')
plt.ylabel('Cidades')
plt.title('Ocorrências por Cidade 2015 - 2019')

for i, v in enumerate(qtd):
    plt.text(v + 5, i + 0.9, str(v), color='red')

plt.show()