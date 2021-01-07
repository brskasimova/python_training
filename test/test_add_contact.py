# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="testfirstname", middlename="testmiddlename", lastname="testlastname",
                          address="test address 1", address2="test address 2",
                          email="email@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru",
                          homephone="70000000000", mobilephone="70000000001", workphone="70000000002", secondaryphone="70000000003")
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#        old_contacts = app.contact.get_contact_list()
#        contact = Contact(firstname="", middlename="", lastname="", mobilephone="")
#        app.contact.create(contact)
#        new_contacts = app.contact.get_contact_list()
#        assert len(old_contacts) + 1 == len(new_contacts)
#        old_contacts.append(contact)
#        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
