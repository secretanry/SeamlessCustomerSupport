import telebot
import json
import threading
import time
import asyncio
import concurrent.futures
from firebase_admin import credentials
import firebase_admin

token = "6095790820:AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)
group_id = -1001770959685

message1 = "How should I use this bot?"
user_id1 = 103452

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "seamless-customer-support",
    "private_key_id": "0faab57fee0cad9be7499f6713a77787392ffd15",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQC5mgVcWbXyOhYJ\n7fdMxn8NRkXRHJAZk1cQRdYLYUtyIiZus9OhSiIAawLUJzPnjWTjuArua7BIhIKm\nB7FVLrxxg55tMS38OCWow9d7QLJiGARFu55YTpU6p/NAedGPbRwS74HTMyZqmB9g\nf5F1oMw2P5YE22vkFWGZExVR397TDiGSFdQnLHcuLc5qo76+p/rtyiluLfgNyurS\nZLnVl8BEywXyTmV+/FE2l8uPxqmIHJCf0+yOOzhpM9mhyvoUuRXwDCo5fGcJ5oRl\nGQfKIrvg9M4Vj/SU+P//UDVEBZTl0E05O3xma+gZibxWh1t8iHwhF32WWv+PPg+z\n7NP7EpWzAgMBAAECgf9I1zjK55ePtVpaTwpG2ye2hnRnnSh4LGo7JeIIdzXZlTMl\nxrjPZt9atA4r6a9IA712kogSGUB/caAQ8nt5EPynzGlv2pH1W5tN6+jDwc2LwQ5k\nqhBNxSAXTod0bB6HOqVvm9sbgLtWv+SfoEQMuPCZhvGVyTxSZXsziTq2qwebF9pu\ndJxcmS/jHmLKiSgGuGxsR36LdiPK79F5cbXMG9Uyv0mUUK/qkAxVAHXskyp9gE+n\nGOC6tOSbBIuTgycaaXjBtT4ZXMBF6TadmA7yHqVbQysBztgbyGjapDEyDQ249IBl\nvfXbNMOPtityGvBAp0mhVna0LOCMrMlf9Vf63yECgYEA+0Se9DizdhEhoe67Z3sx\nt+af0JiCU9CODJ8zZGQsrXOrYb+30EA8tWa5FlFFMbwKr4KhVtoq0upzWAVmdCd1\nRhJOsRjWymZiePdhu6vY6L0VmK4d9bJ6nM1+mSZeZD5l4vsHs7qlMwem4R1XH2VF\nT2T+QgPN/4uUeB+Njb57msUCgYEAvRjRcju6mo4t83VcyKRM8nmvDeRSXZie+7p3\nwhemeGeggJe4+fnqRBlVyyp7F9soHlLdTGcvCR8N6VC0gHYq9yfGKxSdJo+LDHwl\nZIXac/M+ZZRSTLyf1xR2NpxvGT/5bpc2K2sNXuFPwcrGCbfHC1ZiIuLCOh7iJAr6\n0hWr1hcCgYEAvYWMv3jlI/DYBWQkRnFNlwCFGrlt0/pCqpKKGPbWHB5a7mfFJXbO\nU6Ufhg3WuySyip9lQjVch6n/Ri0MkiAQ/MFiSYIKwK9pJwSw2vVLroCwgXETd/cf\nNJZrHukp2UKXZxUhQhdN86eZ38JZrHyeQrxSa0ijYFTPr6tdAcTjRmECgYBJ9/9W\nFA82jg9jgLE+uyZuYzMa2AlwG1d1WMen4OB5kO+z3aW6AwykftSUmJV2C4Bx/DAc\nxvAbPU6PycYRyiecbq6SA4pFnzjhNV7bJ5EAclIiIhbfdZmA5LwpOKAs3F2R6QyD\nh2i/iJtOTyeQfZca1DunMdSQL6x+NN1QeLGzGQKBgBeuxozZ50ZLORXkI1KyMhlh\ntNovpoLwOzZ1/Ptfl66YG7zhhGEGsSiFosUQSEiW9vw1BSV5OjJ2GAlPgMMneAah\nlPDhkYjzpoQTHPTqXImGlfZD6ihWqhJfH3Y+dxI0l3B0n+lSP76KYt0u5TQF1uh4\nvfX1e+gQEt2eDjF1KBxz\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-j8s4r@seamless-customer-support.iam.gserviceaccount.com",
    "client_id": "113425141176073502133",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-j8s4r%40seamless-customer-support.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seamless-customer-support-default-rtdb.europe-west1.firebasedatabase.app/'
})


# async def handle_connection(reader, writer):
#     while True:
#         try:
#             data = yield asyncio.wait_for(reader.readline(), timeout=10.0)
#             start_message(data)
#             break
#         except concurrent.futures.TimeoutError:
#             break
#     writer.close()


def start_message(message):
    bot.send_message(group_id, message)


def push_question_answer_to_history(user_id, question, answer):
    # Get the reference to the 'history' node in the database
    ref_history = firebase_admin.db.reference('history')

    # Push a new question-answer pair to the user's history
    ref_history.child(user_id).push({
        'A question': question,
        'An answer': answer
    })


def delete_messages_from_group(message):
    time.sleep(0.5)
    bot.delete_message(group_id, message.reply_to_message.id)
    bot.delete_message(group_id, message.id)


@bot.message_handler(commands=["start"])
def login(message):
    bot.send_message(message.chat.id, "You successfully logged in!")


@bot.message_handler(content_types=["text"])
def handle_message_from_group(message):
    global answer_1
    if message.chat.id == group_id:
        if message.reply_to_message:
            if message.text == "!get":
                # if '/start' in message.from_user.messages:
                replied_message = message.reply_to_message.text
                bot.send_message(message.from_user.id, replied_message)
                bot.send_message(message.from_user.id, "You successfully catch this question to work")
                delete_messages_from_group(message)
            # else:
            #     bot.send_message(group_id, "You are not logged in, please send /start to bot and try again")
    else:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = telebot.types.KeyboardButton("Yes")
        button_2 = telebot.types.KeyboardButton("No")
        markup.add(button_1, button_2)
        # bot.send_message(message.chat.id, text="Is it all answer? (Yes or No)".format(message.from_user),
        #                  reply_markup=markup)

        if message.text != "Yes":  # пока ответ не весь, добавляет в ответ и снова спрашивает
            if message.text != "No":
                answer_more = message.text
                answer_1 = answer_1 + " " + answer_more
                bot.send_message(message.chat.id, text="Is it all answer? (Yes or No)".format(message.from_user),
                                 reply_markup=markup)

                bot.send_message(message.from_user.id, answer_1)  # отправляет ответ юзеру
        else:
            push_question_answer_to_history(user_id1, answer_1)


answer_1 = ""
start_message(message1)
# loop = asyncio.get_event_loop()
# server_gen = asyncio.start_server(handle_connection, port=2007)
# server = loop.run_until_complete(server_gen)
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
# finally:
#     server.close()
#     loop.stop()
bot.polling()
