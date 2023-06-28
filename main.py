import telebot
import json
import threading
import time
import asyncio
import concurrent.futures

token = "6095790820:AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)
group_id = -1001770959685

message1 = "How should I use this bot?"
user_id1 = 103452


async def handle_connection(reader, writer):
    while True:
        try:
            data = yield asyncio.wait_for(reader.readline(), timeout=10.0)
            start_message(data)
            break
        except concurrent.futures.TimeoutError:
            break
    writer.close()


def start_message(message):
    bot.send_message(group_id, message)


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


loop = asyncio.get_event_loop()
server_gen = asyncio.start_server(handle_connection, port=2007)
server = loop.run_until_complete(server_gen)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    loop.stop()
bot.polling()
