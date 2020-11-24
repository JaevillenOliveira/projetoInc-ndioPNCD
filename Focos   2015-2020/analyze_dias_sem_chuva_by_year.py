import pandas as pd
import numpy as np
import statistics as stats
import scipy 

#Change this variable to your directory path
path = '/home/jaevillen/IEEE/projetoIncendioPNCD/Focos   2015-2020/'

file_names = [
    path+'Focos_2015-01-01_2015-12-31.csv',
    path+'Focos_2016-01-01_2016-12-31.csv',
    path+'Focos_2017-01-01_2017-12-31.csv',
    path+'Focos_2018-01-01_2018-12-31.csv',
    path+'Focos_2019-01-01_2019-12-31.csv',
]

column_to_analyze = 'diasemchuva'
diasemchuva_by_year = pd.DataFrame(index=['2015', '2016', '2017', '2018', '2019', 'Total'])

def analyze_stats():
    median_year = []
    mean_year = []
    diasemchuva_all_years = pd.DataFrame(index=[column_to_analyze])
    for file in file_names:
        focos = pd.read_csv(file, usecols=[column_to_analyze])
        diasemchuva_all_years = diasemchuva_all_years.append(focos, ignore_index=True)
        print('In file: '+file)
        
        median_year.append(stats.median(focos[column_to_analyze]))
        mean_year.append(scipy.nanmean(focos[column_to_analyze]))
        
    median_year.append(stats.median(diasemchuva_all_years[column_to_analyze]))
    mean_year.append(scipy.nanmean(diasemchuva_all_years[column_to_analyze]))
    
    diasemchuva_by_year['Mediana'] = median_year
    diasemchuva_by_year['Média'] = mean_year
    
    diasemchuva_by_year.to_csv(path+'diasemchuva_stats_by_year.csv')    
    
analyze_stats()