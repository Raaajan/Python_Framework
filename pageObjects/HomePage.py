from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.XPATH, "//input[@type='password']")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_password(self):
        return self.driver.find_element(*HomePage.password)

    def click_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def click_submit(self):
        return self.driver.find_element(*HomePage.submit)
