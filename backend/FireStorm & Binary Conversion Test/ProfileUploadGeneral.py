import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from datetime import date
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

cred = credentials.Certificate(
    "testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

user_Ref = db.collection("User")
table_Ref = db.collection("Index Table").document("Terms")
refList = table_Ref.get().to_dict().get('Terms')


#Used to initiation user or update their information, specify when using optional attributes
def updtUser(userEmail,
             gender,
             dob,
             zipC,
             gpa,
             major=' ',
             race=' ',
             ethnicity=' ',
             religion=' ',
             dissabilities=' ',
             sat=' ',
             address1=' ',
             address2=' ',
             address3=' '):

    list1 = [gender]
    list1.append(catAge(dob))
    list1.append(catState(zipC))
    list1.append(catGPA(gpa))

    list2 = [major, race, religion, dissabilities, ethnicity]
    for i in range(len(list2)):
        if list2[i] != ' ':
            list1.append(list2[i])

    if (sat != ' '):
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


def setBin(list):
    binaryInitial = '0' * 807
    usrList = split(binaryInitial)
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
