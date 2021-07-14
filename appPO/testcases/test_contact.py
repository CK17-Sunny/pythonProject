from appPO.page.app import App


class TestContact:
    def setup(self):
        self.app = App().start()
        # self.main = App().goto_main()  # app.py类的start()函数，如果不return self
        self.main = self.app.goto_main()  # return self后

    def teardown(self):
        self.app.stop()

    def test_contact(self):
        name = "testName90"
        phone = "11112098903"
        editpage = self.main.goto_addresslist().goto_addContact().addcontact_manual()
        editpage.edit_contact(name, phone)
        editpage.verify_ok()
