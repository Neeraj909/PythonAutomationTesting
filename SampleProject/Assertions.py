import unittest
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager


class AssertionTest(unittest.TestCase):

    def testName(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://demo.automationtesting.in/Register.html")
        print(self.driver.title)
        title = self.driver.title
        self.assertEqual("Register", title, "Web page is not same")
        self.assertNotEquals("test", title)
        self.driver.close()


if __name__ == '__main__':
    unittest.main
