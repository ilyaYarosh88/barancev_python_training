# -*- coding: utf-8 -*-
from model.contact import Contact




def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list
    contact = Contact(firstname="Ivan", middlename="Sergeevich", lastname="Petrov", nickname="Butthead",
                            title="test", company="Gazprom", address="Moscow", home="+74950000000",
                            mobile="+79190000000", work="+74951000000", fax="+74952000000",
                            email="ispetrov@mail.ru", email2="ispetrov2@mail.ru", email3="ispetrov3@mail.ru",
                            homepage="www.petrov.su", bday="2", bmonth="April", byear="1973", aday="6", amonth="May",
                            ayear="1999", address2="Moscow", phone2="1", notes="Test")
    app.contact.add_contact(contact)
    new_contact = app.contact.get_contact_list
    assert len(old_contact_list) + 1 == len(new_contact)
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)