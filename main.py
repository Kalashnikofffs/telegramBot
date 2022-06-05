import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, bot, Poll, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler

# function to handle the /start command
# def start(update, context):
#     update.message.reply_text('Как нам будет комфортнее общаться: на Ты или на Вы?')
# # function to handle the /help command


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

FIRST, SECOND, THIRD, FOURS, FIFTH, SIX, SEVENTH = range(7)
# Данные обратного вызова
ONE, TWO, THREE, FOUR = range(4)

def start(update,context):
    text = "Представляю техническое задание."
    keyboard = [
        [

            InlineKeyboardButton("Видео с комментариями 👌",
                                 url="https://youtu.be/Q6DpndLdvXg"),
            InlineKeyboardButton("Посмотреть код бота 👌", url="https://github.com/Kalashnikofffs/telegramBot/blob/master/main.py"),

        ],
        [
            InlineKeyboardButton("Начать тестировать бота 👌", callback_data='13'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)






def start_over(update, context):


    keyboard = [
        [
            InlineKeyboardButton("На Ты 👌", callback_data='1'),
            InlineKeyboardButton("На Вы 🤝", callback_data='2')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)

    context.bot.send_message(chat_id=update.effective_chat.id, text='Как вам будет комфортнее общаться: на Ты или на Вы?',reply_markup=reply_markup)

    return FIRST


def naTiiliNaVI(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("Специальная военная операция(СВО)", callback_data='3')
        ],
        [
            InlineKeyboardButton("Война/вторжение война Украину", callback_data='3')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)

    if query.data == '1':
        context.user_data['1'] = '1'
        query.edit_message_text(
            text=f"С 24 февраля на территории Украины проходят военные действия. Мнения о том как их называть разделились. А как считаешь Ты?",
            reply_markup=reply_markup)

    if query.data == '2':
        context.user_data['1'] = '2'
        query.edit_message_text(
            text=f"С 24 февраля на территории Украины проходят военные действия. Мнения о том как их называть разделились. А как считаете Вы?",
            reply_markup=reply_markup)

    return SECOND


def kakOtnosites(update, context):
    query = update.callback_query
    query.answer()
    text = 'Как ты относишься к вторжению РФ на территорию Украины?'
    if context.user_data['1'] == '2':
        text = 'Как Вы относитесь к вторжению РФ на территорию Украины?'
    keyboard = [

        [
            InlineKeyboardButton("Полностью поддерживаю", callback_data='4'),
            InlineKeyboardButton("Скорее поддерживаю", callback_data='4')
        ],
        [
            InlineKeyboardButton("Не могу определиться", callback_data='5'),
            InlineKeyboardButton("Скорее не поддерживаю", callback_data='6')
        ],
        [
            InlineKeyboardButton("Категорически не поддерживаю", callback_data='6')
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    query.edit_message_text(text=text, reply_markup=reply_markup)

    return THIRD


def z(update, context):
    query = update.callback_query
    query.answer()
    text = 'Как ты считаещь, какие их этих целей ставились Россией при решении о вторжении в Украину?'
    if context.user_data['1'] == '2':
        text = 'Как Вы считаете, какие их этих целей ставились Россией при решении о вторжении в Украину'
    keyboard = [

        [
            InlineKeyboardButton("Защитить русских в Донбасе", callback_data='7'),
        ],
        [
            InlineKeyboardButton("Предотвратить вторжение Украины на территорию России", callback_data='7')
        ],
        [
            InlineKeyboardButton("Предотвратить вторжение Украины на территорию ЛНР/ДНР", callback_data='7')
        ],
        [
            InlineKeyboardButton("Денацификация/Уничтожить нацистов", callback_data='7')
        ],
        [
            InlineKeyboardButton("Сменить власть в Украине", callback_data='7')
        ],
        [
            InlineKeyboardButton("Уничтожить биолабаротории", callback_data='7')
        ],
        [
            InlineKeyboardButton("Предотвратить создание ядерного оружия", callback_data='7')
        ],
        [
            InlineKeyboardButton("Повысить рейтинг доверия Владимира Де Морта", callback_data='7')
        ],
        [
            InlineKeyboardButton("Захватить территории Донбаса и юга Украины", callback_data='7')
        ],
        [
            InlineKeyboardButton("Предотвратить размещение баз НАТО в Украине", callback_data='7')
        ],
        [
            InlineKeyboardButton("Я не знаю...", callback_data='8')
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    query.edit_message_text(text=text, reply_markup=reply_markup)

    return FOURS


def z1(update, context):
    query = update.callback_query
    query.answer()
    text = 'Доверяешь ли ты новостям и политическим программам из телевизора?'
    if context.user_data['1'] == '2':
        text = 'Доверяете ли Вы новостям и политическим программам из телевизора?'

    keyboard = [

        [
            InlineKeyboardButton("Да, полностью доверяю", callback_data='9'),
        ],
        [
            InlineKeyboardButton("Скорее да", callback_data='9')
        ],
        [
            InlineKeyboardButton("Скорее нет", callback_data='9')
        ],
        [
            InlineKeyboardButton("Нет, совсем нет доверяю", callback_data='9')
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    query.edit_message_text(text=text, reply_markup=reply_markup)

    return FIFTH


def z2(update, context):
    query = update.callback_query
    query.answer()
    text = 'Раздел в разработке'
    context.bot.send_message(update.effective_chat.id, text=text)


def z3(update, context):
    query = update.callback_query
    query.answer()
    text = 'Помимо ТВ, еще больше информации есть в интернете. Каким из источников ты доверяешь?'
    if context.user_data['1'] == '2':
        text = 'Помимо ТВ, еще больше информации есть в интернете. Каким из источников Вы доверяете?'

    keyboard = [

        [
            InlineKeyboardButton("РИА Новости", callback_data='10'),
        ],
        [
            InlineKeyboardButton("Russia Today", callback_data='10')
        ],
        [
            InlineKeyboardButton("Meduza/Mediazona/BBC/Радио свобода/ Настоящее время", callback_data='10')
        ],
        [
            InlineKeyboardButton("Популярная политика", callback_data='10')
        ],
        [
            InlineKeyboardButton("ТГ-каналы: Военный осведомитель/ WarGonzo /Kotsnews", callback_data='10')
        ],
        [
            InlineKeyboardButton("ТГ-канал: Война с фейками", callback_data='10')
        ],
        [
            InlineKeyboardButton("РБК", callback_data='10')
        ],
        [
            InlineKeyboardButton("ТААС/Комсомольская правда/АиФ/Ведомости/Лента", callback_data='10')
        ],
        [
            InlineKeyboardButton("Яндекс Новости", callback_data='10')
        ],
        [
            InlineKeyboardButton("Википедия", callback_data='10')
        ],
        [
            InlineKeyboardButton("Никому из них...", callback_data='10')
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    query.edit_message_text(text=text, reply_markup=reply_markup)
    return SIX


def z4(update, context):
    questions = 'Кому из этих людей ты доверяешь?'
    answer = ['Владимир Путин',
              'Дмитрий Песков',
              'Рамзан Кадыров',
              'Алексей Навальный',
              'Сергей Лваров',
              'Юрий Подоляка'
        , 'Максим Кац',
              'Владимир Соловьёв',
              'Ольга Скобеева',
              'Михаил Ходорковский'
              'Никому из них'
              ]
    if context.user_data['1'] == '2':
        questions = 'Кому из этих людей Вы доверяете?'

    keyboard = [
        [
            InlineKeyboardButton("Идём дальше", callback_data='11'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)

    message = context.bot.send_poll(
        update.effective_chat.id, questions, answer,
        is_anonymous=False, allows_multiple_answers=True, reply_markup=reply_markup
    )
    payload = {
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }

    context.bot_data.update(payload)

    return SEVENTH


def z5(update, context):
    query = update.callback_query
    query.answer()
    text = 'Считаешь ли ты, что Путин хороший президент?'
    if context.user_data['1'] == '2':
        text = 'Считаете ли Вы, что Путин хороший президент?'

    keyboard = [
        [
            InlineKeyboardButton("Да", callback_data='11'),
            InlineKeyboardButton("Нет", callback_data='11'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_photo(chat_id=update.effective_chat.id, caption=text, photo=open('venv/pic/putin-stol-mem-768x512.jpg', 'rb'), reply_markup=reply_markup)

    return FOURS


def receive_poll_answer(update, context):
    """Итоги опроса пользователей"""
    answer = update.poll_answer
    poll_id = answer.poll_id
    try:
        questions = context.bot_data[poll_id]["questions"]
    except KeyError:  # Это ответ на старый опрос
        return
    selected_options = answer.option_ids
    answer_string = ""
    # подсчет и оформление результатов
    for question_id in selected_options:
        if question_id != selected_options[-1]:
            answer_string += questions[question_id] + " и "
        else:
            answer_string += questions[question_id]
    context.bot.send_message(
        context.bot_data[poll_id]["chat_id"],
        f"{update.effective_user.mention_html()} => {answer_string}!",
        parse_mode=ParseMode.HTML,
    )
    # изменение промежуточных результатов в `bot_data`
    context.bot_data[poll_id]["answers"] += 1
    # Закрываем опрос после того, как проголосовали три участника
    if context.bot_data[poll_id]["answers"] == 2:
        context.bot.stop_poll(
            context.bot_data[poll_id]["chat_id"], context.bot_data[poll_id]["message_id"]
        )


if __name__ == '__main__':
    TOKEN = "5583888317:AAGNr8IzYoA9Bei5AQmgmPHaEiBioiMIFO4"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(start_over, pattern='^' + '13' + '$')],
        states={  # словарь состояний разговора, возвращаемых callback функциями
            FIRST: [
                CallbackQueryHandler(naTiiliNaVI, pattern='^' + '1' + '$'),
                CallbackQueryHandler(naTiiliNaVI, pattern='^' + '2' + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(kakOtnosites, pattern='^' + '3' + '$'),


            ],

            THIRD: [
                CallbackQueryHandler(z, pattern='^' + '4' + '$'),
                CallbackQueryHandler(z5, pattern='^' + '5' + '$'),
                CallbackQueryHandler(z2, pattern='^' + '6' + '$'),
            ],
            FOURS: [
                CallbackQueryHandler(z1, pattern='^' + '7' + '$'),
                CallbackQueryHandler(z2, pattern='^' + '8' + '$'),
                CallbackQueryHandler(z2, pattern='^' + '11' + '$'),
            ],
            FIFTH: [
                CallbackQueryHandler(z3, pattern='^' + '9' + '$'),
            ],
            SIX: [
                CallbackQueryHandler(z4, pattern='^' + '10' + '$'),
                CallbackQueryHandler(z2, pattern='^' + '11' + '$'),
            ],
            SEVENTH: [

                CallbackQueryHandler(z2, pattern='^' + '11' + '$'),

            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()

    updater.idle()
