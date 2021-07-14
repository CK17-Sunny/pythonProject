from appPO.page.base_page import BasePage


class EditContactPage(BasePage):
    def edit_contact(self, name, phone):
        self.find_and_sendkey(
            "//*[contains(@text, '姓名')]/..//*[contains(@resource-id, 'com.tencent.wework:id/au0')]", name)
        self.find_and_click("//*[@text='性别']/..//*[contains(@resource-id, 'com.tencent.wework:id/aut')]")
        self.find_and_click("//*[@text='女']")
        self.find_and_sendkey("//*[@text='手机号']", phone)
        self.find_and_click("//*[contains(@text, '保存')]")

    def verify_ok(self):
        print(self.find("//*[@text='添加成功']"))
