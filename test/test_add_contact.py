# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", nickname="",
                        title="", company="", address="",
                        home="", mobile="", work="",
                        fax="", email="", email2="",
                        email3="", homepage="", address2="",
                        phone2="", notes="")] + [
                Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname",10),
                        title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
                        home=random_string("9190000000", 10), mobile=random_string("9190000000", 10), work=random_string("9190000000", 10),
                        fax=random_string("9190000000", 10), email=random_string("email@mail.im", 10), email2=random_string("email2@mail.im", 10),
                        email3=random_string("email@mail3.im", 10), homepage=random_string("www.homepage.ru", 10), address2=random_string("address2", 10),
                        phone2=random_string("phone2", 10), notes=random_string("notes", 10))
                for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# testdata = [
#     Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
#                       company=company, address=address, home=home, mobile=mobile, work=work, fax=fax, email=email, email2=email2,
#                       email3=email3, homepage=homepage, bday=bday, bmonth=bmonth,
#                       byear=byear, ayear=ayear, amonth=amonth, aday=aday, address2=address2, phone2=phone2, notes=notes)
#     for firstname in ["", random_string("firstname", 10)]
#     for lastname in ["" ,random_string("lastname", 15)]
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
#     for byear in ["", str(randint(1, 31))]
#     for bmonth in ["-", str(randint(1, 12))]
#     for bday in ["", random_string("bday", 20)]
#     for ayear in ["", random_string("ayear", 4)]
#     for amonth in ["", str(randint(1, 12))]
#     for aday in ["", str(randint(1, 31))]
#     for address2 in ["", random_string("title", 20)]
#     for phone2 in ["", random_string("title", 20)]
#     for notes in ["", random_string("title", 20)]]