from discord.ext import commands
from discord import Intents
from loguru import logger
from .cogs.chess import Chess
from .cogs.help import Help
from .cogs.misc import Misc
from .config import TOKEN

bot = commands.Bot(command_prefix="/", intents=Intents().all())

@bot.event
async def on_ready() -> None:
    logger.info(f"Logged in as {bot.user}")
    bot.remove_command("help")  # remove the default !help command
    await bot.add_cog(Chess(bot))
    await bot.add_cog(Help(bot))
    await bot.add_cog(Misc(bot))


def main() -> None:
    bot.run(TOKEN)
