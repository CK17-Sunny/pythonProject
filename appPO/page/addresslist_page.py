from appPO.page.addcontact_page import AddContactPage
from appPO.page.base_page import BasePage


class AddressListPage(BasePage):
    def goto_addContact(self):
        addNum = self.swipe_find("添加成员")
        addNum.click()
        return AddContactPage(self.driver)
