import unittest
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager


class AssertionTrue(unittest.TestCase):
    def testName(self):
        List = {"Java", "python", "JDBC"}
        self.assertIn("Java",List)



if __name__ == '__main__':
    unittest.main
