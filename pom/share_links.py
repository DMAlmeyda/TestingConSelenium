
from pom.Base import Base
from selenium.webdriver.common.by import By
import requests
import time
class share_links(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.facebook = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[1]/a')
        self.twitter = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[2]/a')
        self.email = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[3]/a')
        self.pinterest = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[4]/a')
        self.goggle = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[5]/a')
        self.linkedin = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[6]/a')
        self.myspace = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[7]/a')
        self.digg = (By.XPATH, '//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[8]/a')

    def test_01_Facebook(self):
        url = self.driver.find_element(*self.facebook).get_attribute("href")
        self.driver.get(url)
        titulo = self.driver.title
        response = requests.head(url)
        status = response.status_code
        check = [titulo, status]
        return check

    def test_02_Twitter(self):
        url = self.driver.find_element(*self.twitter).get_attribute("href")
        self.driver.get(url)
        titulo = self.driver.title
        response = requests.head(url)
        status = response.status_code
        check = [titulo, status]
        return check

    def test_03_Email(self):
        link = self.driver.find_element(*self.email).get_attribute("href")
        return link

    def test_04_Pinterest(self):
        url = self.driver.find_element(*self.pinterest).get_attribute("href")
        self.driver.get(url)
        titulo = self.driver.title
        response = requests.head(url)
        status = response.status_code
        check = [titulo, status]
        return check



    def test_05_Goggleplus(self):
        url = self.driver.find_element(*self.goggle).get_attribute("href")
        self.driver.get(url)
        titulo = self.driver.title
        response = requests.head(url)
        status = response.status_code
        check = [titulo, status]
        return check

    def test_06_Linkedin(self):
        url = self.driver.find_element(*self.linkedin).get_attribute("href")
        self.driver.get(url)
        titulo = self.driver.title
        response = requests.head(url)
        status = response.status_code
        check = [titulo, status]
        return check

    def test_07_Myspace(self):
        url = self.driver.find_element(*self.myspace).get_attribute("href")
        self.driver.get(url)
        titulo = self.driver.title
        response = requests.head(url)
        status = response.status_code
        check = [titulo, status]
        return check

    def test_08_Digg(self):
        url = self.driver.find_element(*self.digg).get_attribute("href")
        self.driver.get(url)
        titulo = self.driver.title
        response = requests.head(url)
        status = response.status_code
        check = [titulo, status]
        return check