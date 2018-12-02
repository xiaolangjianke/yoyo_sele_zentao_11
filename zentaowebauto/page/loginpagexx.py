from selenium import webdriver
import time
from common.base import Base

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.b = Base(self.driver)

    def login(self, user="admin", psw="123456"):
        # driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        time.sleep(3)
        self.b.send("xpath", ".//*[@id='account']", "admin")
        self.b.send("css selector", "[name='password']", "123456")
        self.b.click("css selector", "#submit")

        # self.driver.find_element_by_xpath(".//*[@id='account']").send_keys(user)
        # self.driver.find_element_by_css_selector("[name='password']").send_keys(psw)
        # self.driver.find_element_by_css_selector("#submit").click()

    def get_login_reslut(self):
        # time.sleep(3)  # css_selector("#userMenu>a"
        self.b.get_text("css selector", "#userMenu>a", timeout=5)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    zen = LoginPage(driver)
    zen.login()
    result = zen.get_login_reslut()
    print(result)