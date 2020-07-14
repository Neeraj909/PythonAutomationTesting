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
driver.get("http://demo.automationtesting.in/FileUpload.html")
driver.find_element_by_xpath("//*[@id='input-4']").send_keys("/Users/neerajsharma/Desktop/IMG20190329144507.jpg")
time.sleep(5)
driver.close()