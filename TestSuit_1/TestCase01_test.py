
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class Test_Funciones(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.driverpath = 'C:\\Users\\Dieguillo\\Desktop\\driver\\chromedriver.exe'
        self.driver = webdriver.Chrome(self.driverpath, options = self.options)
        #Configuracion especial para mi workspace
        self.driver.set_window_position(-2000, 0)
        self.driver.maximize_window()
        time.sleep(1)

    def test_BuyButton(self):
        self.driver.get("https://academybugs.com/find-bugs/")
        self.driver.find_element("xpath",'//*[@id="ec_add_to_cart_5"]').click()
        time.sleep(3)
        self.assertTrue(True, self.driver.find_element("xpath", '//*[@id="ec_product_page"]/div[2]').is_displayed())

    def test_ViewCart(self):
        self.driver.get("https://academybugs.com/find-bugs/")
        self.driver.find_element("xpath",'//*[@id="ec_add_to_cart_5"]').click()
        time.sleep(3)
        self.driver.find_element("xpath",'//*[@id="ec_add_to_cart_4"]').click()
        time.sleep(3)
        self.driver.find_element("xpath",'//*[@id="ec_add_to_cart_2"]').click()
        time.sleep(3)
        self.driver.find_element("xpath", '//*[@id="ec_product_page"]/div[2]/a').click()
        time.sleep(3)
        productos = self.driver.find_elements(By.CLASS_NAME, 'ec_cartitem_details')
        ListaPD = list()
        for p in productos:
            ListaPD.append(p.text)

        self.assertEqual(ListaPD[0], "Blue Tshirt")
        self.assertEqual(ListaPD[1], "Dark Grey Jeans")
        self.assertEqual(ListaPD[2], "DNK Yellow Shoes")    


    def tearDown(self):
        self.driver.quit() 

if __name__ == "__main__":
    unittest.main()    

