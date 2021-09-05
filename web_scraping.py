from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime

nav = webdriver.Chrome()

moedas = ['Dólar Americano', 'Euro', 'Libra esterlina', 
          'Iene', 'Dólar Australiano', 'Dólar Canadense', 
          'Peso Argentino', 'Lira Turca', 'Bitcoin']

precos = {}

for moeda in moedas:
    nav.get('https://www.google.com')
    string = 'Cotação {}'.format(moeda)
    nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(string)
    nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    precos[moeda] = float(nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
