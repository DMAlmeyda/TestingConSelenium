
from pom.Base import Base
from selenium.webdriver.common.by import By


class btn_viewCart(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.buybtn_1_ID = (By.ID, 'ec_add_to_cart_5')
        self.buybtn_2_ID = (By.ID, 'ec_add_to_cart_4')
        self.buybtn_3_ID = (By.ID, 'ec_add_to_cart_2')
        self.buyconfirmation_CLASS = (By.CLASS_NAME, 'ec_product_added_to_cart')
        self.viewcart_XPATH = (By.XPATH, '//*[@id="ec_product_page"]/div[2]/a')
        self.viewcart_elements_CLASS = (By.CLASS_NAME, 'ec_cartitem_details')

    def buy1(self):
        self.click(self.buybtn_1_ID)

    def buy2(self):
        self.click(self.buybtn_2_ID)

    def buy3(self):
        self.click(self.buybtn_3_ID)

    def buy_confirmation(self):
        self.isDisplayed(self.buyconfirmation_CLASS)

    def go_to_viewcart(self):
        self.click(self.viewcart_XPATH)

    def item_store(self):
        return self.findElements(self.viewcart_elements_CLASS)

