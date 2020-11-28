import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#CosSim Calc
from numpy import dot
from numpy.linalg import norm

cred = credentials.Certificate("testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

scholar_ref=db.collection(u"Scholarships2")
user_ref = db.collection(u'Users')

#Update the document reference with the current user id
user = user_ref.document(u'VS02Ok5RyWD63BrbnzFY')

#Playing with getting the term list 
#doc_info = user.get(field_paths={'Name'}).to_dict().get('Name')
#term_list = user.get().to_dict().get('Terms')
#print(term_list)



#if doc_info.exists:
 #   print(f'Document data: {doc_info')
#else:
 #   print(u'No such document!')

##########################################     METHODS    #######################
# Methods for binary filtering

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
#Input -> Query generator object, filtering number
#Output -> List of strings, these are id's that can be used to pull information  
def filter_results(query, filterVal):
    for i in query:
        #print(' {} => {}'.format(i.id, i.get('GPA')))
        scholBin = i.get('Binary')
        value = comparison(scholBin, userBin)
        if(value > filterVal):
            scholid = i.id
            filteredSchol.append(scholid)
    return filteredSchol
#
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

print(getInfo('JPa6dkCtt8doqLDkMp2m'))
##################################################################################
# update this properly with example binary comparison 
userBin = user.get().to_dict().get('Binary')

#This is the query, modify it a bit more based on user fields
query = scholar_ref.where(u'Terms', u'array_contains_any', [u'Something']).stream()

filterVal = 0.5
filteredSchol = []