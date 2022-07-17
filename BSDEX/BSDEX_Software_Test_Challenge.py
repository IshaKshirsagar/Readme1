#from distutils.command.install import value
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://widgets.bsdex.de/de/market-detail?market=btc-eur,xrp-eur,ltc-eur,eth-eur,bch-eur,uni-eur,link-eur")
time.sleep(2)
driver.maximize_window()

#BTC UI testing-24H,1W,1M,YTD
driver.find_element(By.XPATH,"//div[text()='BTC']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1W']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1M']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='YTD'][position()=1]").click()
time.sleep(2)

#ETH UI testing-24H,1W,1M,YTD
driver.find_element(By.XPATH,"//div[text()='ETH']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1W']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1M']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='YTD'][position()=1]").click()
time.sleep(2)

#LTC UI testing-24H,1W,1M,YTD
driver.find_element(By.XPATH,"//div[text()='LTC']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1W']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1M']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='YTD'][position()=1]").click()
time.sleep(2)

#XRP UI testing-24H,1W,1M,YTD
driver.find_element(By.XPATH,"//div[text()='XRP']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1W']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1M']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='YTD'][position()=1]").click()
time.sleep(2)

#BCH UI testing-24H,1W,1M,YTD
driver.find_element(By.XPATH,"//div[text()='BCH']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1W']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1M']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='YTD'][position()=1]").click()
time.sleep(2)

#general.uni UI testing-24H,1W,1M,YTD
driver.find_element(By.XPATH,"//div[text()='general.uni']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1W']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1M']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='YTD'][position()=1]").click()
time.sleep(2)

#general.link UI testing-24H,1W,1M,YTD
driver.find_element(By.XPATH,"//div[text()='general.link']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1W']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='1M']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='YTD'][position()=1]").click()
time.sleep(2)



#driver.find_element(By.XPATH,"(//*[text()='Chainlink Handeln'])[1]").click()
#time.sleep(2)

#driver.find_element(By.XPATH,"(//span[text()='Bitcoin Handeln'])[1]").click()
#time.sleep(2)


driver.close()