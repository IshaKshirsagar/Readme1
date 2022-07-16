import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://app.surein.de/?lang=en_us&AB=&generic=&step=step_2")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH,"(//input[@type='email'])[position()=2]").send_keys("guru_289@yahoo.co.in")
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='password'])[position()=1]").send_keys("1Faurecia!")
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='password'])[position()=2]").send_keys("1Faurecia!")
time.sleep(2)


driver.find_element(By.XPATH,"(//div[@style='position: relative; padding-top: 100%;'])[position()=2]").click()
time.sleep(2)


driver.find_element(By.XPATH,"(//button[@class='bubble-element Button clickable-element'])[position()=8]").click()
time.sleep(2)


driver.close()
