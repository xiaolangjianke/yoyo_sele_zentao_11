from common.base import Base

class ZenAboutPage(Base):
    '''登录页面元素抓取'''
    loc_about_1 = ("id", "proversion")
    loc_about_2 = ("id", "official")
    loc_about_3 = ("id", "changelog")
    loc_about_4 = ("id", "license")
    loc_about_5 = ("id", "extension")

    # 技术支持
    loc_jszc = ("xpath", ".//*[@class='card-content']/ul/li/a")

    # loc_jszc = ("css selector", ".card-content>ul>li>a")

    loc_about = ("link text", "关于")

    loc_iframe = ("id", "modalIframe")

    def swith_iframe(self):
        self.swith_frame(self.loc_iframe)

    def click_about(self):
        self.click(self.loc_about)

    def click_link_no(self, n=0):
        # 定位一组，选下标去点击
        all = self.finds(self.loc_jszc)
        all[n].click()

    def click_about1(self):
        self.click(self.loc_about_1)

    def click_about2(self):
        self.click(self.loc_about_2)

    def click_about3(self):
        self.click(self.loc_about_3)

    def click_about4(self):
        self.click(self.loc_about_4)

    def click_about5(self):
        self.click(self.loc_about_5)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    ab = ZenAboutPage(driver)

    # 先登录
    from page.zentao_loginpage import ZenLoginPage
    zen = ZenLoginPage(driver)
    zen.login()

    ab.click_about()

    # -----点击流程------
    h1 = driver.current_window_handle
    ab.swith_iframe()
    # 点 商业技术支持
    ab.click_link_no(5)
    h2 = driver.window_handles
    driver.switch_to.window(h2[-1])
    t = driver.title

    # 判断元素存在
    x = ("xpath", ".//*[contains(text(), '服务介绍')]")
    result = ab.is_element_exist(x)
    print(result)
    driver.close() # 关闭新开的窗口
    driver.switch_to.window(h1)
    assert result == True







