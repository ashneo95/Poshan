from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pyautogui as gui
from win10toast import ToastNotifier
import base64
import time
from time import sleep
from random import randint
def PressEscape():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ESCAPE)
    actions.perform()

driver = webdriver.Firefox()
url = "http://poshanabhiyaan.gov.in/#/login"
driver.get(url)
username = "mow&cd-2751626"
password = "mow&cd-2751626"
userfield = driver.find_element_by_id("mat-input-0")
userfield.send_keys(str(username))
passfield = driver.find_element_by_id("mat-input-1")
passfield.send_keys(str(password))
gui.alert("Enter Captcha!")
button = driver.find_element_by_id("signin")
button.click()
noticexpath = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[2]/div/div/div[3]/button"
time.sleep(5)
try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, noticexpath))).click()
    #print('Element found successfully:  Notice Button.')
except:
    print('Not found :  Notice Button.')
    gui.alert("Terminated at first try block.")
#noticebutton = driver.find_element_by_xpath(noticexpath)
#noticebutton.click()
time.sleep(1)
xhomevisit = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[1]/div[1]/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]"
homevisit = driver.find_element_by_xpath(xhomevisit)
homevisit.click()
xhomevisits = "/html/body/div/div[2]/div/div/mat-option[5]/span"
time.sleep(1)
homevisits = driver.find_element_by_xpath(xhomevisits)
homevisits.click()
time.sleep(1)
xblock = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[1]/div[2]/div/div[1]/mat-form-field/div/div[1]/div"
block = driver.find_element_by_xpath(xblock)
block.click()
time.sleep(1)
xblocks = "/html/body/div/div[3]/div/div/mat-option[2]/span"
blocks = driver.find_element_by_xpath(xblocks)
blocks.click()
time.sleep(1)
xtheme = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[1]/div[1]/div/div[3]/mat-form-field/div/div[1]/div/mat-select/div/div[1]"
theme = driver.find_element_by_xpath(xtheme)
theme.click()
time.sleep(1)
xthemes = "/html/body/div/div[4]/div/div/mat-option[9]/span" #Growth Monitoring
themes = driver.find_element_by_xpath(xthemes)
themes.click()
PressEscape()
#themes.send_keys("\t")
'''
themes = Select(driver.find_element_by_xpath(xthemes))
themes.select_by_visible_text('Growth Monitoring')
'''

time.sleep(1)
xorganizer = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[1]/div[2]/div/div[2]/mat-form-field/div/div[1]/div"
organizer = driver.find_element_by_xpath(xorganizer)
organizer.click()
time.sleep(0.5)
xorganizers = "/html/body/div/div[5]/div/div/mat-option[4]/span"
organizers = driver.find_element_by_xpath(xorganizers)
organizers.click()
PressEscape()
#organizer.send_keys("\t")

for i in range(1000):
    print("Entry No: ", i+1)
    time.sleep(0.5)
    male_a = 1
    female_a = randint(1, 3)
    male_c = randint(1, 3)
    female_c = randint(1, 3)
    total = male_a + female_a + male_c + female_c

    xtotal = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/input"
    total_field = driver.find_element_by_xpath(xtotal)
    total_field.send_keys(str(total))

    xmalea = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[1]/th[2]/input"
    malea_field = driver.find_element_by_xpath(xmalea)
    malea_field.send_keys(str(male_a))

    xfemalea = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[1]/th[3]/input"
    femalea_feild = driver.find_element_by_xpath(xfemalea)
    femalea_feild.send_keys(str(female_a))

    xmalec = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[2]/th[2]/input"
    malec = driver.find_element_by_xpath(xmalec)
    malec.send_keys(str(male_c))

    xfemalec = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[2]/th[3]/input"
    femalec = driver.find_element_by_xpath(xfemalec)
    femalec.send_keys(str(female_c))

    descfield = driver.find_element_by_id("mat-input-5")
    descfield.send_keys("Dhodambe")
    time.sleep(0.25)

    xsubmitbutton = "/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[2]/div/div[3]/div/div/button"
    submitbutton = driver.find_element_by_xpath(xsubmitbutton)
    submitbutton.click()

    xsuccess = "/html/body/app-dashboard/div/main/div/app-hierarchy/p-dialog[1]/div/div[2]/div[1]/div[1]/button/span"
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xsuccess))).click()
        #print('Element found successfully:  Success Button.')
    except:
        print('Not found :  Notice Button.')
        gui.alert("Terminated!")



