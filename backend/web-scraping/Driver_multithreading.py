from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
import logging
# import threading
from queue import Queue
import concurrent.futures

################# RECENTLY ADDED ####################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

scholar_ref = db.collection("OfficialScholar")
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

    # print(amount, "\n", deadline, "\n", ava, "\n", dir_link, "\n", description, "\n", contact_info, "\n\n")

    test.append(amount)
    test.append(deadline)
    test.append(ava)
    test.append(dir_link)
    test.append(description)
    test.append(contact_info)

    test_write2file(test)
    return amount, deadline, ava, dir_link, description, contact_info


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
def addScholarship(docdirect, name, amount, deadline, ava, dir_link,
                   description, contact_info, binary):
    docdirect.add({
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


#Get id of the scholarship generated by firestore
#Input -> name of the scholarship, treated as a primary key
#Output -> id of the scholarship
def get_ScholID(name):
    doc_id = 'None'
    doc_find = scholar_ref.where(u'Name', u'==', name).stream()
    for i in doc_find:
        doc_id = i.id
    return str(doc_id)


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
    userBin = scholar_ref.document(id).get().to_dict().get('Binary')
    ind = catIndex(word)
    list = split(userBin)
    list[ind] = "1"
    binaryStr = toString(list)
    scholar_ref.document(id).update({'Binary': binaryStr})


#String to generate the inital binary array of 504 bits because I'm lazy to type it out =D
binaryInitial = '0' * 504
#######################################################


def intialDriver():
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
    # return driver


def categoryScraping():
    # initialize the browser driver
    intialDriver()

    # simulation login
    simulate_login()

    # open the root page
    driver.get(ROOT_URL)

    # scraping level 1
    level_1_tbl = search_level_tbl()
    L1_link, L1_title = scraping_levels(level_1_tbl)
    return L1_link, L1_title


def thread_func(L1_link, L1_title):
    counter = 1
    refList = []
    if "Military Affiliation" == L1_title:
        # special case, no sub-category
        driver.get(L1_link)
        military_link, military_title = get_scholar_tbl()
        for item in military_link:
            driver.get(item)
            get_specific()
    else:
        driver.get(L1_link)

        # scraping level 2
        level2_tbl = search_level_tbl()
        L2_link, L2_title = scraping_levels(level2_tbl)
        refList.extend(L2_title)
        for y in range(0, len(L2_link)):
            driver.get(L2_link[y])
            L3_link, L3_title = get_scholar_tbl()

            # scraping for level 3
            for z in range(0, len(L3_link)):
                driver.get(L3_link[z])
                get_specific()

                # amount, deadline, ava, dir_link, description, contact_info = get_specific()

                # ################# RECENTLY ADDED #################
                # #If statement for if id exists
                # id= get_ScholID(L3_title[z])
                # if id == 'None':
                #     addScholarship(scholar_ref, L3_title[z], amount, deadline, ava, dir_link, description, contact_info, binaryInitial)
                #     id = get_ScholID(L3_title[z])
                # #Updates term list and binary string
                # updateTerms(id, L2_title[y])
                # updateBin(id, L2_title[y])
                # #################################################

                logging.info("Logging at " + str(counter))
                counter = counter + 1


if __name__ == "__main__":
    L1_link, L1_title = categoryScraping()
    category_size = len(L1_link)
    link = Queue(maxsize=category_size)
    link = L1_link
    titile = Queue(maxsize=category_size)
    title = L1_title

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        while link.full():
            i = link.get()
            j = title.get()
            executor.submit(thread_func, i, j)
