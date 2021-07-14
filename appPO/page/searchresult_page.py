from appium.webdriver.common.mobileby import MobileBy

from appPO.page.base_page import BasePage
from appPO.page.editscontact_page import EditSContactPage


class SearchResultPage(BasePage):
    def goto_clickdot(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guk").click()
        return EditSContactPage(self.driver)
