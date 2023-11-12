import os
import time
from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from selenium.webdriver.edge.service import Service as ServiceEdge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None


@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=ServiceEdge(EdgeChromiumDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.url = url
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     # set custom options only if none are provided from command line
#     if not config.option.htmlpath:
#         now = datetime.now()
#         # create report target dir
#         reports_dir = Path('reports', now.strftime('%Y_%m_%d'))
#         reports_dir.mkdir(parents=True, exist_ok=True)
#         # custom report file
#         report = reports_dir / f"report_{now.strftime('%H_%M')}.html"
#         # adjust plugin options
#         config.option.htmlpath = report
#         config.option.self_contained_html = True


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            ## only add additional html on failure test case
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = "../reports/screenshot/" + str(int(round(time.time() * 1000))) + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Automation Testing Report"
