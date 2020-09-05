from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

driver.get(
    "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")


# source and destination elements
washington_box = driver.find_element_by_xpath('//*[@id="box3"]')
country_bucket = driver.find_element_by_xpath('//*[@id="box103"]')

# drag and drop complex tasks
actions = ActionChains(driver)
actions.drag_and_drop(washington_box, country_bucket).perform()
