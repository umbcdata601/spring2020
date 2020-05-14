# http://www.teachmeselenium.com/2018/04/17/python-selenium-actionchains-introducing-actionchains-and-moving-mouse-over-an-element/
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
 
driver_path = "/home/jovyan/week_05_automation/selenium_demo_imdb/chromedriver"
 
driver = webdriver.Chrome(driver_path )
driver.get("https://www.imdb.com")
eleMenuShowtimes = driver.find_element_by_id("navTitleMenu")
 
time.sleep(5)

action_chains = ActionChains(driver)
action_chains.move_to_element(eleMenuShowtimes)
action_chains.click(driver.find_element_by_link_text("In Theaters"))
action_chains.perform()
 
time.sleep(5)

if "New Movies In Theaters" in driver.title:
    print("Passed")
else:
    print("Failed")
 
driver.quit()
