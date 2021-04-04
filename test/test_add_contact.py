# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [ Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname", title="title",
                     company="company", address="address", home="home", mobile="mobile", email="email", email2="email2",
                     email3="email3", bday="bday", bmonth="bmonth",
                     byear="byear", address2="address2", phone2="phone2", notes="notes")] + [
    Contact(lastname=random_string("lastname", 15),
            firstname="" if private and bool(getrandbits(1)) else random_string("firstname", 10),
            middlename="" if private and bool(getrandbits(1)) else random_string("middlename", 15),
            nickname="" if private and bool(getrandbits(1)) else random_string("nickname", 10),
            title="" if private and bool(getrandbits(1)) else random_string("title", 20),
            company="" if private and bool(getrandbits(1)) else random_string("company", 30),
            address="" if private and bool(getrandbits(1)) else random_string("address", 50),
            home="" if phones and bool(getrandbits(1)) else random_string("phone_home", 15),
            mobile="" if phones and bool(getrandbits(1)) else random_string("mobile", 15),
            work="" if phones and bool(getrandbits(1)) else random_string("phone_work", 15),
            fax="" if phones and bool(getrandbits(1)) else random_string("fax", 15),
            email="" if emails and bool(getrandbits(1)) else random_string("email_main", 15),
            email2="" if emails and bool(getrandbits(1)) else random_string("email_secondary", 15),
            email3="" if emails and bool(getrandbits(1)) else random_string("email_other", 15),
            homepage="" if emails and bool(getrandbits(1)) else random_string("homepage", 15),
            byear="" if emails and bool(getrandbits(1)) else get_random_word(constant.SYMBOLS, randint(1, 4)),
            bmonth="-" if emails and bool(getrandbits(1)) else choice(constant.MONTHS),
            bday="" if emails and bool(getrandbits(1)) else str(randint(1, 31)),
            ayear="" if emails and bool(getrandbits(1)) else get_random_word(constant.SYMBOLS, randint(1, 4)),
            amonth="-" if emails and bool(getrandbits(1)) else choice(constant.MONTHS),
            aday="" if emails and bool(getrandbits(1)) else str(randint(1, 31)),
            address2="" if secondary and bool(getrandbits(1)) else random_string("address_secondary", 15),
            phone2="" if secondary and bool(getrandbits(1)) else random_string("phone_secondary", 15),
            notes="" if secondary and bool(getrandbits(1)) else random_string("notes", 15))
            for i in range(5)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(y) for y in testdata])
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