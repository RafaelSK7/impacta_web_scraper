from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

df = pd.DataFrame(columns=['Código', 'Setor', 'Preço Atual', 'Liquidez Diaria',
                              'Dívidendo', 'Dividend Yield', 'Dividend Yield Anual',
                              'Variação Preço', 'P/VP', 'Vacância Física', 'Vacância Financeira'])
dict_list = []
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.get('https://www.fundsexplorer.com.br/ranking')
for i in range(1, 329):

    codigo = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[1]/a'.format(i)).text
    setor = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[2]'.format(i)).text
    precoAtual = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[3]'.format(i)).text
    liquidezDiaria = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[4]'.format(i)).text
    dividendo = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[5]'.format(i)).text
    dividendYield = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[6]'.format(i)).text
    dividendYieldAnual = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[13]'.format(i)).text
    variacaoPreco = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[14]'.format(i)).text
    pvp = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[19]'.format(i)).text
    vacanciaFisica = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[24]'.format(i)).text
    vacanciaFinanceira = driver.find_element(By.XPATH, '//*[@id="table-ranking"]/tbody/tr[{}]/td[25]'.format(i)).text

    row_dict = {'codigo':codigo, 'setor':setor, 'precoAtual':precoAtual, 'liquidezDiaria':liquidezDiaria,
        'dividendo':dividendo, 'dividendYield':dividendYield, 'dividendYieldAnual':dividendYieldAnual,'variacaoPreco':variacaoPreco,
        'pvp':pvp, 'vacanciaFisica':vacanciaFisica,'vacanciaFinanceira':vacanciaFinanceira}
    dict_list.append(row_dict)

df = pd.DataFrame.from_dict(dict_list)
df.to_csv('C:/Users/rafae/Desenvolvimento/Faculdade/Web Mining/SeleniumAulas/realEstateInvestmentsTrustScraper/basesOriginais/reits.csv')