# -*- coding: utf-8 -*-
from model.contact import Contact




def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="EditedIvan", middlename="EditedSergeevich", lastname="EditedPetrov", nickname="EditedButthead",
                            title="Editedtest", company="EditedGazprom", address="EditedMoscow", home="1111",
                            mobile="1111", work="1111", fax="1111",
                            email="Editedispetrov@mail.ru", email2="Editedispetrov2@mail.ru", email3="Editedispetrov3@mail.ru",
                            homepage="Editedwww.petrov.su", bday="3", bmonth="April", byear="1974", aday="9", amonth="May",
                            ayear="2000", address2="EditedMoscow", phone2="1111", notes="EditedTest"))
    app.session.logout()
