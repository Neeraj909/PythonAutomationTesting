import unittest
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager


class AssertionTrue(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://demo.automationtesting.in/Register.html")
        print(self.driver.title)
        title = self.driver.title
        self.assertTrue(title == "Register")
        self.assertFalse(title == "test")
        self.driver.close()


if __name__ == '__main__':
    unittest.main
