from discord import app_commands, Interaction, Embed
from discord.ext import commands


class About(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def get_about(self):
        """Returns the the details of bot as embed"""
        embed = Embed()

        embed.title = "About"
        embed.description = "**Jardani** is created by Ahum Maitra. This is a free and open source bot. This bot is licensed under the terms of GNU Public License V3 or later. \n \n **Official Repository link** : https://github.com/TheAhumMaitra/Jardani"

        return embed

    @app_commands.command(name="about", description="Get the bot's information")
    async def slash_about(self, interaction: Interaction):
        """About slash command"""
        embed = await self.get_about()
        await interaction.response.send_message(embed=embed)

    @commands.command(name="about", description="Get the details of Jardani")
    async def prefix_about(self, ctx):
        """About prefix command"""
        embed = await self.get_about()
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))
