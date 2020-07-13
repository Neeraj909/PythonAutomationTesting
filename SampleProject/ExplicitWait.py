from selenium import webdriver;
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://newtours.demoaut.com")
driver.find_element_by_css_selector("input[name='userName']").send_keys("prahan63")
driver.find_element_by_css_selector("input[name='password']").send_keys("Jivox@123")
driver.find_element_by_css_selector("input[name='login']").click()

select = Select(driver.find_elements_by_tag_name("passCount"))
select.select_by_visible_text("1")
select = Select(driver.find_elements_by_tag_name("fromPort"))
select.select_by_visible_text("New York")
select = Select(driver.find_elements_by_tag_name("fromMonth"))
select.select_by_visible_text("August")
select = Select(driver.find_elements_by_tag_name("fromDay"))
select.select_by_visible_text("20")
select = Select(driver.find_elements_by_tag_name("toPort"))
select.select_by_visible_text("Frankfurt")
select = Select(driver.find_elements_by_tag_name("toMonth"))
select.select_by_visible_text("October")
select = Select(driver.find_elements_by_tag_name("toDay"))
select.select_by_visible_text("29")
driver.find_element_by_css_selector("input[value='Business']").click()
select = Select(driver.find_elements_by_tag_name("airline"))
select.select_by_visible_text("Unified Airlines")
driver.find_element_by_css_selector("input[name='findFlights']").click()
time.sleep(5)
driver.close()
