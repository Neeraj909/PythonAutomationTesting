from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
time.sleep(5)
select = Select(driver.find_element_by_id("Skills"))
# select.select_by_visible_text("Data Analytics")
# time.sleep(5)
select.select_by_index(4)
time.sleep(5)
# select.select_by_value("Desktop Publishing")
# time.sleep(5)
#count num of options
print(len(select.options))
allOptions=select.options
for option in allOptions:
    print(option.text)
links=driver.find_elements(By.TAG_NAME,"a")
print("number of links",len(links))
for link in links:
    print(link.text)
driver.find_element(By.LINK_TEXT,"More").click()
time.sleep(5)
driver.close()

