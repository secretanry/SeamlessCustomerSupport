import telebot
import json
import threading
import time

token = "6095790820:AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)
group_id = -1001770959685

message1 = "How should I use this bot?"
user_id1 = 103452


def start_message(message, user_id):
    bot.send_message(group_id, message + "\n #" + str(user_id))


def delete_messages_from_group(message):
    time.sleep(0.5)
    bot.delete_message(group_id, message.reply_to_message.id)
    bot.delete_message(group_id, message.id)


@bot.message_handler(content_types=["text"])
def handle_message_from_group(message):
    if message.chat.id == group_id:
        if message.reply_to_message:
            if message.text == "!get":
                replied_message = message.reply_to_message.text
                bot.send_message(message.from_user.id, replied_message)
                bot.send_message(message.from_user.id, "You successfully catch this question to work")
                delete_messages_from_group(message)


start_message(message1, user_id1)
bot.polling()
