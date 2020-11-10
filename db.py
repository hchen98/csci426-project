from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

emails = []

with open("output.txt", encoding="utf-8", mode="r") as lines:
    for line in lines:
        emails.append(line)

    lines.close()


config = {
  "apiKey": "AIzaSyDCYPgLjlChuJbC-FMGyNOYkaao8ULyYWE",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://reactnativefirebase-ec822.firebaseio.com",
  "storageBucket": "reactnativefirebase-ec822.appspot.com",
#   "serviceAccount": "path/to/serviceAccountCredentials.json",
}

# # Use the application default credentials
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#   'projectId': "reactnativefirebase-ec822",
# })

# db = firestore.client()


# Use a service account
cred = credentials.Certificate('google-service-account.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def insert_collection(data):
    # Add a new document
    db = firestore.Client(credentials=config)
    doc_ref = db.collection(u'hosts').document(u'engineering')
    doc_ref.set({
        u'email': data,
    })

def query_collection(coll_name):
    # Then query for documents
    users_ref = db.collection(coll_name)

    for doc in users_ref.stream():
        print(u'{} => {}'.format(doc.id, doc.to_dict()))