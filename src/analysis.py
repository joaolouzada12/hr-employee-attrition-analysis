import pandas as pd 

df = pd.read_csv('data/raw/employees.csv')

# limpeza dos dados

df['Saiu'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df_tempo_trabalho = df.groupby('OverTime')['Saiu'].mean()

df['FaixaSalarial'] = pd.cut(
    df['MonthlyIncome'],
    bins=[0, 4000, 7000, float('inf')],
    labels=['Baixo', 'Médio', 'Alto']
)
resultado_faixa = df.groupby('FaixaSalarial')['Attrition'].value_counts(normalize=True)

df_baixo_extra = df.groupby(['FaixaSalarial','OverTime'])['Saiu'].mean()

print(df_baixo_extra)