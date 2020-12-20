# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
        app.contact.create(Contact(firstname="testfirstname", middlename="testmiddlename", lastname="testlastname", mobilephone="70000000000"))


def test_add_empty_contact(app):
        app.contact.create(Contact(firstname="", middlename="", lastname="", mobilephone=""))

