import pandas as pd
import numpy as np

#Change this variable to your directory path
path = '/home/jaevillen/IEEE/projetoIncendioPNCD/Focos   2015-2020/'

file_names = [
    path+'Focos_2015-01-01_2015-12-31.csv',
    path+'Focos_2016-01-01_2016-12-31.csv',
    path+'Focos_2017-01-01_2017-12-31.csv',
    path+'Focos_2018-01-01_2018-12-31.csv',
    path+'Focos_2019-01-01_2019-12-31.csv',
    path+'Focos_2020-01-01_2020-08-13.csv',
]

columns_to_fix = ['diasemchuva', 'precipitacao', 'riscofogo']

def clean():
    for file in file_names:
        focos = pd.read_csv(file)
        print('In file: '+file)
        for index, row in focos.iterrows():       
            for column in columns_to_fix:    
                if(row[column] == -999): # -999 is an invalid value, as told by INPE
                    print('At Row: '+str(index)+ ' Column: '+column+ 'Value: '+str(row[column]))
                    focos.at[index, column] = np.nan
            
        focos.to_csv(file)    

clean()