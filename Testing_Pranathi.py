__author__="pranthi"
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.delete_all_cookies()
#driver = webdriver.firefox()
#driver = webdriver.Ie()

        #This is hard coded in seconds, It could be made more efficent by adding wait till page loads con
#driver.implicitly_wait(15)
driver.set_page_load_timeout(15)
#driver.get("http://google.com")
#driver.set_page_load_timeout(10)
driver.get("http://www.facebook.com")
driver.get_screenshot_as_file("facebook.png") 
driver.maximize_window()
driver.maximize_window()
driver.refresh()
#SIGN UP OF A PAGE#
#def sign_up_page(self):
driver.find_element_by_name("firstname").send_keys("SandhyaRani")
driver.set_page_load_timeout(10)
driver.find_element_by_name("lastname").send_keys("Parigi")
driver.set_page_load_timeout(10)
driver.find_element_by_name("reg_email__").send_keys("aaa@gmail.com")
driver.set_page_load_timeout(10)
driver.find_element_by_name("reg_email_confirmation__").send_keys("aaa@gmail.com")
driver.set_page_load_timeout(10)
driver.find_element_by_name("reg_passwd__").send_keys("Slpgn@gmail.com")

driver.find_element_by_xpath("//*[@id='day']").click()
#Select.select_by_visible_text("birthday_day")
#Select.select_by_index(3)
driver.find_element_by_xpath("//*[@id='month']").click()
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable(id("month")))
driver.find_element_by_xpath("//*[@id='year']").click()

driver.find_element_by_id("u_0_9").click()
driver.set_page_load_timeout(10)


#SUBMIT#
driver.find_element_by_name("websubmit").click()
driver.maximize_window()

driver.forward()

#driver.switch_to_window("https://www.flipkart.com/account/login?ret=/").click()
#driver.find_element_by_css_selector("body > div.mCRfo9 > div > div > div > div > div.Km0IJL.col.col-3-5 > div > form > a > span").click()
#driver.find_element_by_link_text("https://www.flipkart.com/account/login?signup=true").click()
#driver.switch_to_window("/account/login?signup=true").click()



time.sleep(12)







