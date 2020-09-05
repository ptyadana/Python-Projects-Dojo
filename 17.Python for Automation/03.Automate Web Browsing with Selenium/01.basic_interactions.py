from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

# Sending Message
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys("Hello World")

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()


# Suming up two numbers
input_a = driver.find_element_by_xpath('//*[@id="sum1"]')
input_b = driver.find_element_by_xpath('//*[@id="sum2"]')

input_a.send_keys("10")
input_b.send_keys("20")

totalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
totalButton.click()

# driver.close()
