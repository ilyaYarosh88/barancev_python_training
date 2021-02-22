# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):

    app.contact.create(Contact(firstname="Ivan", middlename="Sergeevich", lastname="Petrov", nickname="Butthead",
                            title="test", company="Gazprom", address="Moscow", home="+74950000000",
                            mobile="+79190000000", work="+74951000000", fax="+74952000000",
                            email="ispetrov@mail.ru", email2="ispetrov2@mail.ru", email3="ispetrov3@mail.ru",
                            homepage="www.petrov.su", bday="2", bmonth="April", byear="1973", aday="6", amonth="May",
                            ayear="1999", address2="Moscow", phone2="1", notes="Test"))
    app.session.logout()



