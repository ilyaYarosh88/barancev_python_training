from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact firm
        self.fill_contact_firms(contact)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # edit contact firm
        self.fill_contact_firms(contact)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
         wd = self.app.wd
         if text is not None:
             wd.find_element_by_name(field_name).click()
             wd.find_element_by_name(field_name).clear()
             wd.find_element_by_name(field_name).send_keys(text)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.get("http://localhost/addressbook/")


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

   # def fill_contact_firms(self, contact):
   #     wd = self.app.wd
   #     # Fill contact firms
   #     wd.find_element_by_name("firstname").click()
   #     wd.find_element_by_name("firstname").clear()
   #     wd.find_element_by_name("firstname").send_keys(contact.firstname)
   #     wd.find_element_by_name("middlename").click()
   #     wd.find_element_by_name("middlename").send_keys(contact.middlename)
   #     wd.find_element_by_name("lastname").click()
   #     wd.find_element_by_name("lastname").clear()
   #     wd.find_element_by_name("lastname").send_keys(contact.lastname)
   #     wd.find_element_by_name("nickname").click()
   #     wd.find_element_by_name("nickname").send_keys(contact.nickname)
   #     wd.find_element_by_name("title").click()
   #     wd.find_element_by_name("title").clear()
   #     wd.find_element_by_name("title").send_keys(contact.title)
   #     wd.find_element_by_name("company").click()
   #     wd.find_element_by_name("company").send_keys(contact.company)
   #     wd.find_element_by_name("address").click()
   #     wd.find_element_by_name("address").clear()
   #     wd.find_element_by_name("address").send_keys(contact.address)
   #     wd.find_element_by_name("home").click()
   #     wd.find_element_by_name("home").clear()
   #     wd.find_element_by_name("home").send_keys(contact.home)
   #     wd.find_element_by_name("mobile").click()
   #     wd.find_element_by_name("mobile").clear()
   #     wd.find_element_by_name("mobile").send_keys(contact.mobile)
   #     wd.find_element_by_name("work").click()
   #     wd.find_element_by_name("work").send_keys(contact.work)
   #     wd.find_element_by_name("fax").click()
   #     wd.find_element_by_name("fax").send_keys(contact.fax)
   #     wd.find_element_by_name("email").clear()
   #     wd.find_element_by_name("email").send_keys(contact.email)
   #     wd.find_element_by_name("email2").click()
   #     wd.find_element_by_name("email2").clear()
   #     wd.find_element_by_name("email2").send_keys(contact.email2)
   #     wd.find_element_by_name("email3").click()
   #     wd.find_element_by_name("email3").clear()
   #     wd.find_element_by_name("email3").send_keys(contact.email3)
   #     wd.find_element_by_name("homepage").click()
   #     wd.find_element_by_name("homepage").clear()
   #     wd.find_element_by_name("homepage").send_keys(contact.homepage)
   #     wd.find_element_by_name("bday").click()
   #     Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
   #     wd.find_element_by_name("bday").click()
   #     wd.find_element_by_name("bmonth").click()
   #     Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
   #     wd.find_element_by_name("bmonth").click()
   #     wd.find_element_by_name("byear").click()
   #     wd.find_element_by_name("byear").clear()
   #     wd.find_element_by_name("byear").send_keys(contact.byear)
   #     wd.find_element_by_name("aday").click()
   #     Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
   #     wd.find_element_by_name("aday").click()
   #     wd.find_element_by_name("amonth").click()
   #     Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
   #     wd.find_element_by_name("amonth").click()
   #     wd.find_element_by_name("ayear").click()
   #     wd.find_element_by_name("ayear").clear()
   #     wd.find_element_by_name("ayear").send_keys(contact.ayear)
   #     wd.find_element_by_name("address2").click()
   #     wd.find_element_by_name("address2").clear()
   #     wd.find_element_by_name("address2").send_keys(contact.address2)
   #     wd.find_element_by_name("phone2").click()
   #     wd.find_element_by_name("phone2").clear()
   #     wd.find_element_by_name("phone2").send_keys(contact.phone2)
   #     wd.find_element_by_name("notes").click()
   #     wd.find_element_by_name("notes").clear()
   #     wd.find_element_by_name("notes").send_keys(contact.notes)
    def fill_contact_firms(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

        self.change_field_value_date("bday", contact.bday)
        self.change_field_value_date("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

        self.change_field_value_date("aday", contact.aday)
        self.change_field_value_date("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                #так как в ячейке телефонов отдельные телефоны не указаны приходится получать информацию по всей ячейке а потом порезать её на части
                all_phones = cells[5].text #теперь это список телефонов у ячейки берём текст а потом делим его на телефоны
                # и мы можем этот список использовать что бы заполнить свойства объекта contact
                all_emails = cells[4].text
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones,
                            all_emails_from_home_page=all_emails))


        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        #открываем форму редактирования по заданному индексу
        self.open_contact_to_edit_by_index(index)
        #из формы читаем информацию
        firstname = wd.find_element_by_name("firstname").get_attribute("value")#текст который мы видим в поле является значением аттрибута value
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        # Строим объект из полученных данных, сначала название параметра а потом название локальной переменной
        return Contact(firstname=firstname, lastname=lastname, home=home, mobile=mobile, work=work, phone2=phone2,
                       id=id, email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        #вытаскиваем текст
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)

        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def change_field_value_date(self, field_date, text):
        wd = self.app.wd
        if text is not None:
            selector = Select(wd.find_element_by_name(field_date))
            selector.select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)