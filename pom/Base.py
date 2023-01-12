from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
class Base:
    
    def __init__(self, driver):
        self.driver = driver
        self.options = None

    def chromeDriverConnection(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.s = Service('/home/dieguillo/Documents/chromedriver')
        self.driver = webdriver.Chrome(service=self.s, options=self.options)
        #Configuracion especial para mi workspace
        self.driver.set_window_position(-2000, 0)
        self.driver.maximize_window()
        return self.driver

    def findElement(self, locator):
            return self.driver.find_element(*locator)

    def findElements(self, locator):
            return self.driver.find_elements(*locator)

    def GetText(self, element):
            return element.getText()

    def GetText(self, locator):
            return self.driver.find_element(*locator).getText()

    def type(self, inputText, locator):
        return self.driver.find_element(*locator).sendkeys(inputText)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def isDisplayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except(NoSuchElementException):
            return False            
        
    def visit(self, url):
        self.driver.get(url)