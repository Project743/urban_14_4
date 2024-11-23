import keyboards as kb
import crud_functions
import texts.txttrade


async def get_buying_list(message):
    all_products = crud_functions.get_all_products()
    for id_, name, description, price in all_products:
        await message.answer(f'Название: {name} | Описание: {description} | Цена: {price}')
        with open(f'files/media/{id_}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb.trade_kb)


async def send_confirm_message(call):
    await call.message.answer(texts.txttrade.completed)
    await call.answer()
