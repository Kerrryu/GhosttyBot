import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

MONITOR_CHANNEL_ID = 1174880713934385234
INFO_CHANNEL_ID = 1174880713934385234

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == MONITOR_CHANNEL_ID:
        print(f"Message content: {message.content}")

        if "invite" in message.content:
            await delete_message(message)
            await reply_to_message(message, f"Please check the <#{INFO_CHANNEL_ID}> channel for more information on how to get an invite.")

    else:
        await bot.process_commands(message)

async def delete_message(message):
    await message.delete()

async def reply_to_message(message, content):
    await message.channel.send(content)

import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('DISCORD_BOT_TOKEN')

if bot_token is None:
    raise ValueError("DISCORD_BOT_TOKEN not found in environment variables")

bot.run(bot_token)