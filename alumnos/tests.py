from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import selenium

import time
# Create your tests here.

PATH = "C:\Program Files (x86)\chromedriver.exe"

"""class Hosttest(TestCase):

    def testapipage(self):
        driver = webdriver.Chrome(PATH)
        driver.get("http://localhost:3000/api/alumnos/")
        time.sleep(3)
        elementos = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[6]')
        print("-----------> ELEMENTOS: ", elementos.text)
        driver.quit()"""

class LoginFormTest(LiveServerTestCase):
    def testForm(self):
        driver = webdriver.Chrome(PATH)
        driver.get("http://localhost:3000/admin/login/?next=/admin/")
        time.sleep(5)
        user_name = driver.find_element(By.NAME, 'username')
        pass_word = driver.find_element(By.NAME, 'password')

        submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[3]/div/button')

        user_name.send_keys("admin")
        pass_word.send_keys("passpassword")
        submit.send_keys(Keys.RETURN)
        time.sleep(5)
        
        