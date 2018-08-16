import os
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
uid = ""
password = ""
f = open("userdetails.json")
userdata = json.load(f)
f.close()
reset = input("Do you wanna re-enter details(Y/N) :")
if reset =='Y' or reset == 'y' : 
    r=True
else:
    r=False
if userdata["uid"] == "" or r == True :
    f=open("userdetails.json")
    userdata["uid"]=input("Enter your UID :")
    userdata["password"] = input("Enter your password :")

f=json.dumps(userdata)
uid = userdata["uid"]
password = userdata["password"]
driver = webdriver.Firefox(executable_path=r'./geckodriver-v0.21.0-win64/geckodriver.exe')
driver.get("https://uims.cuchd.in/UIMS/Login.aspx#")
user = driver.find_element_by_css_selector("#txtUserId")
print(password)
user.send_keys(uid)
print (uid)
user.send_keys(Keys.RETURN)
driver.implicitly_wait(4)
driver.current_url
passwordfield = driver.find_element_by_css_selector("#txtLoginPassword")
passwordfield.click()
passwordfield.send_keys(password)
passwordfield.send_keys(Keys.RETURN)
driver.get('https://uims.cuchd.in/UIMS/StudentHome.aspx')
#check attendance
driver.get('https://uims.cuchd.in/UIMS/frmStudentCourseWiseAttendanceSummary.aspx')