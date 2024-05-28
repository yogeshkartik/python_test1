from selenium import webdriver

# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome("C:\\Users\yogesh kartik\PycharmProjects\python_test1\driver\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("https://www.instagram.com/")
driver.find_element_by_xpath("//input[@name='username']").send_keys("")
driver.find_element_by_xpath("//input[@name='password']").send_keys("")
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
"""username = driver.find_element_by_name("username")
password = driver.find_element_by_password("password")

username.send_keys("")
password.send_keys("")

driver.find_element_by_name("Log in").click()"""
# to refresh the browser
# driver.refresh()
# to close the browser
# driver.close()
