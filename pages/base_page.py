import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver: webdriver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_element_alternate(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_element_is_visible(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_is_invisible(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(locator))

    def wait_for_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_url(self, excepted_url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(excepted_url))

    def check_element_is_visible(self, locator):
        #self.wait_for_element_is_visible(locator)
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    def check_element_is_focused(self, locator):
        element = self.driver.find_element(*locator)
        is_focused = self.driver.execute_script("return document.activeElement === arguments[0];", element)
        return is_focused

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)

        # JavaScript для перетаскивания
        self.driver.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            source_element,
            target_element
        )

    def find_text_on_page(self, text):
        text_to_find = text
        result = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text_to_find}')]").text
        return result

    def wait_for_text_change(self, locator, initial_text):
        WebDriverWait(self.driver, 10).until(lambda driver_wait: self.driver.find_element(*locator).text != initial_text)
