import time 
import os
from dotenv import load_dotenv
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

Y_EMAIL = os.getenv("Y_EMAIL")
Y_PASSWORD = os.getenv("Y_PASSWORD")
Y_LOGIN_URL = os.getenv("Y_LOGIN_UR")
SPEED_URL = os.getenv("SPEED_URL")

class InternetSpeedTwitterBot ():
    def __init__(self):
        self.down = self.up = 0 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_speedtest (self):
        self.driver.get(SPEED_URL)
        
        cookie = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        
        self.driver.execute_script("arguments[0].click();", cookie)
        


    def internet_speed(self):

        self.driver.get(SPEED_URL)

        go_click = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            go_click
        )
        go_click.click()

        time.sleep(60)

        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
            (By.XPATH, "//p[contains(., 'Download')]/following-sibling::h3"))
        )

        self.down = float(
            self.driver.find_element(
                By.XPATH,
                "//p[contains(., 'Download')]/following-sibling::h3"
            ).text
        )

        self.up = float(
            self.driver.find_element(
                By.XPATH,
                "//p[contains(., 'Upload')]/following-sibling::h3"
            ).text
        )


    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        email = self.driver.find_element(By.ID,"email")
        email.click()
        email.send_keys(Y_EMAIL)
        passwd = self.driver.find_element(By.ID,"password")
        passwd.click()
        passwd.send_keys(Y_PASSWORD)
        button = self.driver.find_element(By.XPATH,"/html/body/div/div/form/button")
        button.click()
