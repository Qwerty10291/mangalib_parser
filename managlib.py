from selenium import webdriver
import zipfile
import os
import sys
import time
link = 'https://mangalib.me/busou-shoujo-machiavellism'
login = 'andrtazet@gmail.com'

drive = webdriver.Firefox()
drive.get(link)
drive.find_element_by_class_name('header__sign-in').click()
while True:
    try:
        drive.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[2]/div/input[2]').send_keys(login)
        drive.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[3]/div[2]/input').send_keys('QWERTY1029')
        drive.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[5]/button').click()
        break
    except:
        time.sleep(1)
time.sleep(15)
for i in drive.find_elements_by_class_name('fa-cloud-download')[4:91]:
    i.click()
