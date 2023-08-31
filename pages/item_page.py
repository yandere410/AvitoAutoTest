from pages.base_page import BasePage
from resources.locators import Locators


class Favourites(BasePage):
    def choose_fav(self):
        return self.find_element(Locators.FAVOURITE)

    def to_favourites_page(self):
        return self.find_element(Locators.HEART_LINK)

    def is_present_fav(self):
        return self.find_element(Locators.SEARCHABLE)
    