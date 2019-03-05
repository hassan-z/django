from selenium import webdriver

#browser = webdriver.Firefox(executable_path=r"/home/hassan/seleniumDrivers/geckodriver")
browser = webdriver.Chrome(executable_path=r"/home/hassan/seleniumDrivers/chromedriver")
browser.get('http://localhost:8000')

assert 'Django' in browser.title