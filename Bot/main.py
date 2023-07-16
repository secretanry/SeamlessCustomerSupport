import telebot
import time
from firebase_admin import credentials, firestore
import firebase_admin
from firebase_admin import db
import sqlite3
from firebase_admin import firestore
from datetime import datetime

from google.cloud.firestore import CollectionReference

token = "6095790820:AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)
group_id = -1001770959685
admin_id = 1028893821

message1 = "How should I use this bot?"

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


def start_message(message, mobile_id):
    bot.send_message(group_id, message + "\n" + str(mobile_id))


def push_question_answer_to_history(user_id, question, answer):
    doc_ref = ref_history.document()
    doc_ref.set({
        'uid': user_id,
        'question': question,
        'text': answer,
        'createdAt': firestore.firestore.SERVER_TIMESTAMP  # Firestore Timestamp
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
        suggested = ""
        ready_message += "*" + (str(i[1]) + "* ")
        temp = i[0].split("\n")
        if "An answer to the similar question:" in temp[-1]:
            suggested = ("`" + temp[-1].split(":")[-1] + "`")
            temp = temp[:-2]
        else:
            temp = temp[:-1]
        temp = "\n".join(temp)
        ready_message += temp
        ready_message += "\n"
        if suggested != "":
            ready_message += suggested
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


@bot.message_handler(commands=["export"])
def export_history():
    pass


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
                    if "An answer to the similar question:" in replied_message:
                        default_message = ":".join(replied_message.split(":")[:-1]) + ":"
                        ans = "`" + replied_message.split(":")[-1] + "`  (You can easily copy this suggested answer to " \
                                                                     "clipboard using one click)"
                        bot.send_message(message.from_user.id, default_message + ans, parse_mode="MARKDOWN")
                    else:
                        bot.send_message(message.from_user.id, replied_message)
                    bot.send_message(message.from_user.id, "You successfully catch this question to work")
                    replied_message1 = replied_message.split("\n")
                    if "An answer to the similar question:" not in replied_message[-1]:
                        cursor.execute("INSERT INTO active_questions (user_id, question, ticked, mobile_id) VALUES(" + str(
                            message.from_user.id) + ", '" + replied_message + "', FALSE, '" + replied_message1[-1] + "');")
                    else:
                        cursor.execute(
                            "INSERT INTO active_questions (user_id, question, ticked, mobile_id) VALUES(" + str(
                                message.from_user.id) + ", '" + replied_message + "', FALSE, '" + replied_message1[
                                -2] + "');")
                    database_connection.commit()
                    delete_messages_from_group(message)
                    if check_ticked_questions(cursor, message.from_user.id) is None:
                        ready_message = return_message_with_all_questions(cursor, message.from_user.id)
                        bot.send_message(message.from_user.id, ready_message, parse_mode="MarkdownV2")
                        bot.send_message(message.from_user.id, "Please choose a question which you want answer to "
                                                               "now(By sending it's id to the chat).")
                    else:
                        bot.send_message(message.from_user.id, "For now you have active question.")
                else:
                    bot.send_message(message.chat.id, "You are not logged in yet. Please log in by sending /start to "
                                                      "personal messages with bot and try again",
                                     reply_to_message_id=message.id)
            elif message.text == "!answer":
                # m = message.reply_to_message
                # a = message.reply_to_message.message_thread_id - message.id
                if "An answer to the similar question:" in message.reply_to_message.text:
                    ans = message.reply_to_message.text.split("\n")[-1].split(":")[-1]
                    quest = "\n".join(message.reply_to_message.text.split("\n")[:-2])
                    uid = message.reply_to_message.text.split("\n")[-2]
                    push_question_answer_to_history(uid, quest, ans)
                    delete_messages_from_group(message)


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
                bot.send_message(message.from_user.id, ready_message, parse_mode="MarkdownV2")
                bot.send_message(message.from_user.id, "Please choose a question which you want answer to "
                                                       "now(By sending it's id to the chat).")
            else:
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button_1 = telebot.types.KeyboardButton("Submit")
                markup.add(button_1)
                answer_1 = ""
                if message.text != "Submit":  # пока ответ не весь, добавляет в ответ и снова спрашивает
                        answer_1 = cursor.execute("SELECT answer FROM active_questions WHERE user_id=" + str(
                            message.from_user.id) + " and ticked=TRUE").fetchone()[0]
                        if answer_1 is None:
                            answer_1 = ""
                        answer_more = message.text
                        answer_1 = answer_1 + " " + answer_more
                        cursor.execute("UPDATE active_questions set answer='" + answer_1 + "'WHERE ticked=TRUE;")
                        database_connection.commit()
                        bot.send_message(message.chat.id,
                                         text="Is it all answer? (Click submit if it is)".format(message.from_user),
                                         reply_markup=markup)
                        bot.send_message(message.from_user.id, answer_1)  # отправляет ответ юзеру
                else:
                    data = cursor.execute(
                        "SELECT mobile_id, question, answer from active_questions WHERE user_id=" + str(
                            message.from_user.id) + " AND ticked=TRUE;").fetchone()
                    temp = data[1].split("\n")
                    temp = temp[:-1]
                    temp = "\n".join(temp)
                    push_question_answer_to_history(str(data[0]), temp, data[2])
                    cursor.execute(
                        "DELETE from active_questions WHERE user_id=" + str(message.from_user.id) + " AND ticked=TRUE;")
                    database_connection.commit()
                    ready_message = return_message_with_all_questions(cursor, message.from_user.id)
                    bot.send_message(message.from_user.id, "You successfully submitted your answer.")
                    if ready_message != "":
                        bot.send_message(message.from_user.id, ready_message, parse_mode="MarkdownV2")
                        bot.send_message(message.from_user.id, "Please choose a question which you want answer to "
                                                               "now(By sending it's id to the chat).")
                    else:
                        bot.send_message(message.from_user.id, "For now you don't have questions, please return to "
                                                               "the group to catch new.")


# start_message(message1, 101456)
bot.polling()
