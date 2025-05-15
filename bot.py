import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()  # 載入 .env 檔案
TOKEN = os.getenv("DISCORD_TOKEN")  # 讀取環境變數中的 Token

intents = discord.Intents.default()
intents.members = True  # 重要：啟用讀取成員清單的權限
intents.message_content = True  # 重要：啟用讀取訊息內容的權限

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'登入成功：{client.user}')



@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '!draw':
        guild = message.guild
        members = [member for member in guild.members if not member.bot]

        if not members:
            await message.channel.send("沒有可抽的成員 QQ")
            return

        chosen_one = random.choice(members)
        await message.channel.send(f'🎉 被抽到的是：{chosen_one.mention}！')




client.run(TOKEN)
