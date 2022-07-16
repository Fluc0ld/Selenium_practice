from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(
            driver,
            timeout=15,
            poll_frequency=0.3,
            ignored_exceptions=StaleElementReferenceException
        )

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return locating[find_by]

    def is_visible(self, find_by, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by),
                                                                   locator)), locator_name)

    def is_present(self, find_by, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by),
                                                                 locator)), locator_name)

    def is_not_present(self, find_by, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by),
                                                                     locator)), locator_name)

    def are_visible(self, find_by, locator: str, locator_name: str = None) -> list[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by),
                                                                        locator)), locator_name)

    def are_present(self, find_by, locator: str, locator_name: str = None) -> list[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by),
                                                                      locator)), locator_name)

    def get_text_from_webelements(self, elements: list[WebElement]) -> list[str]:
        return [element.text for element in elements]

    def get_elements_by_text(self, elements: list[WebElement], name: str) -> WebElement:
        name = name.lower()
        # return [element for element in elements if element.text.lower() == name][0]
        for element in elements:
            if element.text.lower() == name:
                return element

    def delete_cookie(self, cookie_name: str) -> None:
        self.driver.delete_cookie(cookie_name)
