from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://neeraj.qa3.app.jivox.com/login.html")
driver.find_element_by_css_selector("#loginEmail").send_keys("neerajs+a@jivox.com")
driver.find_element_by_css_selector("#loginPassword").send_keys("Jivox@123")
driver.find_element_by_css_selector("#btnSignIn").click()
print(driver.title)
print(driver.page_source)
driver.close()

