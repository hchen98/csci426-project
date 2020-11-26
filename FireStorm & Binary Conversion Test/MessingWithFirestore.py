import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("testing-845eb-firebase-adminsdk-cckoe-bf65029977.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

doc=db.collection("CollectionName")

doc.add({
    u'first' : u'A',
    u'last' : u'b',
    u'born' : 1900,
    u'terms' : {
        u'free',
        u'bye',
        u'coming'
    }
})

doc.add({
    u'first' : u'B',
    u'last' : u'b',
    u'born' : 1815,
    u'terms' : {
        u'then',
        u'bye',
        u'would'
    }
})

doc.add({
    u'first' : u'C',
    u'last' : u'C',
    u'born' : 1920,
    u'terms' : {
        u'can',
        u'bye',
        u'something'
    }
})

doc.add({
    u'first' : u'D',
    u'last' : u'b',
    u'born' : 1800,
    u'terms' : {
        u'hi',
        u'for',
        u'something'
    }
})

doc.add({
    u'first' : u'D',
    u'last' : u'c',
    u'born' : 1950,
    u'terms' : {
       u'hi',
       u'bye',
       u'this'
    }
})

