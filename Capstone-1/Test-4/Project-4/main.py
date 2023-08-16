from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data import data
from Test_Locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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

        # Navigate to the PIM module
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Pim_Module).click()
        self.driver.implicitly_wait(2)
        # Navigate the Action Methods
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Action_Module).click()
        self.driver.implicitly_wait(2)
        # Navigate the Edit button Methods
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Edit_Module).click()

        # Locate the input fields for editing using different locators and enter new employee
        self.driver.find_element(by=By.NAME, value=locators.Locators().First_input_button).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.NAME, value=locators.Locators().First_input_button).send_keys(Keys.DELETE)
        self.driver.find_element(by=By.NAME, value=locators.Locators().Firstname_input_button).send_keys(data.Data().Middle_Name)

        self.driver.find_element(by=By.NAME, value=locators.Locators().Middle_input_button).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.NAME, value=locators.Locators().Middle_input_button).send_keys(Keys.DELETE)
        self.driver.find_element(by=By.NAME, value=locators.Locators().Middlename_input_button).send_keys(data.Data().Middle_Name)

        self.driver.find_element(by=By.NAME, value=locators.Locators().Last_input_button).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.NAME, value=locators.Locators().Last_input_button).send_keys(Keys.DELETE)
        self.driver.find_element(by=By.NAME, value=locators.Locators().Lastname_input_button).send_keys(data.Data().Last_Name)
        
        self.driver.implicitly_wait(2)

        # Click the Save button to save the changes
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Save_Module).click()

        logout_button = self.driver.find_element(by=By.XPATH, value=locators.Locators().logout_1)
        action = ActionChains(self.driver)
        action.click(on_element=logout_button).perform()        
        self.driver.find_element(by=By.LINK_TEXT, value='Logout').click()
        


johnsi = Johnsi(data.Data().url)
johnsi.login()
