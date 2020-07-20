import unittest


class Test(unittest.TestCase):
    @unittest.SkipTest
    def test_search(self):
        print("this is search test")

    @unittest.skip("I am skipping this test cases")
    def advanced_search(self):
        print("advanced search")


if __name__ == '__main__':
    unittest.main
