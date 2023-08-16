from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data import data
from Test_Locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Johnsi:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
   
    def login(self):
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()

        # Navigate to Pim module
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Pim_module).click()
   
        #  Navigate to Action module
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Action_Module_Button).click()

         # Locate and click the delete button
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Delete_button).click()

        # Handle the confirmation dialog
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Confirmation_Button).click()

        # Close the browser
        logout_button = self.driver.find_element(by=By.XPATH, value=locators.Locators().Logout_1)
        action = ActionChains(self.driver)
        action.click(on_element=logout_button).perform()
        self.driver.find_element(by=By.LINK_TEXT, value='Logout').click()



johnsi = Johnsi(data.Data().url)
johnsi.login()


