from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="testname2", header="testheader2", footer="testfooter2"))
    app.session.logout()


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="testname3"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="testheader4"))
    app.session.logout()