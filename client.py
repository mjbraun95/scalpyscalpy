from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import os

def confirm():
    cont = input("Continue?[Y/n]")
    if cont.lower() == "n":
        quit()

def nikeLoop():
    size = input("Provide size: ")
    quantity = input("Provide quantity: ")
    link = input("Provide a link: ")
    # driver = webdriver.Firefox()
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(link)
    assert "Nike" in driver.title
    confirm()
    # buyTools = driver.find_element_by_id("buyTools")
    # sizeCell = buyTools.find_element_by_class("css-xf3ahq")
    sizeElem = driver.find_element_by_link_text("US {}".format(size))
    sizeElem.click()
    confirm()

    addToCart = driver.find_element_by_link_text("Add to Bag")
    addToCart.click()
    confirm()

    checkout = driver.find_element_by_link_text("Checkout")
    checkout.click()
    confirm()

    memberCheckout = driver.find_element_by_link_text("Member Checkout")
    memberCheckout.click()
    confirm()

    email = driver.find_element_by_name("emailAddress")
    email.send_keys("mjbraun@ualberta.ca", Keys.ENTER)
    confirm()

    password = driver.find_element_by_name("password")
    email.send_keys("", Keys.ENTER)
    confirm()

    # checkout = driver.find_element_by_link_text("Checkout")
    # checkout.click()
    # confirm()

    # checkout = driver.find_element_by_link_text("Checkout")
    # checkout.click()
    # confirm()

    
    # find_element_by_class("ncss-btn-primary-dark btn-lg css-y0myut add-to-cart-btn")

    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    driver.close()


def clientLoop():
    userInput = input("Select a website\n    N = https://www.nike.com/ca/\n    b = https://www.bestbuy.ca/en-ca\n    w = https://www.walmart.ca/en\n    u = https://www.usmint.gov/\n    s = https://www.staples.ca/")

    nikeLoop()

if __name__ == "__main__":
    while True:
        clientLoop()