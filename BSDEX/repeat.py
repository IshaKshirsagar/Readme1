
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


#from selenium.webdriver.common import by
#from Challenge import driver
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.surein.de/?lang=en_us&AB=&generic=&step=step_2")

driver.implicitly_wait(30)

driver.find_element(By.XPATH,"(//input[@type='email'])[position()=2]").send_keys("murli")

print ("Hello")

driver.find_element(By.XPATH,"(//input[@type='password'])[position()=1]").send_keys("murli")

print ("Hello_1")

driver.find_element(By.XPATH,"(//input[@type='password'])[position()=2]").send_keys("murli")

print ("Hello_2")

driver.find_element(By.XPATH,"(//div[contains(text(),'agree')]/..//div)[position()=1").click()

print ("Hello_3")
                                    
driver.find_element(By.XPATH,"//button[text()='create']").click() 

print ("Hello_4")

                    