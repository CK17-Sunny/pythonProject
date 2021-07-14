from time import sleep

from appPO.page.base_page import BasePage
from appPO.page.searchresult_page import SearchResultPage


class Searchlist_page(BasePage):
    def goto_searchContact(self, sea_text):
        self.searchContact(sea_text)
        # elem = self.searchContact(f'{sea_text}')
        # print(elem)
        # if len(elem) > 1:
        #     elem[1].click()
        return SearchResultPage(self.driver)
