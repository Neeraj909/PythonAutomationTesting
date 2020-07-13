from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://newtours.demoaut.com")
print(driver.title)
time.sleep(5)
driver.get("http://demo.automationtesting.in/Register.html")
print(driver.title)
time.sleep(5)
driver.back()
time.sleep(5)
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
time.sleep(5)
driver.close()