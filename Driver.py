from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from collections import defaultdict

HOME_URL = "https://www.scholarships.com"
ROOT_URL = "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory"

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
    driver.get(ROOT_URL)

    # locate the table of scholarship
    root_tbl = driver.find_element_by_id("ullist")

    # locate the element by categories
    level_1_tbl = root_tbl.find_elements_by_tag_name("a")

    level1_link = []
    level1_title = []
    level2_link = []
    level2_title = []
    counter = 0

    for a_tag in level_1_tbl:
        cate1_link = a_tag.get_attribute("href")
        cate1_title = a_tag.text
        # level1_link.append(cate1_link)
        # level1_title.append(cate1_title)
        # print(cate1_title)

        # end level 1 crawling

        driver.get(cate1_link)
        cate2_tbl = driver.find_element_by_id("ullist")
        level2_tbl = cate2_tbl.find_elements_by_tag_name("a")

        for link in level2_tbl:
            cate2_link = a_tag.get_attribute("href")
            cate2_title = a_tag.text
            # level2_link.append(cate2_link)
            # level2_title.append(cate2_title)

            # end level 2 crawling
            driver.get(cate2_link)
            cate3_tbl = driver.find_element_by_id()





finally:
    try:
        driver.close()
    except:
        pass
