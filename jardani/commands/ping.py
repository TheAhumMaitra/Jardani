from discord.ext import commands
from discord import app_commands
import discord


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Check the bot's status")
    async def ping(self, ctx):
        await ctx.send(f"Pong {ctx.author.mention}")

    @app_commands.command(name="ping", description="check the bot's status")
    async def ping_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong {interaction.user.mention}")


async def setup(bot):
    await bot.add_cog(Ping(bot=bot))
