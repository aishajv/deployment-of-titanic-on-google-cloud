import json
import firebase_admin
from firebase_admin import credentials, firestore


def insertSurvivalPrediction(jsonString):
    print("Inserting ModelPrediction into CloudStore")
    cred = credentials.Certificate("../serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    data = json.loads(jsonString)
    data_emailID = data['EmailID']
    data_passengerName = data['PassengerName']
    data_prediction = data['Prediction']
    doc_ref = db.collection('ModelPrediction').document(data_emailID)

    doc_ref.set({

        'EmailID': data_emailID,
        'PassengerName': data_passengerName,
        'Prediction': data_prediction

    })


# if __name__ == "__main__":
#    insertSurvivalPrediction('{"PassengerName": "D", "Prediction": "Dead", "EmailID": "d.e@gmail.com"}')
