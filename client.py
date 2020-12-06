from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def nikeLoop():
    size = input("Provide size: ")
    quantity = input("Provide quantity: ")
    link = input("Provide a link: ")
    driver = webdriver.Firefox()
    driver.get(link)
    assert "Nike" in driver.title
    # buyTools = driver.find_element_by_id("buyTools")
    # sizeCell = buyTools.find_element_by_class("css-xf3ahq")
    sizeElem = driver.find_element_by_link_text("US {}".format(size))
    sizeElem.click()

    addToCart = driver.find_element_by_link_text("Add to Bag")
    addToCart.click()

    checkout = driver.find_element_by_link_text("Checkout")
    checkout.click()

    memberCheckout = driver.find_element_by_link_text("Member Checkout")
    memberCheckout.click()

    email = driver.find_element_by_name("emailAddress")

    password = driver.find_element_by_name("password")

    checkout = driver.find_element_by_link_text("Checkout")
    checkout.click()

    checkout = driver.find_element_by_link_text("Checkout")
    checkout.click()

    
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