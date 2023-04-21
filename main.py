from selenium import webdriver # Подключаем библиотеку
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def end(n):
    if n == 5:
        return True
    return False
def start():
    driver = webdriver.Chrome(executable_path ="ChromeSetup(2).exe")
    driver.get('https://www.google.com/')
    search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search.send_keys('Python Developer')
    time.sleep(3)
    search.send_keys(Keys.ENTER)
    n=0
    for i in range(len(driver.find_elements(By.CLASS_NAME,'uEierd'))):
        try:
            print(driver.find_element(By.XPATH,f'//div[@id="tads"]/div[{i+1}]/div/div/div/div[1]/a/div[1]/span').text)
        except:
            n-=1
        n+=1
        if end(n):
            return
    for i in range(len(driver.find_elements(By.CLASS_NAME,'MjjYud'))):
        try:
            print(driver.find_element(By.XPATH,f'//*[@id="rso"]/div[{i+1}]/div/div/div[1]/div/a/h3').text)
        except:
            n-=1
        n += 1
        if end(n):
            return
start()
