import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#CosSim Calc
from numpy import dot
from numpy.linalg import norm

cred = credentials.Certificate("testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

scholar_ref=db.collection(u"ScholarshipHub")
user_ref = db.collection(u'Users')

##########################################     METHODS    #######################
# Methods for binary filtering

#Split method
#Input -> String, ideally the binary string
#Output -> integer list to be used for CosSim
def split(word):
    stringlist = [char for char in word]
    intlist = [int(i) for i in stringlist]
    return intlist


#For the CosSim comparison
#Input -> two strings, user binary and scholarship binary
#Output -> float value, result of CosSim
def comparison(user_bin, input_bin):
    queryList = split(user_bin)
    inputList = split(input_bin)
    cos_sim = dot(queryList, inputList)/(norm(queryList)*norm(inputList))
    return cos_sim


#For filtereing after a query is done, returns a list of id's that we can loop through to pull info of those scholarships
#Input -> Query generator object, string user id, filtering float number
#Output -> List of strings, these are id's that can be used to pull information  
def filter_results(userId):
    filterVal = 0.4
    user = user_ref.document(userId).get().to_dict()
    userTerms = user.get('Terms')
    query  = scholar_ref.where(u'Terms', u'array_contains_any', userTerms).stream()
    filteredScholar = []
    userBin = user.get('Binary') 
    for i in query:
        scholarBin = i.get('Binary')
        if binCompare(userBin, scholarBin) == True:
            value = comparison(scholarBin, userBin)
            if(value > filterVal):
                scholarid = i.id
                filteredScholar.append(scholarid)
    return filteredScholar

#Method to compare and see hard conditions
#Input - > 2 strings, user binary, scholarship binary
#Output - > boolean, true if good, false if bad
def binCompare(user_bin, scholar_bin):
    userList = split(user_bin)
    scholarList = split(scholar_bin)
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

############################### Testing Stuff #########################


#Example for comparisons 
#print(filter_results('some email'))
