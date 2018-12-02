import unittest
from selenium import webdriver
from page.zentao_loginpage import ZenLoginPage
from page.zentao_aboutpage import ZenAboutPage
import time


testdatas = [
    (0, "判断文本"),
    (5, "判断文本"),
    (6, "判断文本"),
]


class Test_about(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.zen = ZenLoginPage(cls.driver)
        cls.ab = ZenAboutPage(cls.driver)
        cls.zen.login() # 先登录

    def setUp(self):
        self.driver.get("http://127.0.0.1:81/zentao/my/")
        self.ab.click_about() # 关于页面

    def about_click_link(self, no=0, _text=""):
        # -----点击流程------
        h1 = self.driver.current_window_handle
        time.sleep(3)
        self.ab.swith_iframe()
        # 点 商业技术支持
        self.ab.click_link_no(no)
        time.sleep(3)
        h2 = self.driver.window_handles
        self.driver.switch_to.window(h2[-1])
        t = self.driver.title
        print("当前打开页面：%s"%t)

        # 判断元素存在
        x = ("xpath", ".//*[contains(text(), '%s')]" % _text)
        result = self.ab.is_element_exist(x)
        print(result)
        self.driver.close() # 关闭新开的窗口
        self.driver.switch_to.window(h1)
        return result  # 返回结果
        # assert result == True
        # self.assertTrue(result)

    def test_ab_1(self):
        r1 = self.about_click_link(5, "服务介绍")
        self.assertTrue(r1)

    def test_2(self):
        r2 = self.about_click_link(6, "选择适合您的安装方法")
        self.assertTrue(r2)




if __name__ == '__main__':
    unittest.main()