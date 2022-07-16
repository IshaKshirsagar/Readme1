import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://widgets.bsdex.de/de/market-detail?market=btc-eur,xrp-eur,ltc-eur,eth-eur,bch-eur,uni-eur,link-eur")
time.sleep(5)

driver.maximize_window()

driver.find_element(By.XPATH,"//div[text()='24H']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//div[@class='styled__SwitchButton-sc-f37nkm-1 esojeD']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//div[@class='styled__SwitchButton-sc-f37nkm-1 gGMICq']").click()
time.sleep(5)