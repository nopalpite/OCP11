import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def test_firefox():

    # Setup
    email = "john@simplylift.co"
    service = Service('tests/functional_test/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)

    # Test board
    driver.get("http://127.0.0.1:5000/board")
    time.sleep(2)
    assert "Board | GUDLFT" in driver.title

    # Test login
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)
    assert "GUDLFT Registration" in driver.title
    driver.find_element(By.TAG_NAME, "input").send_keys(email + Keys.ENTER)
    time.sleep(3)
    assert "Summary | GUDLFT Registration" in driver.title

    # Test book past competition
    link = driver.find_elements(By.LINK_TEXT, "Book Places")
    link[0].click()
    time.sleep(2)
    assert "This competition is over!" in driver.page_source

    # Test book future competition
    link = driver.find_elements(By.LINK_TEXT, "Book Places")
    link[2].click()
    assert "Booking for" in driver.title
    time.sleep(2)
    driver.find_element(By.NAME, "places").send_keys("1" + Keys.ENTER)
    time.sleep(2)
    assert "Great-booking complete!" in driver.page_source

    # Test logout
    link = driver.find_element(By.LINK_TEXT, "Logout")
    link.click()
    time.sleep(2)
    assert "GUDLFT Registration" in driver.title

    driver.close()
