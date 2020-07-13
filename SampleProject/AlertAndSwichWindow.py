from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Alerts.html")
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Alert with OK & Cancel").click()
time.sleep(5)
driver.find_element_by_css_selector(".btn.btn-primary").click()
driver.switch_to.alert.accept()
driver.find_element_by_css_selector(".btn.btn-primary").click()
driver.switch_to.alert.dismiss()
time.sleep(5)
driver.close()
