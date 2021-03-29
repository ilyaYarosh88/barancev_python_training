# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(
            Contact(firstname="Ivan", middlename="Sergeevich", lastname="Petrov", nickname="Butthead", title="test",
                    company="Gazprom", address="Moscow", home="+74950000000", mobile="+79190000000",
                    work="+74951000000", fax="+74952000000", email="ispetrov@mail.ru", email2="ispetrov2@mail.ru",
                    email3="ispetrov3@mail.ru", homepage="www.petrov.su", bday="2", bmonth="April", byear="1973",
                    aday="6", amonth="May", ayear="1999", address2="Moscow", phone2="1", notes="Test"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact = Contact(firstname="EditedIvan", middlename="EditedSergeevich", lastname="EditedPetrov",
                      nickname="EditedButthead", title="Editedtest", company="EditedGazprom", address="EditedMoscow",
                      home="1111", mobile="1111", work="1111", fax="1111", email="Editedispetrov@mail.ru",
                      email2="Editedispetrov2@mail.ru", email3="Editedispetrov3@mail.ru",
                      homepage="Editedwww.petrov.su", bday="9", bmonth="May", byear="1974", aday="9", amonth="May",
                      ayear="2000", address2="EditedMoscow", phone2="1111", notes="EditedTest")
    contact.id = old_contact_list[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contact_list) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



