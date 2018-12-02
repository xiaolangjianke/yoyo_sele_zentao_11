from selenium import webdriver
import time

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def login(self, user="admin", psw="123456"):
        # driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys(user)
        self.driver.find_element_by_css_selector("[name='password']").send_keys(psw)
        self.driver.find_element_by_css_selector("#submit").click()

    def get_login_reslut(self):
        time.sleep(3)
        try:
            a = self.driver.find_element_by_css_selector("#userMenu>a")
            t = a.text
            return t
        except:
            return ""

