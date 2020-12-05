# https://medium.com/@praneeth.jm/running-chromedriver-and-selenium-in-python-on-an-aws-ec2-instance-2fb4ad633bb5
# ChromeDriver 87.0.4280.88

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import logging
import threading

################# RECENTLY Changed####################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

scholar_ref = db.collection("ScholarshipHub")
table_ref = db.collection("Index Table").document("Terms")
refList = table_ref.get().to_dict().get('Terms')
######################################################

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


def get_specific():
    # get specific scholarship detail
    # OUTPUT: scholarship attributes

    test = []
    award_info = driver.find_element_by_class_name("award-info-row")
    temp = award_info.find_elements_by_tag_name("h3")

    # get general info
    amount = temp[0].text
    deadline = temp[1].text
    ava = temp[2].text
    ava_wrd, ava_num = ava.split(":")

    # get direct apply link
    temp = driver.find_element_by_css_selector(
        ".award-info-action-items [href]")
    temp = temp.get_attribute("href")
    # need to parse here since the site will open another window event with js
    spliter = temp.split(",")
    dir_link = spliter[0][26:-1]

    # get abstract scholarship description
    description = driver.find_element_by_class_name("scholdescrip").text

    # scholarship contact info
    temp2 = driver.find_element_by_id("ulScholDetails").text
    lines = temp2.splitlines()
    flag = False
    contact_info = ""

    for item in lines:
        if (item == "Scholarship Committee"):
            # special case:
            # need to remove useless scholarship contact info
            flag = True
            continue

        if (flag):
            contact_info = contact_info + item + "\n"

    # print(amount, "\n", deadline, "\n", ava_num, "\n", dir_link, "\n", description, "\n", contact_info, "\n\n")

    test.append(amount)
    test.append(deadline)
    test.append(ava_num)
    test.append(dir_link)
    test.append(description)
    test.append(contact_info)

    test_write2file(test)
    return amount, deadline, ava_num, dir_link, description, contact_info


def test_write2file(item):
    # testing func: write the scraping data to a txt
    # INPUT: scraping array
    with open("test_output.txt", "a+", encoding="utf-8") as writer:
        for x in item:
            writer.write(str(x) + "\n")

        writer.write("======================================\n\n")
        writer.close()


########################### RECENTLY ADDED ###########################################
#Firestore methods used


#Inputs new scholarship into the firestore
#Input -> All attributes of scholarship
#Output -> None
def addScholarship(name, amount, deadline, ava, dir_link, description,
                   contact_info, binary):
    scholar_ref.document(name).set({
        u'Name': name,
        u'Amount': amount,
        u'Deadline': deadline,
        u'Awards Available': ava,
        u'Direct Link': dir_link,
        u'Description': description,
        u'Contact Info': contact_info,
        u'Binary': binary,
        u'Terms': {}
    })


#Updates the term array in firestore
#Input-> id to locate the scholarship, term
#Output-> None
def updateTerms(schol_id, term):
    scholar_ref.document(schol_id).update(
        {u'Terms': firestore.ArrayUnion([term])})


#splits the string to array
#input -> string
#output -> char array
def split(word):
    return [char for char in word]


#converts list to string
#Input -> list
#output -> array
def toString(list):
    str = ""
    return (str.join(list))


#Finds the index of the word based on a table generated from the driver
#Input -> string, the word
#output -> int, the index
def catIndex(word):
    ind = refList.index(word)
    return ind


#Updates the binary based on the word in firestore
#Input -> int, string, the id of the scholarship and the term
#Output -> none
def updateBin(id, word):
    scholarBin = scholar_ref.document(id).get().to_dict().get('Binary')
    ind = catIndex(word)
    list = split(scholarBin)
    list[ind] = "1"
    binaryStr = toString(list)
    scholar_ref.document(id).update({'Binary': binaryStr})


#String to generate the inital binary array of 504 bits because I'm lazy to type it out =D
binaryInitial = '0' * 807
#######################################################

try:
    # config firefox profile
    # fp = webdriver.FirefoxProfile()
    # fp.set_preference("http.response.timeout", 5)
    # fp.set_preference("dom.max_scrit_run_time", 2)
    # fp.set_preference("javascript.enabled", False)

    fo = webdriver.ChromeOptions()
    # set headless so that no browser is displayed
    fo.headless = True
    fo.add_argument('--disable-extensions')
    fo.add_argument('--disable-infobars')
    fo.add_argument('--disable-javascript')

    # create a driver
    global driver
    driver = webdriver.Chrome(options=fo)

    # simulation login
    simulate_login()

    # open the root page
    driver.get(ROOT_URL)

    # scraping level 1
    level_1_tbl = search_level_tbl()
    L1_link, L1_title = scraping_levels(level_1_tbl)

    ################ Table now on Firestore ##########################

    counter = 1
    for x in range(0, len(L1_link)):
        if "Military Affiliation" == L1_title[x]:
            # special case, no sub-category
            continue

        driver.get(L1_link[x])

        # scraping level 2
        level2_tbl = search_level_tbl()
        L2_link, L2_title = scraping_levels(level2_tbl)

        for y in range(0, len(L2_link)):
            driver.get(L2_link[y])
            L3_link, L3_title = get_scholar_tbl()

            # scraping for level 3
            for z in range(0, len(L3_link)):
                driver.get(L3_link[z])
                amount, deadline, ava, dir_link, description, contact_info = get_specific(
                )

                ################# RECENTLY Changed #################
                #If statement for if scholarship exists
                #Id is now just the name of the scholarship for less reads
                scholarship = scholar_ref.document(L3_title[z]).get()
                if scholarship.exists == False:
                    addScholarship(L3_title[z], amount, deadline, ava,
                                   dir_link, description, contact_info,
                                   binaryInitial)

#Updates term list and binary string, now with scholarship name
                updateTerms(L3_title[z], L2_title[y])
                updateBin(L3_title[z], L2_title[y])
                #################################################

                logging.info("Logging at " + str(counter))
                counter = counter + 1

finally:
    try:
        driver.close()
    except:
        pass
