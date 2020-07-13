from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_css_selector(".link.linkedin").click()
time.sleep(5)
driver.quit()


