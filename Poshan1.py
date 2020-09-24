from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui as gui
from win10toast import ToastNotifier
import base64
import time
from time import sleep
from random import randint

driver = webdriver.Firefox()
site = "http://poshanabhiyaan.gov.in"
dataentryxpath = "/html/body/app-maahdashboard/div[1]/nav/div/div[3]/div[2]/div/a[3]"
user = 'mow&cd-2751626'
password = user
driver.get(site)
data = driver.find_element_by_xpath(dataentryxpath)
data.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

userfield = driver.find_element_by_id("mat-input-0")
userfield.send_keys(user)
passfield = driver.find_element_by_id("mat-input-1")
passfield.send_keys(password)
#userfield.clear()
gui.alert("Enter Captcha and press Enter!")
time.sleep(2)
#driver.switch_to.window(driver.window_handles[0])
driver.switch_to.window(driver.window_handles[1])
try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located(By.ID,"id1"))
    print("Page loaded.")
except:
    print("Page not loaded.")
