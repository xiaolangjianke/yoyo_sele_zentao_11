import unittest
from selenium import webdriver
from page.zentao_loginpage import ZenLoginPage
from page.zentao_aboutpage import ZenAboutPage
import ddt
from common.read_excel import ExcelUtil

filepath = "testdata.xlsx"
data = ExcelUtil(filepath)
datas = data.dict_data()
print(datas)
# datas = [
#     {"user": "admin", "psw": "123456", "expect": True},
#     {"user": "admin2", "psw": "22222222222", "expect": False},
#     {"user": "admin3", "psw": "3333333333", "expect": False},
#     {"user": "admin4", "psw": "44444444", "expect": False},
#     {"user": "admin5", "psw": "555555555", "expect": False },
# ]



@ddt.ddt
class Test_about(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.zen = ZenLoginPage(self.driver)

    @ddt.data(*datas)
    def test_login_(self, test_data):
        user = test_data["user"]
        psw = test_data["psw"]
        exp = bool(test_data["expect"])  # bool
        print("测试数据：%s %s \n 期望结果：%s"%(user, psw, exp))
        self.zen.login(user, psw) # 先登录
        result = self.zen.get_login_reslut()
        if result == user:
            actul = True
        else:
            actul = False
        self.assertTrue(exp == actul)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()