
from pom.btn_viewCart import btn_viewCart as btn
from selenium import webdriver
import unittest
import time

#Se verifica que las funciones buy y viewcart funcionen como los requerimentos indican
class TestCase01(unittest.TestCase):
    driver = None
    btn = None
    def setUp(self):
        self.btn = btn(driver = webdriver)
        self.driver = self.btn.chromeDriverConnection()
        self.btn.visit("https://academybugs.com/find-bugs/")
        time.sleep(5)

    def test_BuyButton(self):
        time.sleep(3)
        self.btn.buy1()
        time.sleep(3)
        self.assertTrue(True, self.btn.buy_confirmation())

    def test_ViewCart(self):
        self.btn.buy1()
        time.sleep(1)
        self.btn.buy2()
        time.sleep(1)
        self.btn.buy3()
        time.sleep(3)
        self.btn.go_to_viewcart()
        time.sleep(3)
        productos = self.btn.item_store()
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

