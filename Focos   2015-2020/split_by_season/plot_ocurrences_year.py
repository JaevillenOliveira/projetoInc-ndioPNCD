import pandas as pd
import matplotlib.pyplot as plt

path = '/home/jaevillen/IEEE/projetoIncendioPNCD/Focos   2015-2020/'

ocurrences_by_year = pd.read_csv(path+'tabelaOcorrenciasXAno.csv', index_col='Ano')
print(ocurrences_by_year)

def plot_ocurrences_by_year_fr():
    ax = plt.cla() 
    
    ocurrences_by_year.plot(kind='pie',y='Frequência Relativa',autopct='%1.1f%%',ax=ax)
    
    # plt.ylabel('Número de Ocorrências')
    # plt.title('Número de Ocorrências por Estação do Ano')
    plt.savefig(path+'ocorrencias_por_ano.png')
    
plot_ocurrences_by_year_fr()    