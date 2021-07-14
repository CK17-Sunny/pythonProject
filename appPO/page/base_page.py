from time import sleep

from appium import webdriver
import logging

# 基类，初始化driver, find, swipe_find
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):  # driver传递；指定类型为WebDriver；
        self.driver = driver

    def find(self, value):
        self.driver.find_element_by_xpath(value)

    def find_and_click(self, value):
        self.driver.find_element_by_xpath(value).click()

    def find_and_sendkey(self, value, key):
        self.driver.find_element_by_xpath(value).send_keys(key)

    def swipe_find(self, text):
        while True:
            try:
                element = self.driver.find_element_by_xpath(f"//*[@text='{text}']")
                return element
            except:
                print("未找到，将继续滚动查找")
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.2
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def searchContact(self, text):
        while True:
            try:
                elem = self.driver.find_element(MobileBy.XPATH, f"//*[contains(@text, '{text}')]")
                elem.click()
                return elem
            except:
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guu").click()
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fk1").send_keys(f"{text}")
                sleep(3)  # 强制等待，以保证要查找的所有元素都能显示出来，否则会报错
                elemlist = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{text}']")
                # return elemlist
                print(elemlist)  # 检查打印出来的elements个数，以保证返回的是列表形式
                if len(elemlist) > 1:
                    elemlist[1].click()
