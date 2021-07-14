from appPO.page.base_page import BasePage
from appPO.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    def addcontact_manual(self):
        self.find_and_click("//*[contains(@text, '手动输入添加')]")
        return EditContactPage(self.driver)
