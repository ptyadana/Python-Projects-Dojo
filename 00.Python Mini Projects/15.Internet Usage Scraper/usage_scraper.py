import requests
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_usage_history(page_source):

    last_7_days_usage = []

    print("scrapping usage info...")
    soup = BeautifulSoup(page_source, "lxml")

    dates = soup.find_all(
        "h5", class_="list-group-item--bold")

    usages = soup.find_all("div", class_="badge badge-pill badge-info")

    for index in range(len(dates)):
        date = dates[index].text.strip("\n              ")
        usage_in_GB = usages[index].text

        last_7_days_usage.append((date, usage_in_GB))

    return last_7_days_usage


def usage_history_scraper():
    base_url = "https://blahblah.com"

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(base_url)
    print("logging in...")

    # login to the site
    user_id = driver.find_element_by_xpath(
        '//*[@id="form-customer-login"]/div[1]/input')
    user_id.send_keys("blahblah")

    password = driver.find_element_by_xpath(
        '//*[@id="form-customer-login"]/div[2]/input')
    password.send_keys("blahblah")

    login_button = driver.find_element_by_xpath(
        '//*[@id="form-customer-login"]/div[3]/button')
    login_button.click()

    print("logged in successfully...")

    # sleep for a few seconds to wait website to load
    time.sleep(5)

    # go to usage history page and get info
    more_menu = driver.find_element_by_xpath(
        '//*[@id="navbarDropdownMenuLink"]')
    more_menu.click()
    time.sleep(2)

    usage_history_menu = driver.find_element_by_xpath(
        '//*[@id="appNavigation"]/div[2]/div/div/button[6]')
    usage_history_menu.click()
    time.sleep(5)
    page_source = driver.page_source

    last_7_days_usage = get_usage_history(page_source)
    for item in last_7_days_usage:
        print(item[0], ",", item[1])


if __name__ == "__main__":
    usage_history_scraper()
