import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
'''
path = 'dados'
filename = {
    'ipca mensal':'IPCA - Variação mensal', 
    'ipca acumulado':'IPCA - Variação acumulada em 12 meses', 
    'dolar':'Cotação do Dólar', 'oil':'RBRTEm'
}

#--------------------------------------------------------------------
mes_num = {
    'janeiro':'01', 'fevereiro':'02', 'março':'03', 
    'abril':'04','maio':'05', 'junho':'06', 
    'julho':'07', 'agosto':'08', 'setembro':'09', 
    'outubro':'10', 'novembro':'11', 'dezembro':'12'
}
def month_to_num(text):
    m, y = text.split(' ')
    return mes_num[m]+'-'+y

df0 = pd.read_csv(os.path.join(path, filename['ipca mensal']+'.tsv'), sep='\t', names=['mês', 'valor']).replace('...', np.nan)
df0['mês'] = df0['mês'].apply(month_to_num)
df0.to_csv(os.path.join(path, filename['ipca mensal']+'.csv'), index=False)

#--------------------------------------------------------------------

df1 = pd.read_csv(os.path.join(path, filename['ipca acumulado']+'.tsv'), sep='\t', names=['mês', 'valor']).replace('...', np.nan)
df1['mês'] = df1['mês'].apply(month_to_num)
df1.to_csv(os.path.join(path, filename['ipca acumulado']+'.csv'), index=False)

#--------------------------------------------------------------------

df2 = pd.read_csv(os.path.join(path, filename['dolar']+'.csv'))
f = lambda x: float(x.replace(',', '.'))
g = lambda x: datetime.strftime(datetime.strptime(x.split(' ')[0], '%Y-%m-%d'), '%d-%m-%Y')
df2['cotacaoCompra'] = df2['cotacaoCompra'].apply(f)
df2['cotacaoVenda'] = df2['cotacaoVenda'].apply(f)
df2['dataHoraCotacao'] = df2['dataHoraCotacao'].apply(g)
df2.rename(columns={'cotacaoCompra':'compra', 'cotacaoVenda':'venda', 'dataHoraCotacao':'data'}).to_csv(os.path.join(path, filename['dolar']+'.csv'), index=False)

#--------------------------------------------------------------------

df3 = pd.read_csv(os.path.join(path, filename['oil']+'.csv'), sep=';').replace()
f = lambda x: float(x.replace(',', '.'))
g = lambda x: datetime.strftime(datetime.strptime(x.split(' ')[0], '%b-%y'), '%m-%Y')
df3['date'] = df3['date'].apply(g)
df3['brent spot price'] = df3['brent spot price'].apply(f)
df3.to_csv(os.path.join(path, filename['oil']+'.csv'), index=False)
'''
#--------------------------------------------------------------------

dados = pd.read_csv('PRICES_CPI.csv')

form = '%Y-%m'
datas = [datetime.strptime(data, form) for data in set(dados['TIME'].values)]
datas.sort()
datast = [datetime.strftime(data, '%m-%Y') for data in datas]
locations = set(dados['Country'].values)

df = {}
for name in locations:
    values = []
    try:
        this_data = dados.loc[dados['Country'] == name]
        for i, month in enumerate(datas):
            if datetime.strftime(month, form) in this_data['TIME'].values: 
                values.append(this_data.iloc[i]['Value'])
            else: values.append(np.nan)
    except IndexError: pass
    else: df[name] = values
    
df['Date'] = datast
df = pd.DataFrame(df).to_csv('PRICES_CPI.csv', index=False)
