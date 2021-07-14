import yaml
from appium import webdriver

from appPO.page.base_page import BasePage
from appPO.page.main_page import MainPage

with open("../datas/caps.yml") as f:
    data = yaml.safe_load(f)
    desires = data["desireCaps"]
    ip = data["server"]["ip"]
    port = data["server"]["port"]


class App(BasePage):
    def start(self):
        if self.driver == None:
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

        return self  # 方便调用这个类自身的方法，如 goto_main()

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self):
        return MainPage(self.driver)  # driver传递；return到其它类
