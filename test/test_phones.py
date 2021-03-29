import re


    # в метод передается фикстура
    # фикстура инициализирует объект класса application
    # там имеется ссылка на контакт хелпер из него мы будем получать информацию
    # тест проверяет инф. о телефонах на главной совпадает с информацией из формы редактирования
def test_phones_on_home_page(app):
    # Проверку делаем для первого контакта [0]
    # Сохраняем его в переменную
    contact_from_home_page = app.contact.get_contact_list()[0]
    # Получаем информацию о контакте из формы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравниваем объекты между собой
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    #для замены нам нужны рег.выражения
    #в методе саб сначала указываем шаблон(что заменяем), потом указываем на что меняем, где заменять
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile, contact.phone2]))))



