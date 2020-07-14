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
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-nodes/drag-drop-nodes-demo3.html")
source = driver.find_element_by_xpath("//*[@id='node1']")
target = driver.find_element_by_xpath("//*[@id='box1']")
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()
time.sleep(10)
driver.close()
