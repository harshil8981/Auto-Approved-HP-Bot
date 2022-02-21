import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

harshil8981=Client(
    "Auto Approved Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@harshil8981.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("📦 Repo", url="https://github.com/harshil8981/Auto-Approved-HP-Bot"),
      InlineKeyboardButton("Updates 📢", url="https://t.me/Hp_botupdate")
      ],[
      InlineKeyboardButton("➕️ Add Me To Your Chat ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart")
      ]]
    await message.reply_text(text="**__Hello Iam Auto Approved Join Request Bot Repo https://github.com/harshil8981/Auto-Approved-HP-Bot**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@harshil8981.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: harshil8981, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
        print("Welcome....")

print("Auto Approved Bot")
harshil8981.run()
