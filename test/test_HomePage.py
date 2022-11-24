import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    def test_fill_details(self):
        homepage = HomePage(self.driver)
        homepage.enter_name().send_keys("ABCD")
        homepage.enter_email().send_keys("abc@gmail.com")
        homepage.enter_password().send_keys("Abcd@1234")
        homepage.click_checkbox().click()
        s = Select(homepage.select_gender())
        s.select_by_visible_text("Male")
        homepage.click_submit().click()
        time.sleep(2)
        msg = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success" in msg
        time.sleep(2)


print("execution completed successfully")
