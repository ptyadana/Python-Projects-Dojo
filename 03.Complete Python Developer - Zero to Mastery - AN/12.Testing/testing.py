import unittest
import addition

class TestMain(unittest.TestCase):

    def setUp(self):
        print("about to run a function.")

    def test_add_1(self):
        '''Sample doc string'''
        test_param1 = 10
        test_param2 = 20
        result = addition.add(test_param1,test_param2)
        self.assertEqual(result,30)

    
    def test_add_2(self):
        test_param1 = "abcdefg"
        test_param2 = 20
        result = addition.add(test_param1,test_param2)
        # self.assertTrue(isinstance(result,ValueError))
        self.assertIsInstance(result,ValueError)

    def test_add_3(self):
        test_param1 = None
        test_param2 = 20
        result = addition.add(test_param1, test_param2)
        self.assertEqual(result,"Please enter numbers.")

    def test_add4(self):
        test_param1 = ""
        test_param2 = 20
        result = addition.add(test_param1, test_param2)
        self.assertEqual(result,"Please enter numbers.")

    def test_add5(self):
        test_param1 = 0
        test_param2 = 0
        result = addition.add(test_param1, test_param2)
        self.assertEqual(result, 0)

    def tearDown(self):
        print('cleaning up !!!')

if __name__ == "__main__":
    unittest.main()

