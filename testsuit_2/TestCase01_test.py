# Librerías
from selenium import webdriver
import unittest
import time
import requests

class TestCase01(unittest.TestCase):
    #Se verifica que todos los link para compartir un producto funcionen adecuadamente.

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.driverpath = '/home/dieguillo/Documents/chromedriver'
        self.driver = webdriver.Chrome(self.driverpath, options = self.options)
        #Configuracion especial para mi workspace
        self.driver.set_window_position(-2000, 0)
        self.driver.maximize_window()
        time.sleep(1)



    def tearDown(self):
        self.driver.quit() 

    #Facebook
    def test_01_Facebook(self):
        response = requests.head("http://www.facebook.com/sharer/sharer.php?p[url]=https://academybugs.com/store/dnk-yellow-shoes/&p[images][o]=https://academybugs.com/wp-content/uploads/2020/10/shoe8-updated.jpg&p[title]=DNK+Yellow+Shoes")
        time.sleep(2)
        self.assertTrue(200, response.status_code)

    #Twitter
    def test_02_Twitter(self):
        response = requests.head("https://twitter.cointent/tweet?original_referer=#")
        time.sleep(2)
        self.assertTrue(200, response.status_code)

    #Email
    def test_03_Email(self):
        self.driver.get("https://academybugs.com/store/dnk-yellow-shoes/")
        time.sleep(3)
        url = self.driver.find_element("xpath","/html/body/div[3]/div/div/div[1]/main/article/div/section/div[1]/div[3]/div[2]/div[3]/a").text
        self.assertIn(url,"mailto")

    #Pinterest    
    def test_04_Pinterest(self):
        response = requests.head("http://pinterest.com/pin/create/button/?media=https%3A%2F%2Facademybugs.com%2Fwp-content%2Fuploads%2F2020%2F10%2Fshoe8-updated.jpg&description=DNK+Yellow+Shoes&url=https%3A%2F%2Facademybugs.com%2Fstore%2Fdnk-yellow-shoes%2F")
        time.sleep(2)
        self.assertTrue(200, response.status_code)

    #Goggleplus
    def test_05_Goggleplus(self):
        response = requests.head("https://plus.google.com/share?url=https://academybugs.com/store/dnk-yellow-shoes/")
        time.sleep(2)
        self.assertTrue(200, response.status_code)
        
    #Linkedin
    def test_06_Linkedin(self):
        response = requests.head("http://www.linkedin.com/shareArticle?mini=true&url=https://academybugs.com/store/dnk-yellow-shoes/")
        time.sleep(2)
        self.assertTrue(200, response.status_code)

    #MySpace
    def test_07_MySpace(self):
        self.driver.get("https://academybugs.com/store/dnk-yellow-shoes/")
        self.driver.find_element("xpath",'//*[@id="post-1675"]/div/section/div[1]/div[3]/div[2]/div[7]/a/img').click()
        time.sleep(3)
        current = self.driver.current_window_handle
        self.driver.switch_to.window([w for w in self.driver.window_handles if w != current][0])    
        time.sleep(3)
        self.assertTrue("MySpace", self.driver.title)
        
    #Digg
    def test_08_Digg(self):
        response = requests.head("http://digg.com/submit?phase=2&url=https://academybugs.com/store/dnk-yellow-shoes/")
        time.sleep(2)
        self.assertTrue(200, response.status_code)   
               
if __name__ == "__main__":
    unittest.main()        


