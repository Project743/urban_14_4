from aiogram.dispatcher.filters.state import State, StatesGroup
import keyboards as kb
import texts.txtstart


async def start(message):
    await message.answer(f'Привет! @{message.from_user.username}!\n\n' + texts.txtstart.start, reply_markup=kb.kb)


async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb.inline_kb)


async def get_formulas(call):
    await call.message.answer(texts.txtstart.formula)
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    res = (10 * data['weight']) + (6.25 * data['growth']) - (5 * data['age']) + 5
    await message.answer(f'Ваша норма калорий {res}')
    await state.finish()


async def all_messages(message):
    await message.answer(texts.txtstart.all)
