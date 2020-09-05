# Why to use Wait Functions ?
# - many websites use asynchronous techniques to load content
# - technique creates a problem when Selenium tries to locate an element that isn't loaded yet
# - to avoid exceptions in scripts, such as above scenarios

# Wait function add crucial time intervals in between actions performed.
# Two types of Wait in Selenium :
#       1) Explicit Wait Function - wait until a condition is satisfied.
#       2) Implicit Wait Function - pull DOM for a certain amount of time, until element becomes available


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.google.com/earth/")

# define explict wait until a certain condition is satisfied, this case Launch Button is appeared
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))

launchEarthButton.click()
