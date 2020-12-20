from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="testfirstname2", middlename="testmiddlename2", lastname="testlastname2", mobilephone="70000000002"))
    app.session.logout()


def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="testfirstname3"))
    app.session.logout()


def test_edit_first_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(middlename="testmiddlename4"))
    app.session.logout()
