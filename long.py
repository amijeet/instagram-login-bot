from selenium import webdriver
import time 

username = "username"
f = open("password.txt","r")
driver =  webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
if f.mode == "r":
	contents = f.read()
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(contents)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()
time.sleep(4)
driver.find_element_by_xpath("//*[contains(text(),'Not Now')]").click()
time.sleep(2)
#driver.quit()
