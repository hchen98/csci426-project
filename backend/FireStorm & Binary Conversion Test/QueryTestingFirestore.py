import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)


db = firestore.client()


doc = db.collection("Scholarships")
doc1 = db.collection("Users")


#Generator/Iteratable Object
#Note: Need to have something to identify the current user 
docs1 = doc1.where(u'Name', u'==', u'Paul').stream()

user = {}

#Unfortunately have to loop the single query result, not sure how else
for i in docs1:
    #print(' {} => {}'.format(i.id, i.get('GPA')))
    user = i.to_dict()
    #Prints the values which are used for the binary string
    #print(user.values())


#Figure out the number of general fields for filtering 
a = "Terms."
b = a + str(user.get('Ethnicity'))
c = a + str(user.get('Race'))

#This is the query to filter out the hard conditions, can expand for more conditions
docs = doc.where(b, u'==', True).where(c, u'==', True).stream() 

#print(type(docs1))
#print(type(docs))

#This is to get keys from a dictionary
def getList (dict):
    return dict.keys()


#Print Stuff
for i in docs:
    #This is just printing all contents of a scholarship
    #print(' {} => {}'.format(i.id, i.to_dict()))

    #This is to get the keys from a specific scholarship
    print(getList(i.get('Terms')))



#Update Term list
#This is for when collecting everything, you can update a term list if the scholarshiop exists
def updateTerms(User, term):
    doc.document(User).set({
         u'Terms': {
            term : True
         }
    }, merge = True)


#Used to update the term of the current scholarship, using the doc id, won't normally have this
#User = "An9MraNN1COWiV5UC3Qb"
#Term = "Something"
#updateTerms(User, Term)