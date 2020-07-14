from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options();
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "/Users/neerajsharma/Desktop/"})
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.find_element_by_xpath("//*[@id='textbox']").send_keys("dsdsssssfasf")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
time.sleep(2)
driver.find_element_by_id("link-to-download").click()
time.sleep(5)
driver.close()
