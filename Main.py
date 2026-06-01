import discord
from discord.ext import commands
import openai


DISCORD_TOKEN = "BOT TOKEN"
OPENAI_API_KEY = "open ai key"
CHANNEL_ID = channel id

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
openai.api_key = OPENAI_API_KEY

@bot.event
async def on_ready():
    print(f"bot is logged as{bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    

    if message.channel.id != CHANNEL_ID and message.guild is not None:
        return

    try:

        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "you're a friendly bot"},
                {"role": "user", "content": message.content},
            ],
        )

        reply = response.choices[0].message.content
        await message.channel.send(reply)

    except Exception as e:
        print("error:", e)
        await message.channel.send("therew is an error, try again")

bot.run(DISCORD_TOKEN)
