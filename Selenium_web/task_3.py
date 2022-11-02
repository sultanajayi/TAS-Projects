from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_by_property(element):
    print("Text", element.text)
    print("Size", element.size)
    print("Tag Name", element.tag_name)
    print("Location", element.location)
    print("Accessible Name", element.accessible_name)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    elements = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print_by_property(elements)


if __name__ == '__main__':
    main()
