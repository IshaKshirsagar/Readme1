import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://app.surein.de/?step=step_2&login=true&lang=de_de")
time.sleep(5)

driver.find_element(By.XPATH,"//font[text()='create Account']").click()
time.sleep(5)

driver.find_element_By_xpath("//input[@type='email']").send_keys('guru_289@yahoo.co.in')
time.sleep(5)

driver.find_element_By_xpath("//input[@type='password')").send_keys('123')
time.sleep(5)


driver.find_element_By_xpath("//input[@autocomplete='autocomplete']").send_keys('123')
time.sleep(5)


driver.find_element_By_xpath("//div[@style='position: relative; padding-top: 100%;']").click()
time.sleep(5)

driver.find_element_By_xpath("//button[text()='Erstellen']").click()
time.sleep(5)

driver.close()