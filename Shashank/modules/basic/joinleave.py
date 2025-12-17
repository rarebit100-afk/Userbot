# © By Shashank shukla (Github = itzshukla) You are motherfucker if you Don't gives credits.

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from Shashank.modules.help import add_command_help

@Client.on_message(filters.command(["join"], ".") & filters.me)
async def join(client: Client, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`ᴘʀᴏᴄᴇssɪɴɢ...`")
    try:
        await client.join_chat(tex)
        await g.edit(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴊᴏɪɴᴇᴅ ᴄʜᴀᴛ ɪᴅ** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leave"], ".") & filters.me)
async def leave(client: Client, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`ᴘʀᴏᴄᴇssɪɴɢ...`")
    try:
        await xv.edit_text(f"{client.me.first_name} ʜᴀs ʟᴇғᴛ ᴛʜɪs ɢʀᴏᴜᴘ, ʙʏᴇ!!")
        await client.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ᴇʀʀᴏʀ:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leaveallgc"], ".") & filters.me)
async def kickmeall(client: Client, message: Message):
    tex = await message.reply_text("`ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ ᴄʜᴀᴛs...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ {done} ɢʀᴏᴜᴘs, ғᴀɪʟᴇᴅ ᴛᴏ ʟᴇғᴛ {er} ɢʀᴏᴜᴘs**"
    )


@Client.on_message(filters.command(["leaveallch"], ".") & filters.me)
async def kickmeallch(client: Client, message: Message):
    ok = await message.reply_text("`ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ ᴄʜᴀᴛs...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(
        f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ {done} ᴄʜᴀɴɴᴇʟ, ғᴀɪʟᴇᴅ ᴛᴏ ʟᴇғᴛ {er} ᴄʜᴀɴɴᴇʟ**"
    )


add_command_help(
    "joinleave",
    [
        [
            "kickme",
            "To leave!!.",
        ],
        ["leaveallgc", "to leave all groups where you joined."],
        ["leaveallch", "to leaveall channel where you joined."],
        ["join [Username]", "give an specific username to join."],
        ["leave [Username]", "give an specific username to leave."],
    ],
)
