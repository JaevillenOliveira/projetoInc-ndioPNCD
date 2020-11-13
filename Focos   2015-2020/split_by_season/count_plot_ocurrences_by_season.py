import pandas as pd
import matplotlib.pyplot as plt

ocurrences_by_season = pd.DataFrame(index=['Spring', 'Summer', 'Autumn', 'Winter'])

files = {
    'Spring': 'Focos_spring.csv',
    'Summer': 'Focos_summer.csv',
    'Autumn': 'Focos_autumn.csv',
    'Winter': 'Focos_winter.csv',
}

def count_ocurrences_by_season():
    count_list = []
    for season in files:
        file = pd.read_csv(files[season])
        count_list.append(len(file))
    ocurrences_by_season['Ocurrences'] = count_list
    ocurrences_by_season.to_csv('ocurrences_by_season.csv') 
    plot_ocurrences_by_season()      
    
def plot_ocurrences_by_season():
    ax = plt.cla() 
    
    ocurrences_by_season.plot(kind='pie',y='Ocurrences',autopct='%1.1f%%',ax=ax)
    
    plt.ylabel('Número de Ocorrências')
    plt.title('Número de Ocorrências por Estação do Ano')
    plt.savefig('ocurrences_by_season.png')

count_ocurrences_by_season()
 
