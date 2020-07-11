import pytest
from selenium import webdriver
import logging
from selenium.webdriver.support.events import AbstractEventListener
import allure

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


# def pytest_addoption(parser):
#     parser.addoption('--browser', action='store', default="chrome",
#                      help="Choose browser: chrome, ie11 or firefox")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox", "opera", "yandex"])
    parser.addoption("--executor", action="store", default="192.168.56.1")
#
#
@pytest.fixture
def firefox(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def chrome(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                          desired_capabilities={"browserName": browser})  # "platform": "linux"
    browser.maximize_window()
    def fin():
        try:
            allure.attach(name=browser.session_id,
                          body=str(browser.desired_capabilities),
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(name="chrome log",
                          body=browser.get_log('browser'),
                          attachment_type=allure.attachment_type.TEXT)
        except TypeError as e:
            print(e)
        finally:
            browser.quit()

    request.addfinalizer(fin)
    return browser


# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("--browser")
#     if browser_name == "chrome":
#         options = ChromeOptions()
#         options.add_argument("--start-maximized")
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument("--headless")
#         d = DesiredCapabilities.CHROME
#         d['loggingPrefs'] = {'browser': 'ALL'}
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome(options=options, desired_capabilities=d)
#     elif browser_name == "firefox":
#         options = FirefoxOptions()
#         options.add_argument("--start-maximized")
#         # options.add_argument("--headless")
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox(options=options)
#     elif browser_name == "ie11":
#         options = IeOptions()
#         options.add_argument("--start-maximized")
#         options.add_argument("--headless")
#         print("\nstart ie11 browser for test..")
#         browser = webdriver.Ie("C:\\IE11driver\\IEDriverServer.exe")
#
#     def fin():
#         try:
#             allure.attach(name=browser.session_id,
#                           body=str(browser.desired_capabilities),
#                           attachment_type=allure.attachment_type.JSON)
#             allure.attach(name="chrome log",
#                           body=browser.get_log('browser'),
#                           attachment_type=allure.attachment_type.TEXT)
#         except TypeError as e:
#             print(e)
#         finally:
#             browser.quit()
#
#     request.addfinalizer(fin)
#     return browser
