from appPO.page.base_page import BasePage
from appPO.page.deleteconfirm_page import DeleteConfirmPage


class DeleteContactPage(BasePage):
    def deleteContact(self):
        self.find_and_click("//*[contains(@text, '删除成员')]")
        return DeleteConfirmPage(self.driver)
