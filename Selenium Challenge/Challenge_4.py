from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    news_1 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/a')
    print("News_1 : ", news_1.text)
    news_2 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]')
    print("News_2 : ", news_2.text)
    news_3 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]')
    print("News_3 : ", news_3.text)
    news_4 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]')
    print("News_4 : ", news_4.text)
    news_5 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]')
    print("News_5: ", news_5.text)
    news_6 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[1]/div/a')
    print("News_6 : ", news_6.text)
    news_7 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[2]')
    print(" News_7 : ", news_7.text)
    news_8 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[3]')
    print("News_8 : ", news_8.text)
    news_9 = driver.find_element(By.XPATH, '//*[@id="page"]/section[6]/div/ul/li[1]/div/a')
    print("News_9 : ", news_9.text)
    news_10 = driver.find_element(By.XPATH, '//*[@id="page"]/section[6]/div/ul/li[2]')
    print("News_10 : ", news_10.text)


if __name__ == '__main__':
    main()

