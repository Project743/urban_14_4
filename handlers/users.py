from aiogram.dispatcher.filters.state import State, StatesGroup
import keyboards as kb
import crud_functions
import texts.txtusers


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


async def sing_up(message):
    await message.answer(texts.txtusers.name_enter)
    await RegistrationState.username.set()


async def set_username(message, state):
    if crud_functions.is_included(message.text):
        await message.answer(texts.txtusers.name_taken)
        await RegistrationState.username.set()
    else:
        await state.update_data(username=str(message.text))
        await message.answer(texts.txtusers.email_enter)
        await RegistrationState.email.set()


async def set_email(message, state):
    await state.update_data(email=str(message.text))
    await message.answer(texts.txtusers.age_enter)
    await RegistrationState.age.set()


async def set_age(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'])
    await message.answer(texts.txtusers.completed)
    await state.finish()
