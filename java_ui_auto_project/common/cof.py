from selenium import webdriver
def get_java_host():
    host = "http://admin.cosysong.com"
    return host

def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver