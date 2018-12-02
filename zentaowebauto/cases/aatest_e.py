from selenium import webdriver
import unittest
import time

'''
self 1.全局参数
'''
class ZenTaoLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # 前置
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")

    def tearDown(self):
        self.driver.delete_all_cookies()  # 退出登陆

    def test_login_1(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys("admin")
        self.driver.find_element_by_css_selector("[name='password']").send_keys("123456")
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)    # 页面有跳转
        # 实际结果
        a = self.driver.find_element_by_css_selector("#userMenu>a")
        t = a.text
        self.assertEqual(t, "admin")

    def test_login_2(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys("admin111")
        self.driver.find_element_by_css_selector("[name='password']").send_keys("123456111")
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)    # 页面有跳转
        # 实际结果
        try:
            a = self.driver.find_element_by_css_selector("#userMenu>a")
            t = a.text
        except:
            t = ""
        self.assertNotEqual(t, "admin")

if __name__ == '__main__':
    unittest.main()