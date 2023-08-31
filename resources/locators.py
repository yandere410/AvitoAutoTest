from selenium.webdriver.common.by import By


class Locators:
    FAVOURITE = (By.CSS_SELECTOR, '.style-header-add-favorite-M7nA2 > button:nth-child(1)')
    HEART_LINK = (By.CSS_SELECTOR, '.desktop-1rdftp2 > svg:nth-child(1) > path:nth-child(1)')
    SEARCHABLE = (By.CSS_SELECTOR, '.styles-module-root-hwVld')