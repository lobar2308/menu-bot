from aiogram import Dispatcher
from aiogram.types import Message
from loguru import logger

from tgbot.services.database import AsyncSession
from tgbot.models.models import TGUser
from tgbot.misc.broadcast import broadcast
from tgbot.misc.utils import Map


async def admin_start(msg: Message, texts: Map):
    """Admin start command handler"""
    logger.info(f'Admin {msg.from_user.id} opened admin panel')
    await msg.reply(texts.admin.hi)


async def admin_stats(m: Message, db_session: AsyncSession, texts: Map):
    """Admin stats command handler"""
    logger.info(f'Admin {m.from_user.id} requested stats')
    count = await TGUser.users_count(db_session)
    await m.reply(texts.admin.total_users.format(count=count))


async def admin_broadcast(m: Message, db_session: AsyncSession, texts: Map):
    """Admin broadcast command handler"""
    logger.info(f'Admin {m.from_user.id} requested broadcast')
    broadcast_text = m.text.replace("/broadcast", "")
    if not broadcast_text:
        # there must be some text after command for broadcasting
        await m.reply(texts.admin.no_broadcast_text)
        return
    users = await TGUser.get_all_users(db_session)
    try:
        await m.reply(texts.admin.broadcast_started)
        logger.success(f'Broadcast started.')
        await broadcast(broadcast_text, users)
        logger.success(f'Broadcast finished.')
        await m.reply(texts.admin.broadcast_ended)
    except Exception as e:
        await m.reply(texts.admin.broadcast_error.format(err=e))
        logger.error("Error while broadcasting!")
        logger.exception(e)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start,
        commands=["admin"],
        state="*",
        is_admin=True
    )
    dp.register_message_handler(
        admin_stats,
        commands=["stats"],
        state="*",
        is_admin=True
    )
    dp.register_message_handler(
        admin_broadcast,
        commands=["broadcast"],
        state="*",
        is_admin=True
    )
