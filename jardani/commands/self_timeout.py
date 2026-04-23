from discord import app_commands, Interaction
from discord.ext import commands
from datetime import timedelta


class SelfTimeout(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="self-timeout", description="It timeouts the member for specified minutes"
    )
    @app_commands.describe(
        duration="Write the timeout duration in minutes (max duration : 40320)"
    )
    async def self_timeout(self, interaction: Interaction, duration: int):
        """This command allows users to timeout themselves"""
        if duration > 40320:
            await interaction.response.send_message(
                "You exceed the maximum timeout limit", ephemeral=True
            )

        else:
            await interaction.response.send_message(
                f"{interaction.user.mention} Self timeout is applied for you. You requested for {duration}m. If you think this is your mistake then please create a support ticket"
            )
            await interaction.user.timeout(
                timedelta(minutes=duration),
                reason=f"This timeout was requested by the user for {duration}",
            )


async def setup(bot):
    await bot.add_cog(SelfTimeout(bot=bot))
