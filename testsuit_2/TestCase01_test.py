from selenium import webdriver
import unittest
import time
from pom.share_links import share_links as sh
class TestCase01(unittest.TestCase):
    #Se verifica que todos los link para compartir un producto funcionen adecuadamente.
    link = None
    driver = None
    def setUp(self):
        self.link = sh(driver=webdriver)
        self.driver = self.link.chromeDriverConnection()
        self.link.visit("https://academybugs.com/store/dnk-yellow-shoes/")
        time.sleep(4)
    def tearDown(self):
        self.driver.close()
        self.driver.quit() 


    def test_Link_Facebook(self):
        verificar = self.link.test_01_Facebook()
        time.sleep(2)
        self.assertTrue(200, verificar[1])
        self.assertIn(verificar[0], "Facebook")


    def test_Link_Twitter(self):
        verificar = self.link.test_02_Twitter()
        time.sleep(2)
        self.assertTrue(200, verificar[1])
        self.assertIn(verificar[0], "Twitter")


    def test_Link_Email(self):
        self.assertIn("mailto:", self.link.test_03_Email())

    def test_Link_Pinterest(self):
        verificar = self.link.test_04_Pinterest()
        self.assertTrue(200, verificar[1])
        self.assertIn("Pinterest", verificar[0])

    def test_Link_Goggleplus(self):
        verificar = self.link.test_05_Goggleplus()
        self.assertTrue(200, verificar[1])
        self.assertIn("Google", verificar[0])

    def test_Link_Linkedin(self):
        verificar = self.link.test_06_Linkedin()
        self.assertTrue(200, verificar[1])
        self.assertIn("LinkedIn", verificar[0])


    def test_Link_Myspace(self):
        verificar = self.link.test_07_Myspace()
        self.assertTrue(200, verificar[1])
        self.assertIn("Myspace", verificar[0])


    def test_Link_Digg(self):
        verificar = self.link.test_08_Digg()
        self.assertTrue(200, verificar[1])
        self.assertIn("Digg", verificar[0])



if __name__ == "__main__":
    unittest.main()        


