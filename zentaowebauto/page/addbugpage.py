from selenium import webdriver
import time
from common.base import Base
class AddBug(Base):
    loc_test = ("xpath", "//*[@data-id='qa']/a")   # locator
    loc_bug = ("xpath", ".//*[@id='modulemenu']/ul/li[2]/a")
    loc_tibug = ("css selector", "#createActionMenu>a")
    loc_yxbb = ("class name", "default")
    loc_truck = ("css selector", ".active-result.highlighted")
    loc_biaoti = ("id", "title")
    loc_iframe = ("class name", "ke-edit-iframe")
    loc_body = ("class name", "article-content")
    loc_save = ("id", "submit")

    loc_bug_list = ("xpath", ".//*[@id='bugList']/tbody/tr/td[4]/a")
    loc_bug_first = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def add_bug(self, timestr):
        self.click(*self.loc_test)
        self.click(*self.loc_bug)
        self.click(*self.loc_tibug)  #
        self.click(*self.loc_yxbb)
        self.click(*self.loc_truck)
        self.send(*self.loc_biaoti, text="测试的标题:%s" %timestr)
        frame = self.find(*self.loc_iframe)
        self.driver.switch_to.frame(frame)
        self.send(*self.loc_body, text="body正文")
        self.driver.switch_to.default_content()
        self.click(*self.loc_save)

    def get_bug_list_title_text(self):
        self.driver.get("http://127.0.0.1:81/zentao/bug-browse-1.html")
        try:
            all_title = self.finds(*self.loc_bug_list)
            print(all_title)
            t1 = all_title[0].text  # list out of range
            return t1
        except:
            return ""

    def new_get_text(self,  _text):
        r = self.is_text_in_element(self.loc_bug_first, _text=_text)
        return r


if __name__ == '__main__':
    driver = webdriver.Firefox()
    from page.loginpagexx import LoginPage
    zen = LoginPage(driver)
    zen.login()
    add = AddBug(driver)

    timestr = str(time.time())
    add.add_bug(timestr)

    result = add.get_bug_list_title_text()
    print(result)

    r1 = add.new_get_text("测试的标题:"+timestr)
    print("新方法的结果： %s"%r1)
    # assert result == "测试的标题:"+timestr









