from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="testfirstname2", middlename="testmiddlename2", lastname="testlastname2", mobilephone="70000000002"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="testfirstname3"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(middlename="testmiddlename4"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

