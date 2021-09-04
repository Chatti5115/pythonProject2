from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')

driver = webdriver.Chrome('chromedriver.exe', options=options)