import asyncio
import logging
import sys

from db.config import Base, engine
from dispatcher import dp, bot
from bot import *


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    Base.metadata.create_all(engine)
    asyncio.run(main())
