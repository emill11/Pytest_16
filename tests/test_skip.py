import pytest
from selene import browser


def test_github_desktop(github_desktop_mobile_size):
    if browser.config.window_width == 400 and browser.config.window_height == 800:
        pytest.skip("Передано значение мобильного")
    else:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()


def test_open_github_sign_in_page_mobile(github_desktop_mobile_size):
    if browser.config.window_width == 3000 and browser.config.window_height == 2000:
        pytest.skip("Передано значение десктопа")
    else:
        browser.open('/')
        browser.element(".js-details-target.Button--link ").click()
        browser.element('.HeaderMenu-link--sign-in').click()
