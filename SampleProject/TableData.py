from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.w3schools.com/html/html_tables.asp")
row = len(driver.find_elements_by_css_selector(".w3-example>div>table#customers>tbody>tr"))
col = len(driver.find_elements_by_css_selector(".w3-example>div>table#customers>tbody>tr:nth-child(1)>th"))
time.sleep(5)
for r in range(2, row + 1):
    for c in range(1, col + 1):
        value = driver.find_element_by_css_selector(
            ".w3-example>div>table#customers>tbody>tr:nth-child(" + str(r) + ")>td:nth-child(" + str(c) + ")").text
        print(value,end='  ')
    print()

driver.close()
