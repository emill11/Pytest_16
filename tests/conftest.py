import pytest
from selene import browser


@pytest.fixture(params=[(3000, 2000), (1500, 1000)], scope='function')
def github_desktop(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(params=[(200, 400), (300, 500)], scope='function')
def github_mobile(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(params=[(3000, 2000), (400, 800)],
                scope='function')
def github_desktop_mobile_size(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()
