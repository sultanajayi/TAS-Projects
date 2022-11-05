from selenium.webdriver.common.by import By


class TestAutomationSimplified:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.logo_image = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[1]/a/div/span[1]/img')
        self.stories_link = driver.find_element(By.LINK_TEXT, "Success Stories")
        self.title_text = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/h1')
        self.title2_text = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/p')



