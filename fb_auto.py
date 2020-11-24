from selenium import webdriver
from time import sleep

fbupass = input("Please enter your facebook password : ")
driver = webdriver.Chrome("C:\\Users\yogesh kartik\PycharmProjects\python_test1\driver\chromedriver.exe")
driver.get ("https://www.facebook.com")
driver.maximize_window()
driver.find_element_by_id("email").send_keys("kartikyogesh2004@gmail.com")
driver.find_element_by_id("pass").send_keys(fbupass)
driver.find_element_by_id("u_0_b").click()
sleep(30)
image = driver.find_element_by_class_name("l9j0dhe7")

# pos = 0
while 5>1:
    # driver.execute_script("window.scrollTo(pos, 20)", "")
    # pos +=20
    driver.execute_script("arguments[0].scrollIntoView();", image)
    sleep(2)