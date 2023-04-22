from selenium import webdriver # driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Runner():
    """returns 5 firsts names links"""
    def __init__(self):
        self.start()
    @staticmethod
    def end(minimal_row_output) -> int:
        return minimal_row_output == 5

    def start(self) -> None:
        driver = webdriver.Chrome(executable_path="ChromeSetup(2).exe")
        driver.get('https://www.google.com/')
        search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        search.send_keys('Python Developer')
        search.send_keys(Keys.ENTER)
        minimal_row_output = 0
        for i in range(len(driver.find_elements(By.CLASS_NAME, 'uEierd'))):
            try:
                print(driver.find_element(By.XPATH,
                                          f'//div[@id="tads"]/div[{i + 1}]/div/div/div/div[1]/a/div[1]/span').text)
            except Exception:
                minimal_row_output -= 1
            minimal_row_output += 1
            if self.end(minimal_row_output):
                return
        for i in range(len(driver.find_elements(By.CLASS_NAME, 'MjjYud'))):
            try:
                print(driver.find_element(By.XPATH, f'//*[@id="rso"]/div[{i + 1}]/div/div/div[1]/div/a/h3').text)
            except Exception:
                minimal_row_output -= 1
            minimal_row_output += 1
            if self.end(minimal_row_output):
                return


if __name__ == "__main__":
    Runner()
