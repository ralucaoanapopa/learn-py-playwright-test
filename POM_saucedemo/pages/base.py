from mydata import *

class BasePage(object):
    def __init__(self):
        self.base_url = base_URL_Sauce
        self.inventory_url = self.base_url + 'inventory.html'