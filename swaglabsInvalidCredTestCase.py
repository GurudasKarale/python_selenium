import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class loginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Mohit K\Desktop\python_selenium\chromedriver.exe")

    def test_invalidPassword(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        #self.assertIn("Swag Labs", driver.title,"Title mismatched")

        element1=driver.find_element(By.ID,"user-name")
        element1.send_keys("standard_user")
        element2=driver.find_element(By.ID,"password")
        element2.send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()

        time.sleep(5)
        geturl=driver.current_url
        #gettxtelement=driver1.find_element(By.CLASS_NAME,"title")
        #gettext=gettxtelement.text

        if(geturl=="https://www.saucedemo.com/inventory.html"):
            self.assertTrue("Login Succeeded")

        else:
            element3=driver.find_element(By.CLASS_NAME,"error-button")

            if(element3):
            #self.assertIn("","","Test failed")
                driver.find_element(By.CLASS_NAME,"error-button").click()
                time.sleep(5)
                self.assertFalse(element3,"Login failed")
        # else:
        #     self.assertTrue(element3,"Login Succeeded")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()