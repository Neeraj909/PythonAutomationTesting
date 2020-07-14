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
driver.get("http://demo.automationtesting.in/Register.html")
interactions = driver.find_element_by_xpath("//a[@class='dropdown-toggle' and contains(text(),'Interactions ')]")
drag = driver.find_element_by_xpath("//a[@class='dropdown-toggle' and contains(text(),'Drag and Drop ')]")
static = driver.find_element_by_xpath("//ul[@class='childmenu ']//a[contains(text(),'Static ')]")
actions = ActionChains(driver)
actions.move_to_element(interactions).move_to_element(drag).move_to_element(static).click().perform()
time.sleep(5)
driver.get("http://testautomationpractice.blogspot.com/")
ele = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions.double_click(ele).perform()
time.sleep(5)
driver.close()
