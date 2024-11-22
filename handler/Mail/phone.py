from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.state import MAIL
from asyncio import create_task
from utils.env import GROUP_ID
from loader import bot
@dp.message_handler(content_types=('contact'), state=MAIL.phone)
async def Mail_handler_task(message: Message, state: FSMContext):

    phone = message.contact.phone_number

    await state.update_data({
        'phone':phone
    })

    data = await state.get_data()
    count = data.get('count')
    location = data.get('location')

    
    await bot.send_message(
        chat_id= GROUP_ID ,
        text=texts.mail_gruop( 
            count = count,
            phone = phone,
            location = location,
        )
    ) ,

    await message.answer('sizning arizngiz adminga yuborildi')

    
    await state.finish()