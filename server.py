import telebot
from telebot import types
import time

client = telebot.TeleBot("5774902354:AAE10duoD9PnVEm7DFPbgqLtHNqgRDEQR6c")


# Создание команды start и ответ на нее с кнопкой "Начать"
@client.message_handler(commands=["start"])
def start(message):
    makrup_inline = types.InlineKeyboardMarkup()
    markup_start = types.InlineKeyboardButton(text="Продолжить", callback_data="start")
    makrup_inline.add(markup_start)
    client.send_message(message.chat.id,
                        "<b>Привет👋Мы рады, что ты присоединился (-ась).</b>\nЯ помогу тебе узнать пароль от закрытого wi-fi.\n<b>Жми 'продолжить'</b>, если хочешь начать.",
                        reply_markup=makrup_inline, parse_mode="html"
                        )


# Обработка кнопки "Продолжить"
@client.callback_query_handler(func=lambda call: True)
def answer_start(call):
    if call.data == "start":
        markup_reply_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_phys = types.KeyboardButton("Отправлено!")
        markup_reply_1.add(markup_phys)
        client.send_message(call.message.chat.id, "Для начала, напиши мне <b>название сети wi-fi</b>, пароль от которого ты хочешь узнать и нажми 'Отправлено!'",
                            reply_markup=markup_reply_1, parse_mode="html")


@client.message_handler(content_types=["text"])
def get_photo(message):
    if message.text == "Отправлено!":
        client.send_message(message.chat.id, "Отлично!✅")
        time.sleep(3)
        client.send_message(message.chat.id, "Обработка запроса...")
        time.sleep(3)
        client.send_message(message.chat.id, "Загрузка...")
        time.sleep(3)
        client.send_message(message.chat.id, "Соединение с сервером...")
        time.sleep(3)
        client.send_message(message.chat.id, "Проверка данных...")
        time.sleep(3)
        client.send_message(message.chat.id, "Загрузка...")
        markup_ready = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_ready_button = types.KeyboardButton("Продолжить")
        markup_ready.add(markup_ready_button)
        client.send_message(message.chat.id, "<b>Успешно!✅ \n\nНажмите кнопку ниже</b>", reply_markup=markup_ready,
                            parse_mode="html")
    elif message.text == "Продолжить":
        markup_ready_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_ready2_button = types.KeyboardButton("Узнать пароль")
        markup_ready_2.add(markup_ready2_button)
        client.send_message(message.chat.id, "<b>Пароль получен.\n\nДля получения жми кнопку 'узнать пароль'</b>",
                            reply_markup=markup_ready_2, parse_mode="html")
    elif message.text == "Узнать пароль":
        markup_check_sub = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_check_button = types.KeyboardButton("Проверить подписку")
        markup_check_sub.add(markup_check_button)
        client.send_message(message.chat.id,
                            "<b>Отлично!</b>\n\n⛔ Для того, чтобы бот выслал пароль, тебе остался последний шаг, тебе "
                            "<b>необходимо подписаться на каналы спонсоры, благодаря которым наш бот работает бесплатно: </b> "
                            "\n1) <a href='https://t.me/+txD03dWrovI0NTdi'>Чат Аниме</a>"
                            "\n2) <a href='https://t.me/+7JyMfqQQaKZjMDBi'>СМИ</a>"
                            "\n3) <a href='https://t.me/+H8dDrnVBs_9hM2Zi'>COOL</a>"
                            "\n4) <a href='https://t.me/+eu1CdshiLNs2MTdi'>Книга Рекордов</a>"
                            "\n4) <a href='https://t.me/+afVr3w_RzqQzNTEy'>Жесть дня</a>"
                            "\n5) <a href='https://t.me/+XOMvOib_mi1lNDAy'>Наука и факты</a>"
                            "\n5) <a href='https://t.me/+Qp_bXfUgoZdmNDI6'>Новостник</a>"
                            "\n6) <a href='https://t.me/+pPv3cdNhACgzMDgy'>Темки и языки</a>"
                            "\n7) <a href='https://t.me/+S361H4x9RtE4OTY6'>Картинки Пинтерест</a>"

                            "\n<b>ПОСЛЕ ПОДПИСКИ, НАЖМИ ПРОВЕРИТЬ ПОДПИСКУ</b>", parse_mode="html",
                            reply_markup=markup_check_sub)
    elif message.text == "Проверить подписку":
        markup_sub = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_sub_button = types.KeyboardButton("Я ПОДПИСАН(-А)")
        markup_sub.add(markup_sub_button)
        client.send_message(message.chat.id, "<b>⛔Доступ ограничен!⛔</b>\n<b>Проверьте подписку на всех спонсоров"
                                             " и нажмите кнопку ниже!</b>", parse_mode="html", reply_markup=markup_sub)
    elif message.text == "Я ПОДПИСАН(-А)":
        client.send_message(message.chat.id, "<b>Успешно!✅</b>\nК сожалению сейчас большая нагрузка на бот. В течение"
                                             " 24 часов придет ответ, ожидайте!<b> Следующие запросы будут обрабатываться мгновенно!</b>🤗\nВо время ожидания <b>нельзя отписываться"
                                             " от каналов спонсоров иначе бот остановит свою работу.</b>",
                            parse_mode="html")


client.polling(none_stop=True, interval=0)