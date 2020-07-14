from selenium import webdriver;
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
btn = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(btn).perform()
time.sleep(5)
driver.close()
