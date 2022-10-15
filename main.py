from importlib.resources import contents
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
navegador.get('https://www.airbnb.com')
sleep(5)
navegador.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/header/div/div[2]/div/div/div/div[1]/div/button[1]/div').click()
sleep(3)
navegador.find_element(By.XPATH,'//*[@id="bigsearch-query-location-input"]').send_keys('São Paulo')
navegador.find_element(By.XPATH,'//*[@id="bigsearch-query-location-input"]').submit()
sleep(3)
page_content = navegador.page_source
sleep(3)
site = BeautifulSoup(page_content, 'html.parser')
hospedagens = site.findAll('div',attrs={'itemprop':"itemListElement"})
dados = []
for hospedagem in hospedagens:
    hospedagem_descricao = hospedagem.find('span',attrs={'class':"t6mzqp7 dir dir-ltr"}).text
    hospedagem_preco = hospedagem.find('span' , attrs={'class': 'a8jt5op dir dir-ltr'}).text
    hospedagem_nome =  hospedagem.find('div' , attrs={'class': 't1jojoys dir dir-ltr'}).text
    print('nome: ',hospedagem_nome)
    print('descrição: ',hospedagem_descricao)
    print('preço: ',hospedagem_preco)
    dados.append([hospedagem_nome,hospedagem_descricao,hospedagem_preco])

dados = pd.DataFrame(dados,columns=['nome','descrição','preço'])    
dados.to_csv('dados_hospedagens.csv', index=False)
