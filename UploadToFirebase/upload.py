import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

def upload_to_database_useful():
    cred = credentials.Certificate('key2.json')
    firebase_admin.initialize_app(cred, 
    {
    'databaseURL': 'http//allcollections-6e66c.firebaseio.com/'
    })
    db = firestore.client()
    doc_ref = db.collection(u'applications')
    # Import data
    df = pd.read_csv('CoolCats2.csv')
    tmp = df.to_dict(orient='records')
    list(map(lambda x: doc_ref.add(x), tmp))

upload_to_database_useful()


def upload_to_storage_useless():
    from firebase_admin import credentials, initialize_app, storage
    # Init firebase with your credentials
    cred = credentials.Certificate("key.json")
    initialize_app(cred, {'storageBucket': 'allcollections-6e66c.appspot.com'})

    # Put your local file path 
    fileName = "Metadata/all_0x1a92f7381b9f03921564a437210bb9396471050c.csv"
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("your file url", blob.public_url)