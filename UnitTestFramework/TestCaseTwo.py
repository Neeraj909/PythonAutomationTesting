import unittest
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager


class TestTwo(unittest.TestCase):
    def test_lunch_browser(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.naukri.com")
        print(self.driver.title)
        self.driver.close()

    def test_facebook(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.naukri.com")
        print(self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
