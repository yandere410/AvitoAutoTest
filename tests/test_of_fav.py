from pages.item_page import Favourites


class TestFav:
     def test_choose_as_fav(self, driver):
        #Navigate to the desired page
        page = Favourites(driver)
        page.open()

        #Click on the favourite button
        page.choose_fav().click()

        #Navigate to favourites page
        page.to_favourites_page().click()

        #Check if the item has been added to favourites
        assert page.is_present_fav(), "The item is not present in favourites"
