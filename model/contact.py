from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None,
                 address=None, address2=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 email=None, email2=None, email3=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.address2 = address2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.middlename, self.email, self.mobilephone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
