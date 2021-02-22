# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):

    app.group.modify_first_group(Group(name="EditedGroup", header="EditedHeader", footer="EditedFooter"))
    app.session.logout()

def test_modify_group_header(app):

    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()