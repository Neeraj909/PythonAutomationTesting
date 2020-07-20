import unittest




class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("this is login test")

    @classmethod
    def setUpClass(cls) :
        print("opening app")



    def test_search(self):
        print("this is search test")

    def test_advancedSearch(self):
        print("this is advanced searched")

    def test_prepaidRecharg(self):
        print("this pri reacharge")

    def test_postrecharge(self):
        print("this is post charge ")

    @classmethod
    def tearDown(self):
        print("close the test")
    @classmethod
    def tearDownClass(cls):
        print("close the app")


