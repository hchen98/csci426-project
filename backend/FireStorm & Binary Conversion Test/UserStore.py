import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

doc = db.collection("Users")

doc.add({
    u'Name' : u'Paul',
    u'Race' : u'Caucasian',
    u'Ethnicity' : u'Spanish',
    u'GPA' : u'3.4'
})