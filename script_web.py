import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from funcoes import *

#Escrevendo na side bar
st.sidebar.write('''## Obrigado por utilizar minha aplicação!
Me chamo Vinícius Pilan, sou graduando em Ciência da computação e procuro me especializar na área de dados.

Para saber mais sobre mim, sobre esse projeto e também sobre outros projetos que fiz:
- Linkedin: Vinícius de Paula Pilan
- GitHub: [ViniPilan](https://github.com/ViniPilan)
- GitHub do projeto: https://github.com/ViniPilan/moedas''')



#Carregando as variáveis ---------------------------------------------------------------------
moeda = st.selectbox(
    'Escolha a moeda que você está buscando:',
    ('Dólar Americano', 'Euro', 'Libra esterlina', 'Iene', 'Peso Argentino', 'Bitcoin'))

df = pd.read_csv('moedas.csv')
df = df[df['nome'] == moeda] 

dia = int(datetime.today().strftime('%d'))
mes = int(datetime.today().strftime('%m'))
ano = int(datetime.today().strftime('%Y'))
hora = int(df[(df['dia'] == dia) & (df['mes'] == mes) & (df['ano'] == ano)]['hora'])
minuto = int(df[(df['dia'] == dia) & (df['mes'] == mes) & (df['ano'] == ano)]['minuto'])
valor_real = float(df[(df['dia'] == dia) & (df['mes'] == mes) & (df['ano'] == ano)]['valor'])



#Escrita da página ---------------------------------------------------------------------------
#Título
st.write('# {}'.format(moeda))

#Valor da moeda 
st.write('''## Valor da moeda
A moeda **{0}** está valendo, atualmente, {1:.2f} reais a unidade. Portanto, **1 {0} é equivalente a R${1:.2f} reais**.

O valor de {0} foi atualizado na data {2}/{3}/{4} no horário {5}:{6}'''.format(moeda, valor_real, formata_numero(dia), 
                                                                        formata_numero(mes), ano, formata_numero(hora), formata_numero(minuto)))


#Calculadora de conversão
st.write('''## Calculadora conversão
Utilize a calculadora abaixo para fazer a conversão de valor da moeda escolhida.''')

numero01 = st.number_input('Insira o valor que deseja converter')

col1, col2 = st.columns(2)

with col1:
    converter_moeda_para_real = st.button('Converter {} para real'.format(moeda))

with col2:
    converter_real_para_moeda = st.button('Converter real para {}'.format(moeda))

if converter_moeda_para_real:
    numero02 = numero01*valor_real
    st.write('{0:.2f} {2} são R${1:.2f}.'.format(numero01, numero02, moeda))  

if converter_real_para_moeda:
    numero02 = numero01/valor_real
    st.write('R${0:.2f} são {1:.2f} {2}.'.format(numero01, numero02, moeda))


#Gráfico de variação do valor
intervalo_dias = len(list(df['data'].unique()))

st.write('''## Variação do valor da moeda
O gráfico abaixo mostra as mudanças de preço da moeda **{0}** nos últimos {1} dias.'''.format(moeda, intervalo_dias))

fig = go.Figure(data=go.Scatter(x=df['data'], y=df['valor'], mode='lines+markers', line = dict(color='darkred', width=2)))
st.plotly_chart(fig)