from appPO.page.base_page import BasePage
from appPO.page.deletecontact_page import DeleteContactPage


class EditSContactPage(BasePage):
    def goto_editscontact(self):
        self.find_and_click("//*[contains(@text, '编辑成员')]")
        return DeleteContactPage(self.driver)
