from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="testname2", header="testheader2", footer="testfooter2"))
    app.session.logout()
