from selene import browser


def test_github_desktop(github_desktop):
    browser.open("/")
    browser.element(".HeaderMenu-link--sign-in").click()


def test_github_mobile(github_mobile):
    browser.open("/")
    browser.element(".js-details-target.Button--link ").click()
    browser.element(".HeaderMenu-link--sign-in").click()
