from selenium import webdriver
from selenium.webdriver.firefox.options import Options

URL_LOGIN = "https://www.scholarships.com/login"

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

driver.get(URL_LOGIN)

USERNAME = "csci426@protonmail.com"
PASSWORD = "2QAaF5hjc$@k"

# simulate login
driver.find_element_by_id("Email").send_keys(USERNAME)
driver.find_element_by_name("Password").send_keys(PASSWORD)
driver.find_element_by_xpath('//input[@type="submit"]').click()
# driver.find_element_by_css_selector("mdc-button").click()

URL_TEST = "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/academic-major/computer-science/isc%C2%B2-graduate-cybersecurity-scholarship"

driver.get(URL_TEST)


# =================== start scraping =======================
award_info = driver.find_element_by_class_name("award-info-row")
temp = award_info.find_elements_by_tag_name("h3")

# get general info
amount = temp[0].text
deadline = temp[1].text
ava = temp[2].text

# get direct apply link
temp = driver.find_element_by_css_selector(".award-info-action-items [href]")
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

driver.close()