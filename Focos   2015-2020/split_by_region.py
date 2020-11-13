import pandas as pd

file_names = [
    'Focos_2015-01-01_2015-12-31.csv',
    'Focos_2016-01-01_2016-12-31.csv',
    'Focos_2017-01-01_2017-12-31.csv',
    'Focos_2018-01-01_2018-12-31.csv',
    'Focos_2019-01-01_2019-12-31.csv',
]

focos_by_region = {
 'ANDARAI': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_andarai.csv'},
 'BONINAL': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_boninal.csv'},
 'IBICOARA': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_ibicoara.csv'},
 'IRAMAIA': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_iramaia.csv'},
 'IRAQUARA': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_iraquara.csv'},
 'ITAETE': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_itaete.csv'},
 'LENCOIS': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_lencois.csv'},
 'MUCUGE': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_mucuge.csv'},
 'NOVA REDENCAO': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_novaredencao.csv'},
 'PALMEIRAS': {'df':pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']), 
            'name':'Focos_palmeiras.csv'},
}

def results_to_csv():
    for region in focos_by_region:
        focos_by_region[region]['df'].to_csv(focos_by_region[region]['name'])
        
def split_by_region():
    for file in file_names:
        focos = pd.read_csv(file)
        for index, row in focos.iterrows():
            region = row['municipio']
            focos_by_region[region]['df'] = focos_by_region[region]['df'].append(row, ignore_index=True)
        print(file+' Split Succesfully ')


split_by_region()   
results_to_csv()
