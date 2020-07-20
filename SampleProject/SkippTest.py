import unittest


class SkippTest(unittest.TestCase):

    def test_search(self):
        print("this is search test")

    def advanced_search(self):
        print("advanced search")

    def prepaid_recharge(self):
        print("prepaid recharge")

    def post_prepaid(self):
        print("postpaid recharge")


if __name__ == '__main__':
    unittest.main
