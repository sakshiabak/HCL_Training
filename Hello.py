from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_website():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.python.org")

        assert "Python" in driver.title

    finally:
        driver.quit()