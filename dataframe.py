import pandas as pd

df = pd.read_excel('dados_pessoais.xlsx')
df['CPF'] = df['CPF'].apply(lambda x: str(x).zfill(11))

df2 = pd.read_excel('dados.xlsx')
df2['CPF'] = df2['CPF'].apply(lambda x: str(x).zfill(11))

df2 = df2.rename(columns={'nome':'Nome', 'idade':'Idade','sobrenome': 'Sobrenome'})

df2 = df2[['Nome', 'CPF', 'Sobrenome', 'Idade']]


df = df.merge(df2[['CPF','Sobrenome','Idade']], on ='CPF', how = 'left')

df = df[['Nome', 'Sobrenome', 'Idade','Cargo','Empresa','Telefone','CPF']]

df['Telefone'] = df['Telefone'].astype(str)

df.to_excel('dados_completos.xlsx', index=False)

print(df)