from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeChat:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self.driver.quit()

    def swipe_find(self, text):
        while True:
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return element
            except:
                print("未找到，将继续滚动查找")
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def test_AddContact(self):
        name = "testName98"
        phone = "11112097054"
        self.driver.find_element_by_xpath("//*[contains(@text, '通讯录')]").click()
        addNum = self.swipe_find("添加成员")
        addNum.click()

        # # 自带的滚动查找
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        self.driver.find_element_by_xpath("//*[contains(@text, '手动输入添加')]").click()
        self.driver.find_element_by_xpath(
            "//*[contains(@text, '姓名')]/..//*[contains(@resource-id, 'com.tencent.wework:id/au0')]") \
            .send_keys(name)
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[contains(@resource-id, 'com.tencent.wework:id/aut')]") \
            .click()
        self.driver.find_element_by_xpath("//*[@text='女']").click()
        self.driver.find_element_by_xpath("//*[@text='手机号']").send_keys(phone)
        self.driver.find_element_by_xpath("//*[contains(@text, '保存')]").click()
        print(self.driver.page_source)
        print(self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)

    def searchContact(self, text):
        while True:
            try:
                elem = self.driver.find_element_by_xpath(f"//*[contains(@text, '{text}')]")
                elem.click()
                return elem
            except:
                self.driver.find_element_by_id("com.tencent.wework:id/guu").click()
                self.driver.find_element_by_id("com.tencent.wework:id/fk1").send_keys(f"{text}")
                sleep(3)
                elemlist = self.driver.find_elements_by_xpath(f"//*[@text='{text}']")
                print(elemlist)
                if len(elemlist) > 1:
                    elemlist[-1].click()
                    return elemlist

    def test_delContact(self):
        sea_text = "testName98"
        self.driver.find_element_by_xpath("//*[contains(@text, '通讯录')]").click()
        self.searchContact(f'{sea_text}')
        self.driver.find_element_by_id("com.tencent.wework:id/guk").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '编辑成员')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '删除成员')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '确定')]").click()
        elemlist = self.searchContact(f'{sea_text}')
        assert len(elemlist) == 1
