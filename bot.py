import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ollama

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

MONITOR_CHANNEL_ID = int(os.getenv('MONITOR_CHANNEL_ID'))
INFO_CHANNEL_ID = int(os.getenv('INFO_CHANNEL_ID'))
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == MONITOR_CHANNEL_ID:
        print(f"Message content: {message.content}")

        intent = await analyze_intent(message.content)
        print(f"Intent: {intent}")
        if "request_access_to_beta" in intent:
            await delete_message(message)
            await reply_to_message(message, f"Please check the <#{INFO_CHANNEL_ID}> channel for more information on how to get an invite.")

    else:
        await bot.process_commands(message)

async def analyze_intent(message_content):
    messages = [
        {
            'role': 'system',
            'content': 'I need you to analyze the intent of the following message. Our bot is in a discord server and it is monitoring a specific channel. The purpose of the server is for a new terminal emulator called Ghostty. People sometimes request invites to the beta, and when they do, they usually say something like "please send me an invite" or "how do I get an invite?" or "send me an invite pls". The possible intents are: request_access_to_beta, unknown. Respond with the intent name.'
        },
        {
            'role': 'user',
            'content': f'Message: {message_content}'
        }
    ]

    response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
    return response['message']['content']


async def delete_message(message):
    await message.delete()

async def reply_to_message(message, content):
    await message.channel.send(content)

bot_token = os.getenv('DISCORD_BOT_TOKEN')

if bot_token is None:
    raise ValueError("DISCORD_BOT_TOKEN not found in environment variables")

bot.run(bot_token)