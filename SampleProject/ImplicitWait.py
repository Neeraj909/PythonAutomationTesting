from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://newtours.demoaut.com")
assert "Welcome: Mercury Tours" in driver.title
driver.find_element_by_css_selector("input[name='userName']").send_keys("prahan63")
driver.find_element_by_css_selector("input[name='password']").send_keys("Jivox@123")
driver.find_element_by_css_selector("input[name='login']").click()
driver.close()
