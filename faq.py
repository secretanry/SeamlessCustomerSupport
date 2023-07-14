from firebase_admin import firestore
from google.cloud.firestore import CollectionReference
import firebase_admin
from firebase_admin import credentials
from sentence_transformers import SentenceTransformer, util
import torch
import telebot
import time
import datetime
from google.api_core import datetime_helpers

# json file Firebase config
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "chatbot-73526",
    "private_key_id": "8ad1ab03c0df9ca5bd39d5c5e87d9fd85fca3c06",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDMtUjzYK+W+jLC\nfWaCxdV//WoS9RmF6ecJbMtEdTWoj4sXo2LN/0VgJx7nWlquY2BeB6PeDrJOofQq\nWnzH97I/OU1dl/VLgEfBcajcrXouZ5G6HvRH9k7+Y+2bXanMbr1VCAsAwt/6jRdO\nzrHJoVJEueizfxqUWp+QcOUmJczuQnPgT+HCgKC/hrnCDaRN/Ej66WOBqH8WfEHe\ngaASN7sKgBn4YQTN7PTN17HFu37OF22NE7xvwiaNWSWH1rJYDNFEyCuXCh5wggfy\nDTgmd3xtmYllrCtV1eHk/nq4nJgGCNQoTanW+2sJblS9bc90tyZQNPk6zgpk3ECq\nVarfOYerAgMBAAECggEADoKtLJ9GYw/SKEomSY/Hbf6jFbvs9rqZR2hAUlZymsOu\nCttohgyZuNKdFK4pbmIZ8yBcg8GL7xn4ykXGwY/zwRqJOuCqIRNzQqmRXC8p0X9C\n66wFCdLST6L6tUAi6JxS7GOZEBFAOizlIY9yN8YpJDj/XzXbxvdThzQRci5Mw/iu\ndKskljxpqkDtThUjGQeNZ32VkL2KaHgy/2i/s921Vp2xtpxd3Et86PtMTpDumr3x\nKmt1Elf3CnBlF7ik1+n/8YwCUB4x/mOOcevVvM7Z2aFzRfEG78/dFHhWp6CnKvD5\nEq00HoKXMNyZz7yFpE97FsUrVuGIo5cZ8U7bJ30g9QKBgQDmPUdYukynvyg7IW5D\ncstUm4uA4H8dzMWgGEj1nd0g8JXT7gWXIxpXoGrJpAg9i4LIPrTYIA4AkDQRcPI4\nKOOySMHYR51NiAgMssgHYwQc04/Adj5n5kBaoK9McGjZMA1NGp8syLMo2LzIRpTg\n94g0TodzM/FRZkQtz9NOhZFobwKBgQDjnLfYLCkRIRHymYtkX7cr6wlK9PlDa1my\nFHzFpL4rUW8JNoVk3mlLA7KoDLD1ZUSbllx+wot8WNGsEYGqrN5ZOueOS59JucxL\nBBHghQl5+LIWVtIXtBfc1Gs5MfMPnh+tUSwr5hj+PuwzXXPC/b3Q5qIxaDdDMj5i\nkiop9p0ahQKBgQC9C2Wwmc9lENUEsC9sHC6NuuWxnSNioYdHK4mEeuldKY2sJMzc\nSwtPFb148UF+3zU0HCC7MJ6uobjO9VE9AX3sHkdjwXGMfnw1iPoq7ocq8B8hZTVa\ndDk08Kje95Fve0AApjI6QFSy3jsrqqCFk1l3sV8QHX8wWerzPqh+2bcJ6wKBgQCf\n/uXsev5TIB/xnKUzZWTo5kqd+h3NmoRufaBHfkp/QLsAiuaxxPXW2T6YinNJzGmx\nxLw4DqDmQ7j/bz7qrqGNr65dhCLwPD6y7KV0YZALwRnOQjFkoB+2B0tn5QiqjchO\nmKSoJxKihbCbWrGo+5yWX8jbWhqejY700zH4VXaR0QKBgAwqTKsO6U54KJdy5wEY\nS36f57qe2yBYfVGTnl37mvIPsqYam88Ij6chmtXa/y122h0gpKR+xstC7QZAXpbt\n6IbxKBqp8LcL9ITHXQQTL1u6v838EYWIrhB6UeIcHHDyiWPmqm4uM+9G+y8M0ewR\nVpsnQRJ31zwSSvCgKGVIjBuh\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-oi95f@chatbot-73526.iam.gserviceaccount.com",
    "client_id": "117384726188781580536",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-oi95f%40chatbot-73526.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

firebase_admin.initialize_app(cred)

db = firestore.client()

ref_history: CollectionReference = db.collection('history')
ref_messages: CollectionReference = db.collection('messages')

model = SentenceTransformer('all-MiniLM-L6-v2')

token = "6095790820:AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)
group_id = -1001770959685

# Sending message to the volunteer's group 
def start_message(message, mobile_id, answer=""):
    if answer == "":
        a = bot.send_message(group_id,
                             message + "\n" + str(mobile_id))
    else:
        a = bot.send_message(group_id, message + "\n" + str(mobile_id) + "\n" + "An answer to the similar question: " + answer)
    return a

# Analysis of the question on the FAQ
def check_FAQ(question):
    all_questions_data = [doc.to_dict() for doc in ref_history.stream()]

    if all_questions_data:
        all_questions = [item['question'] for item in all_questions_data]
        all_answers = [item.get('text', '') for item in all_questions_data]
        question_embedding = model.encode(question, convert_to_tensor=True)
        all_questions_embeddings = model.encode(all_questions, convert_to_tensor=True)

        cos_scores = util.pytorch_cos_sim(question_embedding, all_questions_embeddings)[0]
        top_results = torch.topk(cos_scores, k=1)

        for score, idx in zip(top_results[0], top_results[1]):
            if score.item() > 0.7:  # If the cosine similarity is greater than 70%
                return True, all_answers[idx]

    return False, None

# Converting a Firestore Timestamp to a python datetime object
def timestamp_to_datetime(timestamp):
    return datetime_helpers.to_milliseconds(timestamp) / 1000.0


# Save the timestamp of the last processed message
last_processed_timestamp = datetime.datetime.now()

# Message processing function
def process_question(doc_snapshot, changes, read_time):
    global last_processed_timestamp

    for doc in doc_snapshot:
        doc_dict = doc.to_dict()  # Convert the DocumentSnapshot into a dict
        if doc_dict is not None:
            message_timestamp = doc_dict.get('createdAt')  # Get the timestamp of the message

            # Convert Firestore Timestamp to datetime
            message_datetime = datetime.datetime.fromtimestamp(timestamp_to_datetime(message_timestamp))

            # If the message is newer than the last processed message
            if message_datetime > last_processed_timestamp:
                question = doc_dict.get('text')
                user_id = doc_dict.get('uid')

                if question and user_id:
                    FAQ_status, similar_answer = check_FAQ(question)

                    if FAQ_status:
                        start_message(question, user_id, similar_answer)
                    else:
                        start_message(question, user_id)

                # Update the last processed timestamp
                last_processed_timestamp = message_datetime


# Listen to updates in messages
ref_messages.on_snapshot(process_question)

while True:
    time.sleep(10)
