import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IeOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, ie11 or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    elif browser_name == "ie11":
        options = IeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        print("\nstart ie11 browser for test..")
        browser = webdriver.Ie("C:\\IE11driver\\IEDriverServer.exe")

    browser.implicitly_wait(3)
    request.addfinalizer(browser.close)
    return browser
