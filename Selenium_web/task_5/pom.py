import time
from TestAutomation import TestAutomationSimplified
from SoftwareTesting import SwitchToSoftwareTesting
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    test_automation = TestAutomationSimplified(driver)
    software_testing = SwitchToSoftwareTesting(driver)

if __name__ == '__main__':

    main()
