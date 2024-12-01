from google.cloud import firestore
import datetime
import os

db = firestore.Client(project=os.getenv("PROJECT_ID"))

def save_feedback(module,feature,sentiment, comment):
    data = {
        "module": module,
        "feature": feature,
        "sentiment": sentiment,
        "comment": comment
    }
    db.collection("feedbacks").document(str(datetime.datetime.now(tz=datetime.timezone.utc))).set(data)
