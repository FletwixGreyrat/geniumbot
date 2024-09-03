import aiogram
from dependencies import courses_info
from aiogram import Bot, Dispatcher, types
from os import getenv

TOKEN = getenv("TOKEN")

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message): 

    channel_keyboard = types.InlineKeyboardMarkup()
    channel_keyboard.add(types.InlineKeyboardButton(text="Перейти на канал", url="https://t.me/genium1"))

    start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_keyboard.add(types.KeyboardButton(text="Ознакомиться с курсами🧑‍🏫🤖"))
    start_keyboard.insert(types.KeyboardButton(text="Обратная связь💌"))
    photo = open("logo.jpg", "rb")
    caption = """Доброго времени суток!
Вас приветствует бот интеллектуально-инновационного центра развития детей и подростков "ГениУм".
Вот мой функционал:
1. Основная информация о центре
2. Каталог курсов центра
3. Связь в мессенджере с администратором центра.

Еще я прикреплю ссылку на наш Телеграм канал, куда мы выкладываем жизнь нашего центра, занятия, и достижения детей"""
    await bot.send_photo(message.from_user.id, photo=photo, caption=caption, reply_markup=channel_keyboard)
    await message.answer("Прикрепляю ниже навигационную клавиатуру🥰", reply_markup=start_keyboard)


@dp.message_handler(lambda message: message.text == "Ознакомиться с курсами🧑‍🏫🤖")
async def courses_list_command(message: types.Message):
    text = """В нашем центре есть множество курсов, направленных на техническое и гуманитарное развитие детей. 
Вот их список:
💻 Программирование
🤖 Робототехника
♙ Шахматы
🧮 Ментальная арифметика
🎒 Подготовка к школе
🧠 Интеллектуальное развитие
🎨 Арт-студия
🖌️ Живопись
🕐 Продленка
📚 Английский язык
✍️ Каллиграфия
🎤 Ораторское искусство
📖 Скорочтение
🎓 Подтягивание по школьным предметам с 1 по 9 класс"""
    courses_keyboard = types.InlineKeyboardMarkup()
    courses_keyboard.add(types.InlineKeyboardButton(text="💻 Программирование", callback_data="Программирование"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🤖 Робототехника", callback_data="Робототехника"))
    courses_keyboard.add(types.InlineKeyboardButton(text="🧮 Ментальная арифметика", callback_data="Ментальная"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎒 Подготовка к школе", callback_data="Подготовка"))
    courses_keyboard.add(types.InlineKeyboardButton(text="🧠 Интеллектуальное развитие", callback_data="Интеллектуальное"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎨 Арт-студия", callback_data="Арт"))
    courses_keyboard.add(types.InlineKeyboardButton(text="🖌️ Живопись", callback_data="Живопись"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🕐 Группа продленного дня", callback_data="Группа"))
    courses_keyboard.add(types.InlineKeyboardButton(text="♟️ Шахматы", callback_data="Шахматы"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="📚 Английский язык", callback_data="Английский"))
    courses_keyboard.add(types.InlineKeyboardButton(text="✍️ Каллиграфия", callback_data="Каллиграфия"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎤 Ораторское искусство", callback_data="Ораторское"))
    courses_keyboard.add(types.InlineKeyboardButton(text="📖 Скорочтение", callback_data="Скорочтение"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎓 Подтягивание", callback_data="Подтягивание"))

    await message.answer(text=text, reply_markup=courses_keyboard)


@dp.callback_query_handler(text="Программирование")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Программирование"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Робототехника")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Робототехника"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)

@dp.callback_query_handler(text="Ментальная")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Ментальная"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Подготовка")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Подготовка"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Интеллектуальное")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Интеллектуальное"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Арт")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Арт"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Группа")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Группа"]}\n
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Шахматы")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Шахматы"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Английский")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Английский"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Ораторское")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Ораторское"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Скорочтение")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Скорочтение"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Подтягивание")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Подтягивание"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Каллиграфия")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Каллиграфия"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)


@dp.callback_query_handler(text="Живопись")
async def chess_callback_keyboard(call: types.CallbackQuery):
    courses_info_keyboard = types.InlineKeyboardMarkup()
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Обратная связь💌", callback_data="obratnaya"))
    courses_info_keyboard.add(types.InlineKeyboardButton(text="Назад❌", callback_data="ci_back"))
    text = f"""{courses_info["Живопись"]}\n 
Остались вопросы? Мы с радостью ответим на них, обратитесь в обратную связь или позвоните нам по номеру +79667421001"""
    await call.message.edit_text(text=text, reply_markup=courses_info_keyboard)

@dp.callback_query_handler(text="ci_back")
async def courses_info_back_command(call: types.CallbackQuery):
    text = """В нашем центре есть множество курсов, направленных на техническое и гуманитарное развитие детей. 
Вот их список:
💻 Программирование
🤖 Робототехника
♙ Шахматы
🧮 Ментальная арифметика
🎒 Подготовка к школе
🧠 Интеллектуальное развитие
🎨 Арт-студия
🖌️ Живопись
🕐 Продленка
📚 Английский язык
✍️ Каллиграфия
🎤 Ораторское искусство
📖 Скорочтение
🎓 Подтягивание по школьным предметам с 1 по 9 класс"""
    courses_keyboard = types.InlineKeyboardMarkup()
    courses_keyboard.add(types.InlineKeyboardButton(text="💻 Программирование", callback_data="Программирование"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🤖 Робототехника", callback_data="Робототехника"))
    courses_keyboard.add(types.InlineKeyboardButton(text="🧮 Ментальная арифметика", callback_data="Ментальная"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎒 Подготовка к школе", callback_data="Подготовка"))
    courses_keyboard.add(types.InlineKeyboardButton(text="🧠 Интеллектуальное развитие", callback_data="Интеллектуальное"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎨 Арт-студия", callback_data="Арт"))
    courses_keyboard.add(types.InlineKeyboardButton(text="🖌️ Живопись", callback_data="Живопись"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🕐 Группа продленного дня", callback_data="Группа"))
    courses_keyboard.add(types.InlineKeyboardButton(text="♟️ Шахматы", callback_data="Шахматы"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="📚 Английский язык", callback_data="Английский"))
    courses_keyboard.add(types.InlineKeyboardButton(text="✍️ Каллиграфия", callback_data="Каллиграфия"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎤 Ораторское искусство", callback_data="Ораторское"))
    courses_keyboard.add(types.InlineKeyboardButton(text="📖 Скорочтение", callback_data="Скорочтение"))
    courses_keyboard.insert(types.InlineKeyboardButton(text="🎓 Подтягивание", callback_data="Подтягивание"))

    await call.message.edit_text(text=text, reply_markup=courses_keyboard)




if __name__ == "__main__":
    aiogram.executor.start_polling(skip_updates=True, dispatcher=dp)
