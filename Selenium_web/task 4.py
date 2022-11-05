import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "hello@mailinator.com")
    send_keys_to_element(driver.find_element(By.NAME, "pass"), "Hello419$")
    login = driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(20)


if __name__ == '__main__':
    main()
