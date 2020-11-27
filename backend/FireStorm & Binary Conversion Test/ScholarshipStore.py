import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#Modify with your own json file, make sure it's in folder with the python file
cred = credentials.Certificate("testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

doc = db.collection("Scholarships")

doc.add({
    u'Name' : u'Some Scholariship',
    u'Amount' : "$100,000",
    u'Deadline' : '10/10/20',
    u'Terms' : {
        u'Caucasian': True,
        u'Spanish': True,
        u'2.1': True
    }
})

doc.add({
    u'Name' : u'Another Scholarship',
    u'Amount' : u'$50',
    u'Deadline' : u'10/10/20',
    u'Terms' : {
        u'Asian': True,
        u'Chinese': True,
        u'3.9': True
    }
})

doc.add({
    u'Name' : u'Different Scholarship',
    u'Amount' : u'$10,000',
    u'Deadline' : u'12/20/20',
    u'Terms' :{
        u'Caucasian': True,
        u'Irish': True,
        u'3.4': True
    }
})

doc.add({
    u'Name' : u'Special Scholarship',
    u'Amount' : u'$1,000,000',
    u'Deadline' : u'1/20/21',
    u'Terms' : {
        u'Caucasian': True,
        u'Spanish': True,
        u'3.5': True
    }
})

doc.add({
    u'Name' : u'Crappy Scholarship',
    u'Amount' : u'$5',
    u'Deadline' : '12/12/20',
    u'Terms' : {
       u'Asian':True,
       u'Japanese':True,
       u'4.0':True
    }
})

