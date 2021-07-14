from appPO.page.app import App


class TestdeleteContact:
    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop()

    def test_deleteContact(self):
        sea_text = "testName98"
        deletepage = self.main.goto_searchlist().goto_searchContact(sea_text).goto_clickdot() \
            .goto_editscontact().deleteContact()
        deletepage.deleteConfirm()
        deletepage.elemIsDeleted(sea_text)
