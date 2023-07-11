import telebot
import json
import threading
import time
import asyncio
import concurrent.futures
from firebase_admin import credentials
import firebase_admin
from firebase_admin import db
import sqlite3

token = "6095790820:AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)
group_id = -1001770959685

message1 = "How should I use this bot?"

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


def start_message(message, mobile_id):
    bot.send_message(group_id, message + "\n" + str(mobile_id))


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


def return_message_with_all_questions(cursor, user_id):
    res = cursor.execute(
        "SELECT question, id from active_questions WHERE user_id=" + str(user_id) + ";").fetchall()
    ready_message = ""
    for i in res:
        ready_message += (str(i[1]) + " ")
        ready_message += i[0]
        ready_message += "\n"
    return ready_message


def check_ticked_questions(cursor, user_id):
    res = cursor.execute(
        "SELECT id from active_questions WHERE ticked=TRUE AND user_id=" + str(user_id) + ";").fetchone()
    return res


def mark_ticked_question(cursor, id, connection):
    res = cursor.execute("SELECT * from active_questions WHERE id=" + str(id) + ";").fetchall()
    if len(res) == 0:
        return False
    cursor.execute("UPDATE active_questions set ticked=TRUE WHERE id=" + str(id) + ";")
    connection.commit()
    return True


def check_login(user_id, cursor):
    res = cursor.execute("SELECT * FROM logged_users WHERE id=" + str(user_id) + ";").fetchall()
    if len(res) == 0:
        return False
    return True


@bot.message_handler(commands=["start"])
def login(message):
    database_connection = sqlite3.connect("botdb")
    cursor = database_connection.cursor()
    if message.chat.id != group_id:
        if not check_login(message.from_user.id, cursor):
            cursor.execute("INSERT INTO logged_users VALUES (" + str(message.from_user.id) + ");")
            database_connection.commit()
            bot.send_message(message.chat.id, "You successfully logged in!")
        else:
            bot.send_message(message.chat.id, "You are already logged in!")
    database_connection.close()


@bot.message_handler(content_types=["text"])
def handle_message_from_group(message):
    database_connection = sqlite3.connect("botdb")
    cursor = database_connection.cursor()
    if message.chat.id == group_id:
        if message.reply_to_message:
            if message.text == "!get":
                if check_login(message.from_user.id, cursor):
                    replied_message = message.reply_to_message.text
                    bot.send_message(message.from_user.id, replied_message)
                    bot.send_message(message.from_user.id, "You successfully catch this question to work")
                    replied_message1 = replied_message.split("\n")
                    cursor.execute("INSERT INTO active_questions (user_id, question, ticked, mobile_id) VALUES(" + str(
                        message.from_user.id) + ", '" + replied_message + "', FALSE, " + replied_message1[-1] + ");")
                    database_connection.commit()
                    delete_messages_from_group(message)
                    if check_ticked_questions(cursor, message.from_user.id) is None:
                        ready_message = return_message_with_all_questions(cursor, message.from_user.id)
                        bot.send_message(message.from_user.id, ready_message)
                        bot.send_message(message.from_user.id, "Please choose a question which you want answer to "
                                                               "now(By sending it's id to the chat).")
                    else:
                        bot.send_message(message.from_user.id, "For now you have active question.")
                else:
                    bot.send_message(message.chat.id, "You are not logged in yet. Please log in by sending /start to "
                                                      "personal messages with bot and try again",
                                     reply_to_message_id=message.id)
    else:
        if message.text.isdigit():
            if check_ticked_questions(cursor, message.from_user.id) is None:
                if mark_ticked_question(cursor, int(message.text), database_connection):
                    bot.send_message(message.from_user.id,
                                     "You successfully mark question " + str(message.text) + " as "
                                                                                             "active",
                                     reply_to_message_id=message.id)
                else:
                    bot.send_message(message.from_user.id, "Incorrect question id, please try again",
                                     reply_to_message_id=message.id)
            else:
                bot.send_message(message.from_user.id, "For now you have active question.",
                                 reply_to_message_id=message.id)
        else:
            ticked_question = check_ticked_questions(cursor, message.from_user.id)
            if ticked_question is None:
                bot.send_message(message.from_user.id, "For now you haven't active question.",
                                 reply_to_message_id=message.id)
                ready_message = return_message_with_all_questions(cursor, message.from_user.id)
                bot.send_message(message.from_user.id, ready_message)
                bot.send_message(message.from_user.id, "Please choose a question which you want answer to "
                                                       "now(By sending it's id to the chat).")
            else:
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button_1 = telebot.types.KeyboardButton("Yes")
                button_2 = telebot.types.KeyboardButton("No")
                markup.add(button_1, button_2)
                answer_1 = ""
                if message.text != "Yes":  # пока ответ не весь, добавляет в ответ и снова спрашивает
                    if message.text != "No":
                        answer_1 = cursor.execute("SELECT answer FROM active_questions WHERE user_id=" + str(
                            message.from_user.id) + " and ticked=TRUE").fetchone()[0]
                        if answer_1 is None:
                            answer_1 = ""
                        answer_more = message.text
                        answer_1 = answer_1 + " " + answer_more
                        cursor.execute("UPDATE active_questions set answer='" + answer_1 + "'WHERE ticked=TRUE;")
                        database_connection.commit()
                        bot.send_message(message.chat.id,
                                         text="Is it all answer? (Yes or No)".format(message.from_user),
                                         reply_markup=markup)
                        bot.send_message(message.from_user.id, answer_1)  # отправляет ответ юзеру
                else:
                    user_id1 = cursor.execute("SELECT mobile_id from active_questions WHERE user_id=" + str(
                        message.from_user.id) + " AND ticked=TRUE;")
                    push_question_answer_to_history(user_id1, ticked_question, answer_1)
                    cursor.execute(
                        "DELETE from active_questions WHERE user_id=" + str(message.from_user.id) + " AND ticked=TRUE;")
                    database_connection.commit()
                    ready_message = return_message_with_all_questions(cursor, message.from_user.id)
                    if ready_message != "":
                        bot.send_message(message.from_user.id, ready_message)
                        bot.send_message(message.from_user.id, "Please choose a question which you want answer to "
                                                               "now(By sending it's id to the chat).")
                    else:
                        bot.send_message(message.from_user.id, "For now you don't have questions, please return to "
                                                               "the group to catch new.")


start_message(message1, 101456)
bot.polling()
