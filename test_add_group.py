# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group
from application import Application
class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):

        self.app.login(username="admin", password="secret")
        self.app.create_group(wd, Group(name="testName", header="testHeader", footer="testFooter"))
        self.app.logout()

    def test_add_empty_group(self):

        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
