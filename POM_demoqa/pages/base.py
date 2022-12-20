from mydata import *

class BasePage(object):
    def __init__(self):
        self.base_URL = base_URL_DemoQA
        self.login_URL = self.base_URL + 'login'
        self.profile_URL = self.base_URL + "profile"
        self.books_URL = self.base_URL + "books"