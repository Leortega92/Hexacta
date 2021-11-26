from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import unittest
import time



class TestCase(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/lortega/Escritorio/python/chrondriver/chromedriver")
   
    def test_Hexacta(self):
        url = "https://www.hexacta.com/"

        self.driver.maximize_window()
        self.driver.get(url)

        search = self.driver.find_element_by_xpath("//div[@class='social-links']/.//a[@class='searchbox']")
        search.click()
        searchType = self.driver.find_element_by_xpath("//input[@type='search']")
        searchType.send_keys("Outsource")
        searchType.send_keys(Keys.ENTER)
        
        time.sleep(2)

        salto_pagina = self.driver.find_element_by_xpath("//div[@class='pagination']/a[contains(text(), '2')]")
        salto_pagina.click()
        time.sleep(2)

        texto = "WHY OUTSOURCE IN ARGENTINA?"
        titulos = self.driver.find_elements_by_class_name("entry-title")
        for titulo in titulos:
            if texto in titulo.text:
                self.assertTrue(True)
        
        
        

 
        
if __name__ == '__main__':
    unittest.main()        
    

 
      
          
        