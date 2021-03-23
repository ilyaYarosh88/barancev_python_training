from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="Ivan", middlename="Sergeevich", lastname="Petrov", nickname="Butthead",
                                        title="test", company="Gazprom", address="Moscow", home="+74950000000",
                                        mobile="+79190000000", work="+74951000000", fax="+74952000000",
                                        email="ispetrov@mail.ru", email2="ispetrov2@mail.ru", email3="ispetrov3@mail.ru",
                                        homepage="www.petrov.su", bday="2", bmonth="April", byear="1973", aday="6", amonth="May",
                                        ayear="1999", address2="Moscow", phone2="1", notes="Test"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact_list) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact_list[index:index+1] = []
    assert old_contact_list == new_contact