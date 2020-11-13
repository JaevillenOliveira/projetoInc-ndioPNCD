import matplotlib.pyplot as plt 
import pandas as pd
import os

NULO = ''

fig = plt.figure(dpi=200)
ax = fig.add_subplot()

months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro", "Total"]

cols = ["{: }".format(i) for i in range(2015, 2020)]
cols.append('Ocorrências')
cols.append("F.R % (Aprox)")


auxMonth = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
]

table_data = []
total = [0, 0, 0, 0, 0, 0]

for month in range(12):
    
    line = []
    for year in range(2015, 2020):
        fileName = 'dataset/Focos_' + str(year) + '_' + auxMonth[month] + '.csv'
        if os.path.exists(fileName):
            df = pd.read_csv(fileName)
            line.append(len(df))
            total[year - 2015] += len(df);
        else:
            line.append(NULO)
            
    soma = 0;
    for i in line:
        if i != NULO:
            soma += i
            
    total[5] += soma
    line.append(soma)
            
    table_data.append(line)
    
   
table_data.append(total)


for i in range(len(table_data)):
    porcento = (table_data[i][5] * 100)/table_data[12][5]
    table_data[i].append(round(porcento,2))
    
    

print(table_data)

table = ax.table(cellText=table_data, loc='center', rowLabels=months, colLabels=cols)

table.set_fontsize(14)

table.scale(1,2)

ax.axis('off')

plt.show()

df = pd.DataFrame(table_data, columns=cols, index=months)
df.to_csv("tabela.csv")
