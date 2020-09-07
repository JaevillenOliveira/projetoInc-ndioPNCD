import pandas as pd

focos = {
 "2015": "Focos_2015-01-01_2015-12-31.csv",
 "2016": "Focos_2016-01-01_2016-12-31.csv",
 "2017": "Focos_2017-01-01_2017-12-31.csv",
 "2018": "Focos_2018-01-01_2018-12-31.csv",
 "2019": "Focos_2019-01-01_2019-12-31.csv",
 "2020": "Focos_2020-01-01_2020-08-13.csv",
}

auxDf = {
    "01": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "02": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "03": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "04": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "05": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "06": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "07": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "08": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "09": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "10": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "11": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
    "12": pd.DataFrame(columns = ['datahora', 'satelite', 'pais', 'estado', 'municipio', 'bioma', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude', 'frp', 'areaprotegida']),
}
    
def clearAuxDf(): 
    for month in auxDf:
        auxDf[month].drop(auxDf[month].index, inplace=True)
        
def getMonth(datahora):
    return datahora.split('/')[1]

def buildCSVDataset(auxDf):
    for i in auxDf:
        length = len(auxDf[i].index)
        if(length > 0):
            outName = 'SplitMonth/Focos_' + year + '_' + i + '.csv'
            print('Building dataset: ' + outName)
            auxDf[i].to_csv(outName)
            
def splitByMonth(df):
    length = str(len(df.index))
    for i, row in df.iterrows():
        datahora = df.loc[i, 'datahora']
        month = getMonth(datahora)
        print('appending to month ' + month + ' | ' + str(i) + ' from ' + length + ' of ' + year);
        auxDf[month] = auxDf[month].append(row, ignore_index = True)

#Percorrer cada arquivo
for year in focos:   
    df = pd.read_csv(focos[year]);
    
    #percorrer as linhas e deixar em seu respectivo dataframe
    splitByMonth(df);
    
    #Construindo o csv do respectivo ano
    buildCSVDataset(auxDf);
    
    #Limpando o dicionário
    clearAuxDf();
    
    print('Split ' + year + ' already done');
        
print('-------------> Done <------------------')

        