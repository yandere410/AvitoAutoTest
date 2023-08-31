from resources.locators import Locators
from pages.item_page import Favourites


class TestFav:
     def test_choose_as_fav(self, driver):
        # Step 1: Navigate to the desired page
        page = Favourites(driver)
        page.open()

        # Step 2: Click on the favourite button
        page.choose_fav().click()

        # Step 3: Navigate to favourites page
        page.to_favourites_page().click()

        # Step 4: Check if the item has been added to favourites
        assert page.is_present_fav(), "The item is not present in favourites"




