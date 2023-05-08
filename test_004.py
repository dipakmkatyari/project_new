from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_google_2:

    def test_005(self,):
        web=webdriver.Chrome()
        web.get("https://www.google.com/")
        logo = web.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        if logo:
            print("test cases passed")
            assert True
        else:
            assert False
            print("test cases failed")