# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(Contact(firstname="testfirstname", middlename="testmiddlename", lastname="testlastname", mobilephone="70000000000"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)

def test_add_empty_contact(app):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(Contact(firstname="", middlename="", lastname="", mobilephone=""))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)

