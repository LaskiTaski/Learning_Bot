from aiogram.utils import executor
from bot_telegram import dp
from handlers import FSM, Video, HomeWork, Project

FSM.register_handlers_machine(dp)
Video.register_handlers_video(dp)
HomeWork.register_handlers_video(dp)
Project.register_handlers_video(dp)

async def on_start_up(_):
    print('The bot is running')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
