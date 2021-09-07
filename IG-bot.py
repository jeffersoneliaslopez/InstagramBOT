import os
from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')
sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("Tu usuario")
password_input.send_keys("Tu contraseña")


#file = open("cred.txt", mode='r')
#arr = file.readlines()

# username_input.send_keys(arr[0])
# password_input.send_keys(arr[1])

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(2)

not_save_info_button = browser.find_element_by_xpath(
    "//*[@id='react-root']/section/main/div/div/div/div/button")
not_save_info_button.click()

sleep(1)

not_now_button = browser.find_element_by_xpath(
    "/html/body/div[4]/div/div/div/div[3]/button[2]")
not_now_button.click()

# Inicio dar click a perfil y realizar

# final

sleep(180)

browser.close()
