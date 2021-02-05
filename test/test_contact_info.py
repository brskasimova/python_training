from model.contact import Contact
import re
from random import randrange


def test_contact_info_home_vs_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testfirstname3", middlename="testmiddlename3", lastname="testlastname3",
                      homephone="73000000000", mobilephone="73000000001", workphone="73000000002", address="test address 1",
                      secondaryphone="73000000003", email="3email@mail.ru", email2="3email2@mail.ru", email3="3email3@mail.ru"))
    for index in range(len(db.get_contact_list())):
        contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[index]
        contact_from_db = db.get_contact_list()[index]
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_from_home_page(contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_from_home_page(contact_from_db)


def test_contact_info_home_vs_edit(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testfirstname3", middlename="testmiddlename3", lastname="testlastname3",
                      homephone="73000000000", mobilephone="73000000001", workphone="73000000002", address="test address 1",
                      secondaryphone="73000000003", email="3email@mail.ru", email2="3email2@mail.ru", email3="3email3@mail.ru"))
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_from_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_from_home_page(contact_from_edit_page)


def test_contact_info_home_vs_view(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testfirstname3", middlename="testmiddlename3", lastname="testlastname3",
                      homephone="73000000000", mobilephone="73000000001", workphone="73000000002",
                      secondaryphone="73000000003", email="3email@mail.ru", email2="3email2@mail.ru", email3="3email3@mail.ru"))
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[./() -]", "", s)


def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))