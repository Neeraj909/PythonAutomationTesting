from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager

from SampleProject import XlUtills

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.facebook.com/")
path = "/Users/neerajsharma/Desktop/AutomationTestPyhton/neeraj.xlsx"

rows = XlUtills.getRowCount(path, "Sheet1")
for r in range(2, rows + 1):
    userName = XlUtills.getReadData(path, "Sheet1", r, 1)
    password = XlUtills.getReadData(path, "Sheet1", r, 2)
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(userName)
    driver.find_element_by_id("pass").clear()
    driver.find_element_by_id("pass").send_keys(str(password))
    driver.find_element_by_id("loginbutton").click()
    if driver.title == "Facebook":
        XlUtills.writeDataIntoExcel(path, "Sheet1", r, 3, "test passed")
    else:
        XlUtills.writeDataIntoExcel(path, "Sheet1", r, 3, "failed")
