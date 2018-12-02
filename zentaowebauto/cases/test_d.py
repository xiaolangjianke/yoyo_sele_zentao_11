import unittest

def add(a, b):
    c = a+2*b
    return c

class TestAdd(unittest.TestCase):
    '''测试集合的注释'''

    @classmethod
    def setUpClass(cls):
        print("每个class用例开始前。只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("每个class结束后。只执行一次")

    def setUp(self):
        print("前置操作")

    def tearDown(self):
        print("后置操作")

    def test_001(self):
        '''测试用例 2, 3'''
        print("test_001")
        result = add(2, 3)
        expect = 18
        self.assertEqual(result, expect)

    def test_002(self):
        '''测试用例 "hello" "world"'''
        print("test_002")
        result = add("hello", "world")
        print(result)
        expect = "helloworldworld"
        self.assertEqual(result, expect)

    def test_003(self):
        '''测试用例 0 0'''
        print("test_003")
        result = add(0, 0)
        print(result)
        expect = 0
        self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()
