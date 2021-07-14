from appPO.page.base_page import BasePage
from appPO.page.verifyOK_page import VerifyOKPage


class DeleteConfirmPage(BasePage):
    def deleteConfirm(self):
        self.find_and_click("//*[contains(@text, '确定')]")

    def elemIsDeleted(self, sea_text):
        elemlist = self.searchContact(f'{sea_text}')
        assert len(elemlist) == 1
