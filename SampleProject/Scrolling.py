from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.worldometers.info/geography/countries-of-the-world/")
# Scroll down the by pixel
# driver.execute_script("window.scrollBy(0,1000)","")
# scroll the page till the element visible
# countries = driver.find_element(By.LINK_TEXT, "Jordan")
# driver.execute_script("arguments[0].scrollIntoView();", countries)
# scroll down till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.close()
