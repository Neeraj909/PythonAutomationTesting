from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.save_screenshot("/Users/neerajsharma/Desktop/homepage.png")
driver.get_screenshot_as_file("/Users/neerajsharma/Desktop/homepage1.jpg")  # this will accept only jpg format
driver.close()
