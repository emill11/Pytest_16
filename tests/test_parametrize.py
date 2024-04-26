import pytest
from selene import browser


@pytest.mark.parametrize('github_desktop', [(3000, 2000), (1500, 1000)], indirect=True)
def test_github_desktop(github_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('github_mobile', [(200, 400), (300, 500)], indirect=True)
def test_github_mobile(github_mobile):
    browser.open('/')
    browser.element(".js-details-target.Button--link ").click()
    browser.element('.HeaderMenu-link--sign-in').click()
