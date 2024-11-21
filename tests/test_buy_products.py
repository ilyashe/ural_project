import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.run(order=1)
def test_buy_products():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test 1')

    '''Открываем главную страницу'''
    mp = MainPage(driver)
    mp.open_base_url()
    '''Открываем раздел Одежда'''
    mp.open_clothes()
    '''Добавляем переменную для подсчета общей цены'''
    common_price = 0

    '''Сортируем по цене от большего к меньшему'''
    cp = CatalogPage(driver)
    cp.select_sort_by_price()
    cp.select_sort_by_price()
    '''Открываем самый дорогой продукт'''
    cp.open_product_1()

    '''Добавляем цену продукта в common_price и продукт в корзину'''
    pp = ProductPage(driver)
    common_price += pp.get_price_product_value()
    pp.add_product_xl_to_cart()

    '''Открываем раздел Атрибуты'''
    mp.open_attributes()
    '''Выбираем фильтр от 100 до 1000'''
    cp.select_filter_from_100_to_1000()
    '''Добавляем цену продукта в common_price и продукт в корзину'''
    common_price += cp.get_price_product_1_value()
    cp.add_product_1_to_cart()
    '''Выбираем фильтр от 2000 до 5000'''
    cp.select_filter_from_2000_to_5000()
    '''Добавляем цену продукта в common_price и продукт в корзину'''
    common_price += cp.get_price_product_1_value()
    cp.add_product_1_to_cart()

    '''Открываем раздел Сувениры'''
    mp.open_souvenirs()
    '''Сортируем по цене от меньшего к большему'''
    cp.select_sort_by_price()
    '''Добавляем цену продукта в common_price и продукт в корзину'''
    common_price += cp.get_price_product_1_value()
    cp.add_product_1_to_cart()
    '''Добавляем цену девятого в списке продукта в common_price и продукт в корзину'''
    common_price += cp.get_price_product_9_value()
    cp.add_product_9_to_cart()
    '''Выбираем фильтр от 2000 до 5000'''
    cp.scroll_up()
    cp.select_filter_from_2000_to_5000()
    '''Сортируем по цене от меньшего к большему'''
    cp.select_sort_by_price()
    '''Добавляем цену продукта в common_price и продукт в корзину'''
    common_price += cp.get_price_product_1_value()
    cp.add_product_1_to_cart()

    '''Открываем корзину'''
    cp.select_cart()

    cart_page = CartPage(driver)
    '''Сравниваем common_price с ценой в корзине'''
    cart_common_price = cart_page.get_common_price_value()
    cart_page.assert_price(common_price,cart_common_price)
    '''Делаем скриншот'''
    cart_page.scroll_down(500)
    cart_page.get_screenshot()
    '''Заполняем инфо покупателя (без нажатия на оформить)'''
    cart_page.input_information()
    '''Кликаем на body - закрываем открывшийся список городов'''
    cart_page.click_on_body()
    '''Делаем скриншот'''
    cart_page.scroll_down(1100)
    cart_page.get_screenshot()
    time.sleep(5)

    print('Finish Test 1')

    driver.quit()