# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

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