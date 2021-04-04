# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="")] + [
               Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10))
               for i in range(5)
           ]
# testdata = [
#     Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
#                      company=company, address=address, home=home, mobile=mobile, email=email, email2=email2,
#                      email3=email3, bday=bday, bmonth=bmonth,
#                      byear=byear, address2=address2, phone2=phone2, notes=notes)
#     for lastname in ["" ,random_string("lastname", 15)]
#     for firstname in ["", random_string("firstname", 10)]
#     for middlename in ["", random_string("middlename", 15)]
#     for nickname in ["", random_string("nickname", 10)]
#     for title  in ["", random_string("title", 20)]
#     for company in ["", random_string("company", 20)]
#     for address in ["", random_string("address", 20)]
#     for home in ["", random_string("home", 20)]
#     for mobile in ["", random_string("mobile", 20)]
#     for work in ["", random_string("work", 20)]
#     for fax in ["", random_string("fax", 20)]
#     for email in ["", random_string("email", 20)]
#     for email2 in ["", random_string("email2", 20)]
#     for email3 in ["", random_string("email3", 20)]
#     for homepage in ["", random_string("homepage", 20)]
#     for byear in ["", random_string("byear", 20)]
#     for bmonth in ["-", choice(constant.MONTHS)]
#     for bday in ["", str(randint(1, 31))]
#     for ayear in ["", get_random_word(constant.SYMBOLS, randint(1, 4)),
#     for amonth in ["-", choice(constant.MONTHS)]
#     for aday in ["", str(randint(1, 31)]
#     for address2 in ["", random_string("title", 20)]]
#     for phone2 in ["", random_string("title", 20)]
#     for notes in ["", random_string("title", 20)]
# ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Sergeevich", lastname="Petrov", nickname="Butthead", title="test",
                      company="Gazprom", address="Moscow", home="+74950000000", mobile="+79190000000",
                      work="+74951000000", fax="+74952000000", email="ispetrov@mail.ru", email2="ispetrov2@mail.ru",
                      email3="ispetrov3@mail.ru", homepage="www.petrov.su", bday="2", bmonth="April", byear="1973",
                      aday="6", amonth="May", ayear="1999", address2="Moscow", phone2="+5", notes="Test")
    app.contact.add_contact(contact)

    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)