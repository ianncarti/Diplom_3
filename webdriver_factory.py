from selenium import webdriver


class WebdriverFactory:

    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == 'firefox':
            return webdriver.Firefox()
        elif browser_name == 'chrome':
            return webdriver.Chrome()
        else:
            raise ValueError(f"Неподдерживаемый тип браузера: {browser_name}")
