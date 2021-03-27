

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
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_home_page.secondaryphone == contact_from_edit_page.secondaryphone


