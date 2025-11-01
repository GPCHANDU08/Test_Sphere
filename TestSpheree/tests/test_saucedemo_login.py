import pytest
from TestSpheree.helpers.driver_factory import create_driver    

from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),
    ("standard_user", "wrong_password", False),
    ("locked_out_user", "secret_sauce", False)
])
def test_saucedemo_login(username, password, expected):
    driver = create_driver(headless=True)
    login = LoginPage(driver)
    login.login(username, password)

    result = login.is_logged_in()
    driver.save_screenshot(f"TestSpheree/reports/{username}_result.png")
    driver.quit()

    assert result == expected
