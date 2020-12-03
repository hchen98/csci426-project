# This script should not be runned again since 
# it scraping the info and then upload to the firestore

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
import logging
import threading
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

HOME_URL = "https://www.scholarships.com"
ROOT_URL = "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory"
LOGIN_URL = "https://www.scholarships.com/login"

USERNAME = "csci426@protonmail.com"
PASSWORD = "2QAaF5hjc$@k"


def simulate_login():
    # simulation of login
    driver.get(LOGIN_URL)

    # simulate login
    driver.find_element_by_id("Email").send_keys(USERNAME)
    driver.find_element_by_name("Password").send_keys(PASSWORD)
    driver.find_element_by_xpath('//input[@type="submit"]').click()


def search_level_tbl():
    # search scholarship categoery table
    # OUTPUT: seleiunm <a> list

    # locate the table of scholarship
    root_tbl = driver.find_element_by_id("ullist")

    # locate the element by categories
    a_tag_tbl = root_tbl.find_elements_by_tag_name("a")
    return a_tag_tbl


def scraping_levels(sele_ele):
    # scarping first level category
    # INPUT: selenium obj <-- scholarship tbl
    # OUTPUT: url and title (category)

    level_link = []
    level_title = []

    for a_tag in sele_ele:
        cate_link = a_tag.get_attribute("href")
        cate_title = a_tag.text
        level_link.append(cate_link)
        level_title.append(cate_title)

    return level_link, level_title


def get_scholar_tbl():
    # level 3 scholarship table
    # OUTPUT: # OUTPUT: selenium <tr> list

    link = []
    title = []
    # locate the info of scholarship
    scholar_tbl = driver.find_element_by_tag_name("tbody")
    tr = scholar_tbl.find_elements_by_tag_name("tr")
    for t in tr:
        x = t.find_element_by_tag_name("td a")
        link.append(x.get_attribute("href"))
        title.append(x.text)
        # print(x.get_attribute("href"))

    return link, title


def scraping_scholar_tbl(tr_ele):
    # get the item inside the scholar table on level 3
    # INPUT: selenium <tr> ele

    scholar_tit = []
    scholar_link = []

    for item in tr_ele:
        # nested tag here, locate <td> then <a>
        temp = driver.find_element_by_tag_name("td a")
        L3_link = temp.get_attribute("href")
        scholar_tit.append(temp.text)
        scholar_link.append(L3_link)
        # print(temp.text, ":\n", L3_link, "\n\n")
        # sleep to ensure IP address is not blocked
        time.sleep(random.randint(1, 6))

    return scholar_link, scholar_tit


def test_write2file(item):
    # testing func: write the scraping data to a txt
    # INPUT: scraping array
    with open("test_output.txt", "a+", encoding="utf-8") as writer:
        for x in item:
            writer.write(str(x) + "\n")

        writer.write("======================================\n\n")
        writer.close()


def insert_collection(db, docName, data):
    doc_ref = db.collection(u'scholar_dir').document(docName)
    doc_ref.set({
      docName: data
    })


try:
    # config firefox profile
    fp = webdriver.FirefoxProfile()
    fp.set_preference("http.response.timeout", 5)
    fp.set_preference("dom.max_scrit_run_time", 2)
    fp.set_preference("javascript.enabled", False)

    fo = webdriver.FirefoxOptions()
    # set headless so that no browser is displayed
    fo.headless = True
    fo.add_argument('--disable-extensions')
    fo.add_argument('--disable-infobars')
    fo.add_argument('--disable-javascript')

    # create a driver
    global driver
    driver = webdriver.Firefox(firefox_profile=fp, options=fo)

    # simulation login
    simulate_login()

    # open the root page
    driver.get(ROOT_URL)

    # scraping level 1
    level_1_tbl = search_level_tbl()
    L1_link, L1_title = scraping_levels(level_1_tbl)
    counter = 1
    scholarship_dist = {}

    for x in range(0, len(L1_link)):
        if "Military Affiliation" == L1_title[x]:
            # special case, no sub-category
            scholarship_dist[L1_title[x]] = L1_title[x]
            continue

        driver.get(L1_link[x])

        # scraping level 2
        level2_tbl = search_level_tbl()
        L2_link, L2_title = scraping_levels(level2_tbl)

        for y in range(0, len(L2_link)):

            scholarship_dist[L1_title[x]] = (L2_title)

    cred = credentials.Certificate('/home/hui/Desktop/google-service-account_CSCI426.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()


    scholarship_list = list(scholarship_dist)
    for i in range(0, len(scholarship_list)):
        # Insert the data!
        doc_name = scholarship_list[i]
        insert_collection(db, doc_name, scholarship_dist[doc_name])

    print("Data Insert!")
    
finally:
    try:
        driver.close()
    except:
        pass
