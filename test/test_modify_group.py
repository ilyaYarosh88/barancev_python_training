# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name", header="Header", footer="Footer"))
    app.group.modify_first_group(Group(name="EditedGroup", header="EditedHeader", footer="EditedFooter"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name", header="Header", footer="Footer"))
    app.group.modify_first_group(Group(header="New header"))
