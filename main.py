import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import random


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

statistic = {}

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
            if pers_id in statistic.keys():
                statistic[pers_id] += 1
            else:
                statistic[pers_id] = 1
            vk.messages.send(
                key=(''),
                server=(''),
                ts=(''),
                random_id=get_random_id(),
                message="Ваше здоровье, @id" + str(pers_id) + " (Алкаш)",
                chat_id=event.chat_id
            )
        if '[club208798128|@pizdobolishe] Статистика' in event.message.text:
            vk.messages.send(
                key=(''),
                server=(''),
                ts=(''),
                random_id=get_random_id(),
                message= "Поздравляю, за этот месяц ты выпил: " + str(statistic[event.message.from_id]) + " раз",
                chat_id=event.chat_id
            )