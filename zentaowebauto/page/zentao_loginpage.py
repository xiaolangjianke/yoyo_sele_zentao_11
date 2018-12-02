from common.base import Base

login_url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"

class ZenLoginPage(Base):
    '''登录页面元素抓取'''
    loc_user = ("id", "account")
    loc_psw = ("css selector", "[name='password']")
    loc_keep = ("id", "keepLoginon")
    loc_login_button = ("id", "submit")
    loc_forget = ("link text", "忘记密码")

    def input_user(self, user):
        self.send(self.loc_user, user)

    def input_psw(self, psw):
        self.send(self.loc_psw, psw)

    def click_keep(self):
        self.click(self.loc_keep)

    def click_login_button(self):
        self.click(self.loc_login_button)

    def click_forget_psw(self):
        self.click(self.loc_forget)

    def login(self, user="admin", psw="123456", flog=False):
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        if flog:
            self.click_keep()
        self.click_login_button()

    def get_login_reslut(self):
        loc = ("css selector", "#userMenu>a")
        return self.get_text(loc, timeout=5)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    zen = ZenLoginPage(driver)
    driver.get(login_url)
    zen.login(flog=True)
    # zen.input_user("admin")
    # zen.input_psw("123456")
    # zen.click_keep()
    # zen.click_login_button()