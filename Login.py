import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def test_a_login_success(self):
        #step
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("syakir13@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("Qwerty2006")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#signin_login").click()
        time.sleep(1)

        #validasi
        textAtas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        textBawah = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertIn("Welcome",textAtas)
        self.assertEqual(textBawah,"Anda Berhasil Login")

    def test_b_login_gagal(self): #password salah
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("syakir13@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("Qwerty123")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(1)

        #validasi
        textAtas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        textBawah = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertIn("not",textAtas)
        self.assertEqual(textBawah,"Email atau Password Anda Salah")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()