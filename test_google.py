import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver



class Test_google_1:

    def test_001(self,):
        web=webdriver.Chrome()
        web.get("https://www.google.com/")
        logo = web.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        if logo==True:
            print("sucess")
            assert True
        else:
            assert False