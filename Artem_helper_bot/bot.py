import asyncio

from aiogram import Bot, Dispatcher
from handlers import  other_handlers, user_handlers
from config_data.config import Config, load_config


#Функция конфигурирования и запуска бота
async def main() -> None:

    #Загружаем конфиг в переменную config
    config: Config = load_config()
    BOT_TOKEN: str = config.tg_bot.token

    #Инициализируем бот и диспетчер 
    bot: Bot = Bot(token=config.tg_bot.token) 
    dp: Dispatcher = Dispatcher()

    #Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    #Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())