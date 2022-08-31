import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegis(unittest.TestCase): #test scenario
    def setUp(self):
        #self.browser = webdriver.Chrome(ChromeDriverManager().install())
        #Selenium v4 compatible Code Blok
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_a_regis_success(self):
        #step
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("Amma Syakir")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("syakir13@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("Qwerty2006")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)
        #browser.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()
        #time.sleep(1)

        #validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertEqual(text_atas,"berhasil")
        self.assertIn("user",text_bawah)

    def test_b_regis_gagal(self): #email sudah dipakai
        #step
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("Amma Syakir")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("syakir13@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("Qwerty2006")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        #validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertEqual(text_atas,"Email sudah terdaftar") #real condition: Oops
        self.assertIn("gagal",text_bawah)

    
    def tearDown(self):
        self.browser.close()
    
if __name__ == "__main__":
    unittest.main()