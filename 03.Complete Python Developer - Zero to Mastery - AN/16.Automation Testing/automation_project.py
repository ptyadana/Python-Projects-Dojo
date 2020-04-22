from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert('Show Message' in chrome_browser.page_source)

user_message_textbox = chrome_browser.find_element_by_id('user-message')
user_message_textbox.clear()
user_message_textbox.send_keys('python is awesome!')

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()

display_message = chrome_browser.find_element_by_id('display')
output = display_message.text
print(output)

assert 'python is awesome!' in output

chrome_browser.quit()