import unittest
from selenium import webdriver
import time
from page.loginpagexx import LoginPage
from page.addbugpage import AddBug

class TestAddBug(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.zen = LoginPage(self.driver)
        self.zen.login()  # 先登录
        self.add = AddBug(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_bug_1(self):
        '''测试提交BUG流程'''
        timestr = str(time.time())
        self.add.add_bug(timestr)  # 提交BUG流程
        # 获取结果
        result = self.add.get_bug_list_title_text()
        print(result)
        self.assertEqual(result, "测试的标题:"+ timestr)



if __name__ == '__main__':
    unittest.main()