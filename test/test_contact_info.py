from model.contact import Contact
from random import randrange
import re


def test_contact_info_on_main_page(app):
    if app.contact.count() == 0:
        app.contact.add_contact(
            Contact(firstname="Ivan", middlename="Sergeevich", lastname="Petrov", nickname="Butthead", title="test",
                    company="Gazprom", address="Moscow", home="+74950000000", mobile="+79190000000",
                    work="+74951000000", fax="+74952000000", email="ispetrov@mail.ru", email2="ispetrov2@mail.ru",
                    email3="ispetrov3@mail.ru", homepage="www.petrov.su", bday="2", bmonth="April", byear="1973",
                    aday="6", amonth="May", ayear="1999", address2="Moscow", phone2="1", notes="Test"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))