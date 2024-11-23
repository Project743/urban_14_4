from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import keyboards as kb
import config, crud_functions
import handlers.users, handlers.start, handlers.trade

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

crud_functions.initiate_db()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


dp.message_handler(text='Регистрация')(handlers.users.sing_up)
dp.message_handler(state=handlers.users.RegistrationState.username)(handlers.users.set_username)
dp.message_handler(state=handlers.users.RegistrationState.email)(handlers.users.set_email)
dp.message_handler(state=handlers.users.RegistrationState.age)(handlers.users.set_age)

dp.message_handler(text='Рассчитать')(handlers.start.main_menu)
dp.callback_query_handler(text='formulas')(handlers.start.get_formulas)
dp.callback_query_handler(text='calories')(handlers.start.set_age)
dp.message_handler(state=handlers.start.UserState.age)(handlers.start.set_growth)
dp.message_handler(state=handlers.start.UserState.growth)(handlers.start.set_weight)
dp.message_handler(state=handlers.start.UserState.weight)(handlers.start.send_calories)

dp.message_handler(commands=['start'])(handlers.start.start)

dp.message_handler(text='Купить')(handlers.trade.get_buying_list)
dp.callback_query_handler(text='product_buying')(handlers.trade.send_confirm_message)

dp.message_handler()(handlers.start.all_messages)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
