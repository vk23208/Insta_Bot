# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 04:04:31 2020

@author: Vishal Rana
"""
'For likes'
from selenium import webdriver
import time
EXE_PATH = r'C://Users//Vishal Rana//chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=EXE_PATH,chrome_options=chrome_options)

searchnames = ['dogworld']

for i in searchnames:
    a = str('https://www.instagram.com/explore/tags/')+str(i)
    driver.get(a)
    time.sleep(4)

    login = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
    login.click()
    time.sleep(3)

    username = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    username.click()
    username.send_keys('username')

    password = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    password.click()
    password.send_keys('password')

    login = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]')
    login.click()
    time.sleep(4)

    first = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    first.click()
    time.sleep(2)

    like = driver.find_element_by_class_name('fr66n')
    like.click()
    time.sleep(2)
    nextbutton = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
    nextbutton.click()
    time.sleep(2)

    for i in range(0,15):
        like = driver.find_element_by_class_name('fr66n')
        like.click()
        time.sleep(2)

        nextbutton = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        nextbutton.click()
        time.sleep(2)

    driver.quit()

##########################################################################################
'For following'
from selenium import webdriver
import time
EXE_PATH = r'C://Users//Vishal Rana//chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=EXE_PATH,chrome_options=chrome_options)

searchnames = ['dogworld']

for i in searchnames:
    a = str('https://www.instagram.com/explore/tags/')+str(i)
    driver.get(a)
    time.sleep(4)

    login = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
    login.click()
    time.sleep(3)

    username = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    username.click()
    username.send_keys('username')

    password = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    password.click()
    password.send_keys('password')

    login = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]')
    login.click()
    time.sleep(4)

    first = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    first.click()
    time.sleep(2)
    
    follow = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
    follow.click()
    time.sleep(3)
    
    nextbutton = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
    nextbutton.click()
    time.sleep(2)

    for i in range(0,15):
        follow = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
        follow.click()
        time.sleep(3)

        nextbutton = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        nextbutton.click()
        time.sleep(2)
    driver.quit()

##############################################################
        
'For comments'
from selenium import webdriver
import time
import random
EXE_PATH = r'C://Users//Vishal Rana//chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=EXE_PATH,chrome_options=chrome_options)

searchnames = ['dogworld']
commentsbox = ['love,love,love','Awwww','Gorgeous','Beautiful']

for i in searchnames:
    a = str('https://www.instagram.com/explore/tags/')+str(i)
    driver.get(a)
    time.sleep(4)

    login = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
    login.click()
    time.sleep(3)

    username = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    username.click()
    username.send_keys('username')

    password = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    password.click()
    password.send_keys('password')

    login = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]')
    login.click()
    time.sleep(4)

    first = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    first.click()
    time.sleep(2)

    comment = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
    comment.click()
    comment1 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
    comment1.send_keys(random.choice(commentsbox))
    time.sleep(3)
    
    post = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button')
    post.click()
    time.sleep(2)
    
    nextbutton = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
    nextbutton.click()
    time.sleep(2)

    for i in range(0,15):
        comment = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
        comment.click()
        comment1 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
        comment1.send_keys(random.choice(commentsbox))
        time.sleep(3)
        post = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button')
        post.click()
        time.sleep(2)

        nextbutton = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        nextbutton.click()
        time.sleep(2)

    driver.quit()
time.sleep(5)
