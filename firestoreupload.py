# python firestoreupload.py --credentials=credentials.json --file=output/results.json --collection=DetectedObjects

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import argparse
import datetime

def main():
    parser = argparse.ArgumentParser(description="Helper to run Ultralytics YOLO on images")
    parser.add_argument('--file', '-f', type=str, default='results.json', help='Input json file path')
    parser.add_argument('--collection', '-c', type=str, default='DetectedObjects', help='Collection to use')
    parser.add_argument('--credentials', '-i', type=str, default='credentials.json', help='Firebase credentials json')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()

    cred = credentials.Certificate(args.credentials)
    
    firebase_admin.initialize_app(cred)

    with open(args.file) as f:
        data = json.load(f)

    doc_data = {
        'detected': data,
        'date': int(datetime.date.today().strftime("%Y%m%d")),
        'datetime': int(datetime.datetime.now().strftime("%Y%m%d%H%M%S")),
    }

    db = firestore.client()
    doc_ref = db.collection(args.collection).document()
    doc_ref.set(doc_data)

if __name__ == '__main__':
    main()