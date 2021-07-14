from appPO.page.Searchlist_page import Searchlist_page
from appPO.page.addresslist_page import AddressListPage
from appPO.page.base_page import BasePage


class MainPage(BasePage):  # 页面； 继承通用的BasePage类
    def goto_addresslist(self):  # 页面主要功能， 新增联系人
        self.find_and_click("//*[contains(@text, '通讯录')]")
        return AddressListPage(self.driver)

    def goto_searchlist(self):  # 删除联系人
        # self.driver.find_element_by_xpath("//*[contains(@text, '通讯录')]").click()
        self.find_and_click("//*[contains(@text, '通讯录')]")
        return Searchlist_page(self.driver)
