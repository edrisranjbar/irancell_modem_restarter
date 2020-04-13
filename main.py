from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

current_path = os.getcwd()
browser = webdriver.Chrome(f"{current_path}/chromedriver")

# Initializing variables
url = "http://192.168.1.1"
username = "admin"
password = "admin"

browser.get(url)
browser.switch_to.frame(browser.find_element_by_id('frame_menu'))
username_txt = browser.find_element_by_xpath("//*[@id='login_center_box']/div[1]/input")
password_txt = browser.find_element_by_xpath("//*[@id='login_center_box']/div[2]/input")
username_txt.send_keys(username)
password_txt.send_keys(password)
password_txt.send_keys(Keys.RETURN)
sleep(5)
browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="index_frameset"]/frame[1]'))
browser.find_element_by_xpath("/html/body/img[5]").click()
print("Restarting Process started...")
alert = browser.switch_to_alert()
alert.accept()
sleep(10)
browser.close()
print("Done!")