import discord
from discord.ext import commands

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# CONFIGURATION (Replace these with your actual IDs as integers)
TARGET_AUTHOR_ID = 713586207119900693  # Target User or Bot ID to trigger on
TARGET_CHANNEL_ID = 1560243134477373470  # Optional: Set to Channel ID if restricted to one channel (or keep 0 for all channels)

@bot.event
async def on_ready():
    print(f"Logged in successfully as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author.id == bot.user.id:
        return

    # Check if the message is from the target author
    if message.author.id == TARGET_AUTHOR_ID:
        # Check channel restriction if specified
        if TARGET_CHANNEL_ID == 0 or message.channel.id == TARGET_CHANNEL_ID:
            await message.channel.send("@everyone")

    await bot.process_commands(message)

# Run the bot using your token
bot.run("MTU2MDI5OTk4Njg3NTQ1MzQ4MA.GY4nNF.RnfOT7tsg-9F570yGy4apsxN2P1oj0oIHweJZ4")