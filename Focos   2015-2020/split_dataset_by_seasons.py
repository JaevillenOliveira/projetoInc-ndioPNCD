import pandas as pd
import datetime

path = '/home/jaevillen/IEEE/projetoIncendioPNCD/Focos   2015-2020/'
file_names = [
    path+'Focos_2015-01-01_2015-12-31.csv',
    path+'Focos_2016-01-01_2016-12-31.csv',
    path+'Focos_2017-01-01_2017-12-31.csv',
    path+'Focos_2018-01-01_2018-12-31.csv',
    path+'Focos_2019-01-01_2019-12-31.csv',
]

focos_by_season = {
 'summer': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':path+'Focos_summer.csv'},
 'autumn': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':path+'Focos_autumn.csv'},
 'winter': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':path+'Focos_winter.csv'},
 'spring': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':path+'Focos_spring.csv'},
}

Y = 2000 
seasons = {
    'summer_end':   {'start': datetime.date(Y, 1, 1),   'end':datetime.date(Y, 3, 19)}, #{'start': {'month':12, 'day':21}, 'end':{'month':3, 'day':21}}, 
    'autumn':       {'start': datetime.date(Y, 3, 20),  'end':datetime.date(Y, 6, 19)}, #{'start': {'month':3, 'day':21}, 'end':{'month':6, 'day':21}}, 
    'winter':       {'start': datetime.date(Y, 6, 20),  'end':datetime.date(Y, 9, 21)}, #{'start': {'month':6, 'day':21}, 'end':{'month':9, 'day':23}}, 
    'spring':       {'start': datetime.date(Y, 9, 22),  'end':datetime.date(Y, 12, 20)}, #{'start': {'month':9, 'day':23}, 'end':{'month':12, 'day':21}}, 
    'summer_start': {'start': datetime.date(Y, 12, 21), 'end':datetime.date(Y, 12, 31)}, #{'start': {'month':12, 'day':21}, 'end':{'month':3, 'day':21}}, 
}

def get_date(row):
    date = row['datahora'].split()[0]
    month = date.split('/')[1]
    day = date.split('/')[2]
    return datetime.date(Y, int(month), int(day))

def get_season(row):
    date = get_date(row)
    for season in seasons:
        if ((date >= seasons[season]['start']) & (date <= seasons[season]['end'])):
            return season

def results_to_csv():
    for season in focos_by_season:
        focos_by_season[season]['df'].to_csv(focos_by_season[season]['name'])
        
def split_by_season():
    for file in file_names:
        focos = pd.read_csv(file)
        for index, row in focos.iterrows():
            season = get_season(row)
            if((season == 'summer_start') | (season == 'summer_end')):
                season = 'summer'
            focos_by_season[season]['df'] = focos_by_season[season]['df'].append(row, ignore_index=True)
        print(file+' Split Succesfully ')


split_by_season()   
results_to_csv()
