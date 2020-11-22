from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup
import config
import time
import csv


# Instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


# Webdriver initialization
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
web_url = 'https://www.site.com/rolesec/site/#login'
browser.get(web_url)
print("working") #debugging


#Log into website and click "login" button
user_name = browser.find_element_by_id('username')
user_name.send_keys(config.DATACOUP_USERNAME)
time.sleep(4)
print("still working...")  #debugging
password = browser.find_element_by_id('password')
password.send_keys(config.DATACOUP_PASSWORD)
time.sleep(4)
submit = browser.find_element_by_id('loginButton')
submit.click()
time.sleep(4)
print("...")  #debugging


#Click on the "Year" button to get clients' names over last 12 months
browser.find_element_by_link_text('Year').send_keys(Keys.RETURN)
time.sleep(4)


# Give source code to BeautifulSoup and parse
soup = BeautifulSoup(browser.page_source, 'lxml')

#Find and print one client's name  -  works
cnames = soup.find('div', class_='listCtrlEntry')
cname = cnames.find('span', class_='eBidActClientName')
print(cname.text)


#Find and print all client emails
cinfo = soup.find_all('div', class_='listCtrlEntry')
for each in cinfo:
    email = soup.find('a', class_='emailLink')
    print(email.text)
    csv_writer.writerow(email.text)

#Exit headless chrome browser session
browser.quit()


'''
with open('pep_pull.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)

#write header row for csv
#csv_writer.writerow(['Email'])



#Find and print all client's name  - Only gets names that are visible
count = 0
cnames = soup.find_all('div', class_='listCtrlEntry')
for cname in cnames:
    time.sleep(0.5)
    if cname == None:
        print('cname empty')
        continue
    else:
        actname = cname.find('span', class_='eBidActClientName')
        if actname == None and count < 1:
            browser.find_element_by_link_text('Year').send_keys(Keys.RETURN)
            time.sleep(4)
            count += 1
            print('first time')
            continue
        elif actname == None:
            print('second time')
            continue
        else:
            print(actname.text)
'''



'''
#Print email and phone in same line ----works!!!!!
cnames = soup.find_all('div', class_='listCtrlEntry')
for cname in cnames:
    email = cname.find('a', class_='emailLink')
    phone = cname.find('a', class_='telLink')
    print(email.text, phone.text)
'''

#file.close()

#print(cinfo)


'''
#Find and print all client's name - Prints "none" after visible names
cname = soup.find_all('div', class_='listCtrlEntry')
for each in cname:
    try:
        print (each.find('span', class_='eBidActClientName').contents[0])
    except:
        print ("none")
        testing
'''
