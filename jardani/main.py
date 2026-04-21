from dotenv import load_dotenv
import os
import asyncio

import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True
intents.message_content = True

# description of bot
description = "Jardani is a special, open-source bot"

# initialize the bot
bot = commands.Bot(
    command_prefix="j!",
    description=description,
    intents=intents,
    help_command=commands.DefaultHelpCommand(),
)

# load enviornment variables
load_dotenv()

secret_token = os.getenv("DISCORD_TOKEN")

cogs = ["ping", "lock", "about", "ai"]


async def load_cogs():
    """Load all extensions from specified cogs list"""
    for cog in cogs:
        try:
            await bot.load_extension(f"commands.{cog.lower()}")
        except Exception as error:
            print(f"Failed to load {cog} because {error}")


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}. Bot id is {bot.user.id}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync slash commands because of - {e}")


async def main() -> None:
    async with bot:
        await load_cogs()
        await bot.start(secret_token)


if __name__ == "__main__":
    asyncio.run(main())
