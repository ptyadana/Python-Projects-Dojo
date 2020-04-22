from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

print('Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title)

#auto click on button
button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML'))