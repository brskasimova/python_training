# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", mobilephone="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15), lastname=random_string("lastname", 15),
            address=random_string("address", 15), address2=random_string("address2", 15),
            email=random_string("1@1.", 10), email2=random_string("2@2.", 15), email3=random_string("email", 20),
            homephone=random_string("+7", 10), mobilephone=random_string("7", 10), workphone=random_string("8", 10), secondaryphone=random_string("7000", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
