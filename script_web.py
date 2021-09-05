import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


moeda = 'Bitcoin'

dia = int(datetime.today().strftime('%d')) - 1
mes = int(datetime.today().strftime('%m'))
ano = int(datetime.today().strftime('%Y'))
df = pd.read_csv('moedas.csv')
df = df[df['nome'] == moeda] 
valor_real = float(df[(df['dia'] == dia) & (df['mes'] == mes) & (df['ano'] == ano)]['valor'])

st.write('# {}'.format(moeda))

st.write('''## Valor da moeda
A moeda **{0}** está valendo, atualmente, R${1}  a unidade.
Portanto, no dia {2}/{3}/{4}, 1 {0} é equivalente a {1} reais.'''.format(moeda, valor_real, dia, mes, ano))

intervalo_dias = 0

st.write('''## Variação do valor de câmbio
O gráfico abaixo mostra as mudanças de preço da moeda 
nos últimos {} dias.'''.format(intervalo_dias))

x = [1,2,3,4,5]
y = [2,4,8,16,32]

fig, ax = plt.subplots(figsize=(13,7))
ax.plot(x,y)
st.pyplot(fig=fig)