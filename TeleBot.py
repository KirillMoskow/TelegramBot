import telebot
from telebot import types

bot = telebot.TeleBot("token")


def start(message):
    greetings = f'<b>Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, greetings, parse_mode='html')
    get_info(message)


def get_info(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_1 = types.KeyboardButton('Меньше 30')
    item_2 = types.KeyboardButton('30-40')
    item_3 = types.KeyboardButton('40-60')
    item_4 = types.KeyboardButton('Больше 60')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"Сколько вам лет?", reply_markup=markup)
    bot.register_next_step_handler(message, Age)
def get_info2(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Валюта и банковские вклады')
    item_2 = types.KeyboardButton('ПИФы, доверительное управление, металлические счета, структурные продукты')
    item_3 = types.KeyboardButton('Самостоятельная торговля ценными бумагами, Forex')
    item_4 = types.KeyboardButton('Самостоятельная торговля ценными бумагами, фьючерсами, опционами')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"Есть опыт в инвестициях?", reply_markup=markup)
    bot.register_next_step_handler(message, Exp)
def get_info3(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Меньше 5 лет')
    item_2 = types.KeyboardButton('5-10 лет')
    item_3 = types.KeyboardButton('10-15 лет')
    item_4 = types.KeyboardButton('Больше 15 лет')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"На какой срок планируешь инвестировать?", reply_markup=markup)
    bot.register_next_step_handler(message, Period)
def get_info4(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Сохранить капитал')
    item_2 = types.KeyboardButton('Доходность больше, чем в банке')
    item_3 = types.KeyboardButton('Получить существенный доход')
    item_4 = types.KeyboardButton('Получить максимальный доход')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"Твоя инвестиционная цель?", reply_markup=markup)
    bot.register_next_step_handler(message, Target)
def get_info5(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Покрытия текущих расходов')
    item_2 = types.KeyboardButton('Совершения крупных покупок в ближайшие годы')
    item_3 = types.KeyboardButton('Долгосрочного создания капитала (пенсия, наследство)')
    item_4 = types.KeyboardButton('Максимизации богатства (результат инвестиций не критичен для среднесрочных и краткосрочных целей)')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"Доход от инвестиций нужен для", reply_markup=markup)
    bot.register_next_step_handler(message, Needs)
def get_info6(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Предполагаю, что вырастет')
    item_2 = types.KeyboardButton('Останется примерно на том же уровне')
    item_3 = types.KeyboardButton('Предполагаю, что снизится')
    item_4 = types.KeyboardButton('Планирую выход на пенсию/потерю основного источника дохода')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"Изменится ли твой доход в ближайшие годы?", reply_markup=markup)
    bot.register_next_step_handler(message, Changes)
def get_info7(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Низкая доходность при минимальном риске')
    item_2 = types.KeyboardButton('Небольшая доходность при низком риске')
    item_3 = types.KeyboardButton('Средняя доходность при среднем риске')
    item_4 = types.KeyboardButton('Высокая доходность при высоком риске')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"Что предпочтёшь?", reply_markup=markup)
    bot.register_next_step_handler(message, Profit)
def get_info8(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Менее 10%')
    item_2 = types.KeyboardButton('10-20%')
    item_3 = types.KeyboardButton('20-30%')
    item_4 = types.KeyboardButton('30-40%')
    item_5 = types.KeyboardButton('Более 40%')
    markup.add(item_1, item_2, item_3, item_4,item_5)
    bot.send_message(message.chat.id,"На какую величину допускаешь падение стоимости портфеля в рамках одного года?", reply_markup=markup)
    bot.register_next_step_handler(message, Choice)
def get_info9(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Продам все рисковые активы и положу деньги в банк')
    item_2 = types.KeyboardButton('Продам часть рисковых активов и положу деньги в банк')
    item_3 = types.KeyboardButton('Ничего, подожду пока портфель снова вырастет')
    item_4 = types.KeyboardButton('Докуплю ещё рисковых активов, пока дёшево')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,"Что будешь делать в случае значительного снижения стоимости портфеля?", reply_markup=markup)
    bot.register_next_step_handler(message,Risks)
def get_info10(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item_1 = types.KeyboardButton('Возможность заработать до 105$ или потерять до 100$')
    item_2 = types.KeyboardButton('Возможность заработать до 205$ или потерять до 200$')
    item_3 = types.KeyboardButton('Возможность заработать до 310$ или потерять до 300$')
    item_4 = types.KeyboardButton('Возможность заработать до 420$ или потерять до 400$')
    item_5 = types.KeyboardButton('Возможность заработать до 540$ или потерять до 500$')
    markup.add(item_1, item_2, item_3, item_4,item_5)
    bot.send_message(message.chat.id,"У тебя есть 1 000$. Какой из предложенных вариантов инвестиций выберешь?", reply_markup=markup)
    bot.register_next_step_handler(message, Loses)
a = 0
def exit_msg(message):
    global a

    markup = types.ReplyKeyboardMarkup(row_width=1)
    but_1 = types.KeyboardButton('Да')
    but_2 = types.KeyboardButton('Нет')

    markup.row(but_1, but_2)
    bye_msg = f'<b>Спасибо за опрос!, {message.from_user.first_name} {message.from_user.last_name}</b>\n' \
              f'Ваш результат: {a}'
    bot.send_message(message.chat.id, bye_msg, parse_mode='html')

    bot.send_message(message.chat.id, "Хотите пройти опрос заново?", reply_markup=markup)
    bot.register_next_step_handler(message, get_restart_answ)


@bot.message_handler(commands=['start'])
def new_user(message):
    global a
    a = 0
    start(message)

@bot.message_handler()
def Age(message):
    global a
    if message.text == 'Меньше 30':
        a += 1
    elif message.text == '30-40':
        a += 2
    elif message.text == '40-60':
        a += 3
    elif message.text == 'Больше 60':
        a += 4
    get_info2(message)

@bot.message_handler()
def Exp(message):
    global a
    if message.text == 'Валюта и банковские вклады':
        a += 1
    elif message.text == 'ПИФы, доверительное управление, металлические счета, структурные продукты':
        a += 2
    elif message.text == 'Самостоятельная торговля ценными бумагами, Forex':
        a += 3
    elif message.text == 'Самостоятельная торговля ценными бумагами, фьючерсами, опционами':
        a += 4
    get_info3(message)

@bot.message_handler()
def Period(message):
    global a
    if message.text == 'Меньше 5 лет':
        a += 1
    elif message.text == '5-10 лет':
        a += 2
    elif message.text == '10-15 лет':
        a += 3
    elif message.text == 'Больше 15 лет':
        a += 4
    get_info4(message)

@bot.message_handler()
def Target(message):
    global a
    if message.text == 'Сохранить капитал':
        a += 1
    if message.text == 'Доходность больше, чем в банке':
        a += 2
    elif message.text == 'Получить существенный доход':
        a += 3
    elif message.text == 'Получить максимальный доход':
        a += 4
    get_info5(message)

@bot.message_handler()
def Needs(message):
    global a
    if message.text == 'Покрытие текущих расходов':
        a += 1
    elif message.text == 'Совершение крупных покупок в ближайшие годы':
        a += 2
    elif message.text == 'Долгосрочного создания капитала (пенсия, наследство)':
        a += 3
    elif message.text == 'Максимизации богатства (результат инвестиций не критичен для среднесрочных и краткосрочных целей)':
        a += 4
    get_info6(message)

@bot.message_handler()
def Changes(message):
    global a
    if message.text == 'Предполагаю, что вырастет':
        a += 1
    elif message.text == 'Останется примерно на том же уровне':
        a += 2
    elif message.text == 'Предполагаю, что снизится':
        a += 3
    elif message.text == 'Планирую выход на пенсию/потерю основного источника дохода':
        a += 4
    get_info7(message)

@bot.message_handler()
def Profit(message):
    global a
    if message.text == 'Низкая доходность при минимальном риске':
        a += 1
    elif message.text == 'Небольшая доходность при низком риске':
        a += 2
    elif message.text == 'Средняя доходность при среднем риске':
        a += 3
    elif message.text == 'Высокая доходность при высоком риске':
        a += 4
    get_info8(message)

@bot.message_handler()
def Choice(message):
    global a
    if message.text == 'Менее 10%':
        a += 1
    elif message.text == '10-20%':
        a += 2
    elif message.text == '20-30%':
        a += 3
    elif message.text == '30-40%':
        a += 4
    elif message.text == 'Более 40%':
        a += 5
    get_info9(message)

@bot.message_handler()
def Risks(message):
    global a
    if message.text == 'Продам все рисковые активы и положу деньги в банк':
        a += 1
    elif message.text == 'Продам часть рисковых активов и положу деньги в банк':
        a += 2
    elif message.text == 'Ничего, подожду пока портфель снова вырастет':
        a += 3
    elif message.text == 'Докуплю ещё рисковых активов, пока дёшево':
        a += 4
    get_info10(message)

@bot.message_handler()
def Loses(message):
    global a
    if message.text == 'Возможность заработать до 105$ или потерять до 100$':
        a += 1
    elif message.text == 'Возможность заработать до 205$ или потерять до 200$':
        a += 2
    elif message.text == 'Возможность заработать до 310$ или потерять до 300$':
        a += 3
    elif message.text == 'Возможность заработать до 420$ или потерять до 400$':
        a += 4
    elif message.text == 'Возможность заработать до 540$ или потерять до 500$':
        a += 5
    bot.send_message(message.chat.id,f'Score_exp:{a}')

    exit_msg(message)

@bot.message_handler()
def get_restart_answ(message):
    global a

    if message.text == 'Да':
        a = 0
        start(message)
    if message.text == 'Нет':
        pass


bot.polling()
