import pytest
from selenium import webdriver
import logging
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IeOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browsermobproxy import Server, Client
import urllib.parse
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="test.log")


class ScreenshotListener(AbstractEventListener):

    def before_click(self, element, driver):
        logging.info(f"I'm clicking {element}")

    def after_click(self, element, driver):
        logging.info(f"I've clicked {element}")

    def before_find(self, by, value, driver):
        logging.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        logging.info(f"I've found '{value}' with '{by}'")

    def before_quit(self, driver):
        logging.info(f"I'm getting ready to terminate {driver}")

    def after_quit(self, driver):
        logging.info(f"Driver closed.")

    def on_exception(self, exception, driver):
        logger.error(f'Oooops i got: {exception}')
        logger.info(f'Saved screenshot: {driver.title}.png')
        driver.save_screenshot(f'{driver.title}.png')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, ie11 or firefox")


@pytest.fixture
def proxy_server(request):
    server = Server("browsermob-proxy/bin/browsermob-proxy")
    server.start()
    time.sleep(1)
    client = Client("localhost:8080")
    time.sleep(1)
    server.create_proxy()
    request.addfinalizer(server.stop)
    client.new_har()
    return client


@pytest.fixture(scope="function")
def browser(request, proxy_server):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        caps = DesiredCapabilities.CHROME
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless")
        options.add_experimental_option('w3c', False)
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}

        # proxy
        proxy_url = urllib.parse.urlparse(proxy_server.proxy).path
        print("\nstart chrome browser for test..")
        browser = EventFiringWebDriver(webdriver.Chrome(
            options=options, desired_capabilities=caps
        ), ScreenshotListener())

        #browser.proxy = proxy_server

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        print("\nstart firefox browser for test..")
        browser = EventFiringWebDriver(webdriver.Firefox(options=options), ScreenshotListener())
    elif browser_name == "ie11":
        options = IeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        print("\nstart ie11 browser for test..")
        browser = webdriver.Ie("C:\\IE11driver\\IEDriverServer.exe")

    request.addfinalizer(browser.close)
    return browser
