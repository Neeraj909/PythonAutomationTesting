from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
#driver.find_element(By.LINK_TEXT,"Open New Seperate Windows").click()
time.sleep(5)
print(driver.current_window_handle)
driver.find_element_by_css_selector(".btn.btn-info").click()
time.sleep(5)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()

