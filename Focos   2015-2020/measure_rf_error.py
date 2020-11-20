import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

#Change this variable to your directory path
path = '/home/jaevillen/IEEE/projetoIncendioPNCD/Focos   2015-2020/'

file_names = [
    path+'Focos_2015-01-01_2015-12-31.csv',
    path+'Focos_2016-01-01_2016-12-31.csv',
    path+'Focos_2017-01-01_2017-12-31.csv',
    path+'Focos_2018-01-01_2018-12-31.csv',
    path+'Focos_2019-01-01_2019-12-31.csv',
]

column_to_analise = 'riscofogo'
rmse_by_year = pd.DataFrame(index=['2015', '2016', '2017', '2018', '2019', 'Total'])

def plt_hist(df):
	df.plot.hist()
	
	plt.xlabel(column_to_analise)
	plt.title(column_to_analise + '2015-2019')
	plt.savefig(column_to_analise+'_all_years_hist.png')
 
def make_test_ds(file_len):
    an_array = np.full((file_len, 1), 1.0)
    return pd.DataFrame(an_array)

def calculate_rmse(y_pred):
    y_test = make_test_ds(len(y_pred))
    rmse = sqrt(mean_squared_error(y_test, y_pred))*100
    return "{0:.2f}%".format(rmse)

def get_rf_pred_error():
    rmse_list = []
    all_years = pd.DataFrame(index=[column_to_analise])
    for file in file_names:
        focos = pd.read_csv(file, usecols=[column_to_analise])
        focos = focos.dropna()
        all_years = all_years.append(focos, ignore_index=True)
       
        rmse = calculate_rmse(focos)
        rmse_list.append(rmse)
        print('In file: '+file)
        print("rmse: "+rmse)

    total_rmse = calculate_rmse(all_years.dropna())
    rmse_list.append(total_rmse)
    print('All years ')
    print("rmse: "+total_rmse)
    
    rmse_by_year['RMSE'] = rmse_list
    rmse_by_year.to_csv(path+'rf_rmse_by_year.csv') 
    
    plt_hist(all_years)

            
get_rf_pred_error()
