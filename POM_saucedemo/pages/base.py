from mydata import *

class BasePage(object):
    def __init__(self):
        self.base_url = base_URL_Sauce
        self.inventory_url = self.base_url + 'inventory.html'
        self.cart_url = self.base_url + 'cart.html'
        self.checkout_one_url = self.base_url + 'checkout-step-one.html'
        self.checkout_two_url = self.base_url + 'checkout-step-two.html'
        self.checkout_final_url = self.base_url + 'checkout-complete.html'