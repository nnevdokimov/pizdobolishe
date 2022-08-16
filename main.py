import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import random
import sqlite3
import os
import psycopg2

vk_session = vk_api.VkApi(token="ef398fd1e87b904c38232133a7e8a20f35e044e333549edea9574eb2af3b380b31d740bae73f906848c5a")

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 208798128)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Пить?', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Выпил', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('Статистика', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Участвовать', color=VkKeyboardColor.POSITIVE)



statistic = []
phrases = ["Первое место занимает @id", "На втором месте @id", "И тройку лидеров закрывает @id"]


# Heroku DataBase
DB_URI = 'postgres://venhaufbqxsuff:e5e158ad10abc8813621cc3477c4c12a07d22e82ff40d6d2a45e8a56af8d0753@ec2-100-26-39-41.compute-1.amazonaws.com:5432/df6oldn5b639fa'
conn = psycopg2.connect(DB_URI, sslmode='require')
cur = conn.cursor()


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        vars1 = ['[club208798128|@pizdobolishe] клавиатура', '[club208798128|@pizdobolishe] клава', '[club208798128|@pizdobolishe] Клавиатура', '[club208798128|@pizdobolishe] Клава']
        # print(str(event))
        message = event.message
        print(event.message)
        if event.message.text in vars1:
            if event.from_chat:
                vk.messages.send(
                    keyboard=keyboard.get_keyboard(),
                    key=('21b7e67abf6b938c8223242c37b4ff873efe1453'),
                    server=('https://lp.vk.com/wh183415444'),
                    ts=('3539'),
                    random_id=get_random_id(),
                    message='Держи',
                    chat_id=event.chat_id
                )
        if '[club208798128|@pizdobolishe] Пить?' in event.message.text:
            answ = ['Харе бухать, алкаш', 'Все говорят, что пить нельзя, а я говорю, что буду', 'Выпей за весь наш цыганский табор!', 'Думаю, что сегодня не стоит']
            if event.from_chat:

                vk.messages.send(
                    key=(''),
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message=answ[random.randint(0, 3)],
                    chat_id=event.chat_id
                )
        if '[club208798128|@pizdobolishe] Выпил' in event.message.text:
            pers_id = event.message.from_id

            count = 0
            cur.execute("SELECT user_id FROM counter WHERE user_id = ?;",
                           [str(pers_id)])
            user = cur.fetchone()  # None или кортеж с данными

            if user is None:
                vk.messages.send(
                    key=(''),
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message="Ты еще не зарегистрировался!",
                    chat_id=event.chat_id
                )
            else:
                cur.execute("SELECT count FROM counter WHERE user_id = ?;", [str(pers_id)])
                num = cur.fetchone()

                cur.execute("UPDATE counter SET count = ? WHERE user_id = ?;",
                               [num[0] + 1, str(pers_id)])
                conn.commit()
                vk.messages.send(
                    key=(''),
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message="Ваше здоровье, @id" + str(pers_id) + " (Алкаш)",
                    chat_id=event.chat_id
                )

        if '[club208798128|@pizdobolishe] Статистика' in event.message.text:
            cur.execute("SELECT user_id, count FROM counter ORDER BY count DESC;")
            results = cur.fetchmany(3)
            conn.commit()

            print(results)
            for i in range(0,3):
                vk.messages.send(
                    key=(''),
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message=phrases[i] + str(results[i][0]) + " выпив " + str(results[i][1]) + " раз",
                    chat_id=event.chat_id
                )
        if '[club208798128|@pizdobolishe] Участвовать' in event.message.text:

            cur.execute("SELECT user_id FROM counter WHERE user_id = ?;",
                           [str(event.message.from_id)])
            user = cur.fetchone()  # None или кортеж с данными

            if user is None:
                db_table_val(user_id = str(event.message.from_id), count=0, time=-1)

                vk.messages.send(
                    key=(''),
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message="Добро пожаловать в наши ряды!",
                    chat_id=event.chat_id
                )
                conn.commit()
            else:
                vk.messages.send(
                    key=(''),
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message="Ты уже участвуешь!",
                    chat_id=event.chat_id
                )
