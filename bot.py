import os

import discord
from discord import app_commands


class PingBot(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.none())
        self.commands = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.commands.sync()


bot = PingBot()


@bot.commands.command(name="ping", description="Check whether the bot is awake.")
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Pong!")


token = os.environ.get("DISCORD_BOT_TOKEN")
if not token:
    raise RuntimeError("DISCORD_BOT_TOKEN is not set.")

bot.run(token)