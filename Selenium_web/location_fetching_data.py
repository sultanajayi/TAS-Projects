from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_by_element(element):
    print("Text", element.text)
    print("Size", element.size)
    print("Tag Name", element.tag_name)
    print("Location", element.location)
    print("Accessible Name", element.accessible_name)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    element = driver.find_element(By.TAG_NAME, "h2")
    print_by_element(element)

if __name__ == '__main__':
    main()
