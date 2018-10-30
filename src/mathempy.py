import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class Mathempy:
    def __init__(self, chromedriver_executable_path=None, headless=False):
        self.mathem_base_url = "https://www.mathem.se"
        self.basket_url = "https://www.mathem.se/kassan"
        self.login_url = "https://www.mathem.se/Account/LogIn"
        self.logout_url = "https://www.mathem.se/Account/LogOffConfirmed"
        self.headless = headless
        if not chromedriver_executable_path:
            self.chromedriver_executable_path=os.path.abspath("../chromedriver")
        self.create_session()
    
    def create_session(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=self.chromedriver_executable_path, options=chrome_options)
        self.driver.get(self.mathem_base_url)

    def basket_add_item(self, url, quantity):
        self.driver.get(url)
        product_id = self.driver.find_element_by_id('ItemId').get_attribute('value')
        product_amount_box = self.driver.find_element_by_xpath("//div[@class='prodImgAndBuy']//input")
        product_amount_box.clear()
        product_amount_box.send_keys(quantity)
        product_amount_box.send_keys(Keys.RETURN)

    def basket_list(self):
        self.driver.get(self.basket_url)

        contents = []
        try:
            shopping_cart_list = self.driver.find_element_by_id("shoppingCartList")
        except NoSuchElementException as e:
            return contents
            
        for item in shopping_cart_list.find_elements_by_xpath("//div[@data-group='category']"):
            this_item_name = item.find_element_by_class_name("prodTitle").text
            this_item_quantity = item.find_element_by_name("Quantity").get_attribute("value")
            contents.append({"name": this_item_name, "quantity": this_item_quantity})

        return contents

    def basket_total(self):
        self.driver.get(self.basket_url)
        try:
            total = self.driver.find_element_by_class_name("totalBig").text
            total = total.replace("Att betala: ", "")
            total = total.replace("Kr", "")
            total = total.replace("kr", "")
            total = total.replace(",",".")
            total = total.rstrip()
            return float(total)
        except NoSuchElementException as e:
            return 0

    def save_basket(self, basket_name):
        self.driver.get(self.basket_url)
        try:
            expand_save_basket_inputs_button = self.driver.find_element_by_class_name("icon-list")
            expand_save_basket_inputs_button.click()
        except NoSuchElementException as e:
            print("Not logged in")
            return False

        save_basket_list_input = self.driver.find_element_by_id("shoppingListName")
        time.sleep(1) # wait for the dialog box to open
        save_basket_list_input.clear()
        save_basket_list_input.send_keys(basket_name)

        save_list_save_button = self.driver.find_element_by_xpath("//input[@value='Spara']")
        save_list_save_button.click()

        try:
            time.sleep(2) # wait for the alert to finish arriving, if it does at all
            alert = self.driver.switch_to_alert()
            alert.accept()
            print("A basket with that name already exists.")
            return False
        except NoAlertPresentException as e:
            return True



    def login(self, username, password):

        self.driver.get(self.login_url)
        username_field = self.driver.find_element_by_id('Username')
        password_field = self.driver.find_element_by_id('Password')
        login_button = self.driver.find_element_by_xpath("//input[@value='Logga in']")

        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

        try:
            returned = self.driver.find_element_by_xpath("//pre").text
            return True
        except:
            return False

    def logout(self):
        self.driver.get(self.logout_url)

    def exit(self):
        self.driver.close()