from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = ("https://www.avito.ru/nikel/"
                         "knigi_i_zhurnaly/domain-driven"
                         "_design_distilled_vaughn_vernon_2639542363")

    # timings elements funcitons
    def find_element(self, locator, time=100):
        return WebDriverWait(
            self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=100):
        return WebDriverWait(
            self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def open(self):
        return self.driver.get(self.base_url)

    # requirements check
    def is_element_present(self, locator):
        try:
            self.find_element(locator)
        except(NoSuchElementException):
            return False
        return True
