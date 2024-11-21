from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class MainPage(Base):

    url = "https://shop.fc-ural.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    clothes = '//a[contains(text(), "Одежда")]'
    attributes = '//a[contains(text(), "Атрибутика")]'
    souvenirs = '//a[contains(text(), "Сувениры")]'

    # Getters

    def get_clothes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clothes)))

    def get_attributes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.attributes)))

    def get_souvenirs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.souvenirs)))

    # Actions

    def click_clothes(self):
        self.get_clothes().click()
        print('Click clothes')

    def click_attributes(self):
        self.get_attributes().click()
        print('Click attributes')

    def click_souvenirs(self):
        self.get_souvenirs().click()
        print('Click souvenirs')

    # Methods

    def open_base_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def open_clothes(self):
        self.get_current_url()
        self.click_clothes()

    def open_attributes(self):
        self.get_current_url()
        self.click_attributes()

    def open_souvenirs(self):
        self.get_current_url()
        self.click_souvenirs()