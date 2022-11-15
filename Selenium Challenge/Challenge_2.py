import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("http://www.google.com")
    element = send_keys_to_element(driver.find_element(By.TAG_NAME, "input"), "Python")
    enterkey = driver.find_element(By.XPATH, '//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]').click()
    pytext = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div')
    time.sleep(20)
    print(pytext.text)


if __name__ == '__main__':
    main()
