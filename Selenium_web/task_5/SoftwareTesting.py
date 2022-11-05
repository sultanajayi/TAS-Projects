from selenium.webdriver.common.by import By


class SwitchToSoftwareTesting:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")

        self.logo_image = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[1]/a/div/span[1]/img')
        self.courses_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/button')
        self.title_text = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/h1')
        self.enroll_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
        self.enroll_button.click()

