from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import sub
from decimal import Decimal

instauname = input("Please enter your instagram's username : ")
instaupass = input("Please enter instagram user password : ")

class Instabot:
    def __init__(self,username,password,OtherUserId):
        self.driver=webdriver.Chrome("C:\\Users\yogesh kartik\PycharmProjects\python_test1\driver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(instauname)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(instaupass)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(10)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(5)
        self.driver.get("https://www.instagram.com/"+OtherUserId)
        posts = self.driver.find_element_by_xpath("/html/body/div/section/main/div/header/section/ul/li/span/span").text
        posts = Decimal(sub(r'[^\d.]', '', posts))
        print(posts)
        pic = self.driver.find_element_by_class_name("_9AhH0")
        pic.click()
        sleep(2)
        like = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        like.click()
        nextPic = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
        nextPic.click()
        print("success")
        sleep(2)
        for i in range(int(posts-1)):
            like = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
            sleep(2)
            like.click()
            sleep(2)
            nextPic = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
            nextPic.click()
            sleep(2)
    sleep(20)
Instabot('abcxcwe','dfasd32963','capdt') #Username,password,Username of other person