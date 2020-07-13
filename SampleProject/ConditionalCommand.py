from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://newtours.demoaut.com")
time.sleep(5)
driver.find_element_by_css_selector("input[name='userName']").send_keys("prahan63")
driver.find_element_by_css_selector("input[name='password']").send_keys("Jivox@123")
driver.find_element_by_css_selector("input[name='login']").click()
time.sleep(5)
radioBtn=driver.find_element_by_css_selector("input[value='oneway']")
print(radioBtn.is_selected())
driver.close()

