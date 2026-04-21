from discord import app_commands, Interaction, Role, TextChannel
from discord.ext import commands


class Lock(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="lock", description="Lock a channel with specified role")
    @app_commands.describe(
        channel="Select the channel you want to lock",
        role="Select or type out the role id to restrict",
    )
    @app_commands.default_permissions(
        manage_channels=True
    )  # member needs to have mange channels permssions to use thiscommand
    async def lock(self, interaction: Interaction, channel: TextChannel, role: Role):
        """Lock slash command to lock a channel for specified role"""

        # if user doesn't have mannage channels perms
        if not interaction.user.guild_permissions.manage_channels:
            return await interaction.response.send_message(
                "You are not the one to decide", ephemeral=True
            )

        overwrite = channel.overwrites_for(role)
        overwrite.send_messages = False

        perms = channel.permissions_for(role)

        if perms.send_messages:
            print(f"Processing the request to lock {channel} for {role}")
            await interaction.response.send_message(
                f"{interaction.user.mention} Locking `{channel}` for `{role}` . Have a nice day! God bless!"
            )
            return await channel.set_permissions(role, overwrite=overwrite)
        else:
            return await interaction.response.send_message(
                f"{channel} is already locked for {role}"
            )

    # unlock command
    @app_commands.command(
        name="unlock", description="Unlock a channel with specified role"
    )
    @app_commands.describe(
        channel="Select the channel you want to unlock",
        role="Select or type out the role id to unrestrict",
    )
    @app_commands.default_permissions(manage_channels=True)
    async def unlock(self, interaction: Interaction, channel: TextChannel, role: Role):
        """Unlock a channel with specified role"""

        if not interaction.user.guild_permissions.manage_channels:
            return await interaction.response.send_message(
                "You are not the one to decide", ephemeral=True
            )

        overwrite = channel.overwrites_for(role)
        overwrite.send_messages = True

        perms = channel.permissions_for(role)

        if not perms.send_messages:
            print(f"Processing the request to unlock {channel} for {role}")
            await interaction.response.send_message(
                f"{interaction.user.mention} Unlocking `{channel}` for `{role}` . Have a nice day! God bless!"
            )
            return await channel.set_permissions(role, overwrite=overwrite)
        else:
            # if the channel is already locked
            return await interaction.response.send_message(
                f"{channel} is already unlocked for {role}"
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Lock(bot))
