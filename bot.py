import telebot
import random
from telebot import types
import os
import asyncio
import time 
import sqlite3

bot = telebot.TeleBot('5230072438:AAFFvNqRKy6wMasj3opxHymx8qBSXAglktg')

tutor = open('media/tutorial.png', 'rb')
conn = sqlite3.connect('db/milkadmin.db', check_same_thread=False)
cursor = conn.cursor()
admins = [1399518545, 1023868925, 5187271167, 809626602, 5036463357, 1947620382, 5078105628, 789948896, 1951874311, 1459362307, 5172657386, 1420774826, 5129107819, 1069404358, 713102231, 5194563375, 1707532183, 1397474781, 2105248374, 1398238093, 1707592399]

@bot.message_handler(commands=["start", "help"])
def start(message):
	markup = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton("Помощь и все про бота.", url='https://telegra.ph/Pomoshch-po-botu-MilkAdmin-08-14')
	markup.add(button1)
	bot.send_message(message.chat.id, f'*Приветствую {message.from_user.username}! Нажми на кнопку снизу для помощи по боту!*', reply_to_message_id=message.message_id, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def tools(message):
	if message.text.lower() == "!бан":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '*❌Команду бан нужно использовать в ответ на сообщение нарушителя!❌*', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
			 	bot.reply_to(message.reply_to_message, f'🔒*@{user_name} забанил @{user_nametwo}*🔒', parse_mode='Markdown')
	if message.text.lower() == "!разбан":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду разбан нужно использовать в ответ на сообщение человека которого хотите разбанить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
			 	bot.reply_to(message.reply_to_message, f'🔓*@{user_name} разбанил @{user_nametwo}*🔓', parse_mode='Markdown')
	if message.text.lower() == "!кик":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду кик нужно использовать в ответ на сообщение человека которого хотите кикнуть!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
			 	bot.reply_to(message.reply_to_message, f'🚪👈*@{user_name} кикнул @{user_nametwo}*👉🚪', parse_mode='Markdown')
	if message.text == '/tutorial':
	   	bot.send_photo(message.chat.id, tutor, reply_to_message_id=message.message_id)
	if message.text == '/tutorial@MilkAdminBot':
	   	bot.send_photo(message.chat.id, tutor, reply_to_message_id=message.message_id)
	if message.text.lower() == f"!мут 1м":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на минуту*🔇', parse_mode='Markdown')
			 	time.sleep (60)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} на минуту прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!мут 5м":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на 5 минут*🔇', parse_mode='Markdown')
			 	time.sleep (300)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} на 5 минут прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!мут 30м":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на полчаса*🔇', parse_mode='Markdown')
			 	time.sleep (1800)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} полчаса прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!мут 1ч":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на час*🔇', parse_mode='Markdown')
			 	time.sleep (3600)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} на час прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!мут 2ч":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на два часа*🔇', parse_mode='Markdown')
			 	time.sleep (7200)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} на два часа прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!мут 4ч":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на 4 часа*🔇', parse_mode='Markdown')
			 	time.sleep (14400)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} на 4 часа прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!мут 8ч":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на 8 часов*🔇', parse_mode='Markdown')
			 	time.sleep (14400)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} на 8 часов прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!мут 24ч":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} на день*🔇', parse_mode='Markdown')
			 	time.sleep (86400)
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
			 	bot.reply_to(message.reply_to_message, f'🔊*Мут от @{user_name} для @{user_nametwo} на день прошел*🔊', parse_mode='Markdown')
	if message.text.lower() == f"!размут":
		bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True)
		user_name = message.from_user.username
		user_nametwo = message.reply_to_message.from_user.username
		bot.reply_to(message.reply_to_message, f'🔊*@{user_name} размутил @{user_nametwo}*🔊', parse_mode='Markdown')
	if message.text.lower() == "!бан 1д":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '*❌Команду бан нужно использовать в ответ на сообщение нарушителя!❌*', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
			 	bot.reply_to(message.reply_to_message, f'🔒*@{user_name} забанил @{user_nametwo} на 1 день*🔒', parse_mode='Markdown')
			 	time.sleep(86400)
			 	bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
			 	bot.send_message(message.chat.id, f'*🔓Бан на день от @{user_name} для @{user_nametwo} прошёл*🔓', parse_mode="Markdown")
	if message.text == '!ping':
		bot.reply_to(message, "*👷worker👷*", parse_mode="Markdown")
	if message.text.lower() == f"!мут навсегда":
		if not message.reply_to_message:
			bot.send_message(message.chat.id, '❌*Команду мут нужно использовать в ответ на сообщение человека которого хотите замутить!*❌', reply_to_message_id=message.message_id, parse_mode="Markdown")
		else:
			user_name = message.from_user.username
			user_nametwo = message.reply_to_message.from_user.username
			if message.from_user.id:
			 	bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages = False, can_send_media_messages = False, can_send_other_messages = False)
			 	bot.reply_to(message.reply_to_message, f'🔇*@{user_name} замутил @{user_nametwo} навсегда*🔇', parse_mode='Markdown')
			 	
bot.infinity_polling(none_stop=True)