from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="testname2", header="testheader2", footer="testfooter2"))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="testname3"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="testheader4"))
