from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from collections import defaultdict

HOME_URL = "https://www.scholarships.com"
ROOT_URL = "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory"
LOGIN_URL = "https://www.scholarships.com/login"

USERNAME = "csci426@protonmail.com"
PASSWORD = "2QAaF5hjc$@k"

try:
    # config firefox profile
    fp = webdriver.FirefoxProfile()
    fp.set_preference("http.response.timeout", 5)
    fp.set_preference("dom.max_scrit_run_time", 5)

    fo = webdriver.FirefoxOptions()
    # set headless so that no browser is displayed
    fo.headless = True
    fo.add_argument('--disable-extensions')
    fo.add_argument('--disable-infobars')

    # create a driver
    driver = webdriver.Firefox(firefox_profile=fp, options=fo)

    driver.get(LOGIN_URL)

    # simulate login
    driver.find_element_by_id("Email").send_keys(USERNAME)
    driver.find_element_by_name("Password").send_keys(PASSWORD)
    driver.find_element_by_xpath('//input[@type="submit"]').click()

    # open a page
    driver.get(ROOT_URL)

    # locate the table of scholarship
    root_tbl = driver.find_element_by_id("ullist")

    # locate the element by categories
    level_1_tbl = root_tbl.find_elements_by_tag_name("a")

    for a_tag in level_1_tbl:
        cate1_link = a_tag.get_attribute("href")
        cate1_title = a_tag.text
        print(cate1_title + ": " + cate1_link)
        # end level 1 crawling

finally:
    try:
        driver.close()
    except:
        pass
