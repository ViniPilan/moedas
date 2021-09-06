from os import terminal_size
from os import system
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime

#Inicializa o navegador
nav = webdriver.Chrome()


#Lista de moedas que serão pesquisadas
moedas = ['Dólar Americano', 'Euro', 'Libra esterlina', 
          'Iene', 'Dólar Australiano', 'Dólar Canadense', 
          'Peso Argentino', 'Lira Turca', 'Bitcoin']

df = pd.read_csv('moedas.csv')


#Armazena uma cópia de backup das moedas antes de fazer as alterações
df.to_csv('moedas_anteriores_backup.csv', index=False)


#Armazena a data do momento de execução para verificar se ja houve execução desse script no dia atual
dia = int(datetime.today().strftime('%d')) 
mes = int(datetime.today().strftime('%m'))
ano = int(datetime.today().strftime('%Y'))
data = str(dia) + '/' + str(mes) + '/' + str(ano)

#Como não se deve ter inserções da mesma moeda em um mesmo dia, desconsidera 
#qualquer dado inserido no dia atual antes dessa atual execução do script
df = df[df['data'] != data]


#Para cada moeda na lista definida no começo do script
for moeda in moedas:
    #Pesquisa a moeda na web
    nav.get('https://www.google.com')
    string = 'Cotação {}'.format(moeda)
    nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(string)
    nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    
    #Armazena o valor da moeda, junto com a data de consulta e o horário
    valor = float(nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
    dia = int(datetime.today().strftime('%d')) 
    mes = int(datetime.today().strftime('%m'))
    ano = int(datetime.today().strftime('%Y'))
    hora = int(datetime.today().strftime('%H'))
    minuto = int(datetime.today().strftime('%M'))

    dicio = {}

    dicio['nome'] = [moeda]
    dicio['valor'] = [valor]
    dicio['dia'] = [dia]
    dicio['mes'] = [mes]
    dicio['ano'] = [ano]
    dicio['data'] = [str(dia) + '/' + str(mes) + '/' + str(ano)]
    dicio['hora'] = [hora]
    dicio['minuto'] = [minuto] 
    
    print(dicio)

    #Armazena a nova informação do data frame com todas as moedas
    df_aux = pd.DataFrame(data=dicio)
    df = pd.concat([df, df_aux], axis=0, ignore_index=True)


#Atualiza o data frame 
df.to_csv('moedas.csv', index=False)

print('Data frame atualizado!')
system('pause')