from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.in/")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# add the cookies
cookie = {'name': 'myCookie', 'value': '1111313134'}

driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# delete the cookie
driver.delete_cookie('myCookie')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
driver.close()

