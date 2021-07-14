from appPO.page.base_page import BasePage


class VerifyOKPage(BasePage):
    def elemIsDeleted(self, sea_text):
        elemlist = self.searchContact(f'{sea_text}')
        assert len(elemlist) == 1
