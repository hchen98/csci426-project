from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random

URL = "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/academic-major/computer-science"

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

    # open a page
    driver.get(URL)

    list_tt = []
    list_amount = []
    list_date = []

    # locate the info of scholarship
    scholar_tbl = driver.find_element_by_tag_name("tbody")
    tr = scholar_tbl.find_elements_by_tag_name("tr")

    for item in tr:
        # nested tag here
        temp = item.find_element_by_tag_name("td a")
        link = temp.get_attribute("href")
        title = temp.text

        amount = item.find_element_by_css_selector("td.scholamt").text
        deadline = item.find_element_by_css_selector("td.scholdd").text

        # sleep to ensure IP address is not blocked
        time.sleep(random.randint(1, 6))

        # print(title, " ===> ", amount, " ===> ", deadline)
        # print(link, "\n")

finally:
    try:
        driver.close()
    except:
        pass
