from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="testfirstname2", middlename="testmiddlename2", lastname="testlastname2", mobilephone="70000000002"))


def test_edit_first_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="testfirstname3"))


def test_edit_first_contact_middlename(app):
    app.contact.edit_first_contact(Contact(middlename="testmiddlename4"))

