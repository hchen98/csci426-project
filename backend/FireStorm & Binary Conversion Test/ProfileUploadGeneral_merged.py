import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from datetime import date
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

#CosSim Calc
from numpy import dot
from numpy.linalg import norm

# cred = credentials.Certificate(
#     "testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
cred = credentials.Certificate(
    "google-service-account_CSCI426.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

scholar_ref=db.collection(u"ScholarshipHub")
user_Ref = db.collection("Users")
table_Ref = db.collection("Index Table").document("Terms")
refList = table_Ref.get().to_dict().get('Terms')


#Used to initiation user or update their information, specify when using optional attributes
def updtUser(userEmail,
             gender,
             dob,
             zipC,
             gpa,
             major='',
             race='',
             ethnicity='',
             religion='',
             dissabilities='',
             sat='',
             address1='',
             address2='',
             address3=''):

    list1 = [gender]
    list1.append(catAge(dob))
    list1.append(catState(zipC))
    list1.append(catGPA(gpa))

    list2 = [major, race, religion, dissabilities, ethnicity]
    for i in range(len(list2)):
        if list2[i] != '':
            list1.append(list2[i])

    if (sat != ''):
        list1.append(catSat(sat))

    binary = setBin(list1)

    user_Ref.document(userEmail).set({
        u'Email': userEmail,
        u'Gender': gender,
        u'Date of Birth': dob,
        u'Zip': zipC,
        u'GPA': gpa,
        u'Major': major,
        u'Religion': religion,
        u'Race': race,
        u'Ethnicity': ethnicity,
        u'Dissabilities': dissabilities,
        u'SAT Score': sat,
        u'Address 1': address1,
        u'Address 2': address2,
        u'Address 3': address3,
        u'Binary': binary,
        u'Terms': list1
    })


#def binaryConvert():
#refers to a list

#def updateAccount():
#update all fields? not too sure


def catState(zipC):
    zipcode = zcdb[zipC]
    state = abrevConv[zipcode.state]
    return state


abrevConv = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'DC': 'District of Columbia',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'MP': 'Northern Mariana Islands',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VI': 'Virgin Islands',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}


def catGPA(gpa):
    str = ' '
    gpa = float(gpa)
    if (gpa >= 1.0) & (gpa <= 2.0):
        str = 'Minimum Grade Point Average From 1.0 to 2.0'
    elif (gpa >= 2.1) & (gpa <= 2.5):
        str = 'Minimum Grade Point Average From 2.1 to 2.5'
    elif (gpa >= 2.6) & (gpa <= 3.0):
        str = 'Minimum Grade Point Average From 2.6 to 3.0'
    elif (gpa >= 3.1) & (gpa <= 3.5):
        str = 'Minimum Grade Point Average From 3.1 to 3.5'
    elif (gpa >= 3.6) & (gpa <= 4.0):
        str = 'Minimum Grade Point Average From 3.6 to 4.0'
    return str


def catAge(dob):
    birth = datetime.strptime(dob, "%m/%d/%Y")
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) <
                                     (birth.month, birth.day))
    string = ''
    if age < 13:
        string = ("Age 13")
    elif age > 30:
        string = ("Age Greater Than 30")
    else:
        string = ("Age " + str(age))
    return string


def catSat(sat):
    str = ''
    if (float(sat) >= 400) & (float(sat) <= 1000):
        str = 'SAT Scores From 400 To 1,000'
    elif (float(sat) >= 1001) & (float(sat) <= 1200):
        str = 'SAT Scores From 1,001 To 1,200'
    elif (float(sat) >= 1201) & (float(sat) <= 1400):
        str = 'SAT Scores From 1,201 To 1,400'
    elif (float(sat) >= 1401) & (float(sat) <= 1600):
        str = 'SAT Scores From 1,401 To 1,600'
    return str


#splits the string to array
#input -> string
#output -> char array
def splitStr(word):
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


def setBin(list):
    binaryInitial = '0' * 807
    usrList = splitStr(binaryInitial)
    for i in range(len(list)):
        ind = catIndex(list[i])
        usrList[ind] = "1"
    binaryStr = toString(usrList)
    return binaryStr


#Updates the binary based on the word in firestore
#Input -> int, string, the id of the scholarship and the term
#Output -> none

#listA = table_Ref.get().to_dict().get('Terms')
#print(setBin(['Accounting']))
#updtUser('some email', 'Male', '5/11/1999', '10308', '3.6', sat='1400')
# updtUser("hchen60@nyit.edu", "Male", "01/18/1998", "11223", "3.41",
#          "Computer Science", "Asian/Pacific Islander", "Chinese",
#          "Buddhist")




#########################################     METHODS    #######################
# Methods for binary filtering

#Split method
#Input -> String, ideally the binary string
#Output -> integer list to be used for CosSim
def splitInt(word):
    stringlist = [char for char in word]
    intlist = [int(i) for i in stringlist]
    return intlist


#For the CosSim comparison
#Input -> two strings, user binary and scholarship binary
#Output -> float value, result of CosSim
def comparison(user_bin, input_bin):
    queryList = splitInt(user_bin)
    inputList = splitInt(input_bin)
    cos_sim = dot(queryList, inputList)/(norm(queryList)*norm(inputList))
    return cos_sim

#The key for sorting the list or results
#Input -> dictionary 
#Output -> value of specified field
def sortKey(e):
    return e['Val']


#For filtereing after a query is done, returns a list of id's that we can loop through to pull info of those scholarships
#Input -> Query generator object, string user id, filtering float number
#Output -> List of strings, these are id's that can be used to pull information  
def filter_results(userId):
    filterVal = 0.4
    user = user_Ref.document(userId).get().to_dict()
    userTerms = user.get('Terms')
    query  = scholar_ref.where(u'Terms', u'array_contains_any', userTerms).stream()
    filteredScholar = []
    userBin = user.get('Binary')
    for i in query:
        scholarBin = i.get('Binary')
        if binCompare(userBin, scholarBin) == True:
            value = comparison(scholarBin, userBin)
            if(value >= filterVal):
                scholarInfo = {
                    'ID' : i.id,
                    'Amount' : i.get('Amount'),
                    'Deadline': i.get('Deadline'),
                    'Val': value
                    }
                filteredScholar.append(scholarInfo)
                filteredScholar.sort(key = sortKey, reverse= True)
    return filteredScholar


#Method to compare and see hard conditions
#Input - > 2 strings, user binary, scholarship binary
#Output - > boolean, true if good, false if bad
def binCompare(user_bin, scholar_bin):
    userList = splitInt(user_bin)
    scholarList = splitInt(scholar_bin)
    for y in range(len(userList)):
        if userList[y] < scholarList[y]:
            return False
    return True

#Method to return content of a specific scholarship, id will be supplied from a list of id's that is from filtering in filter_reults method
#Input -> String, Scholarship id
#Output -> List, filled of the scholarship's contents 
def getInfo(scholarId):
    scholarInfo = []
    scholarDir = scholar_ref.document(scholarId).get().to_dict()
    scholarInfo.append(scholarDir.get('Name'))
    scholarInfo.append(scholarDir.get('Amount'))
    scholarInfo.append(scholarDir.get('Deadline'))
    scholarInfo.append(scholarDir.get('Awards Available'))
    scholarInfo.append(scholarDir.get('Direct Link'))
    scholarInfo.append(scholarDir.get('Description'))
    scholarInfo.append(scholarDir.get('Contact Info'))
    return scholarInfo
