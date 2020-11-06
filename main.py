import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="roxy ")


@bot.command()
async def info(ctx, arg: str):
    # StdOut notice that bot is connected to server
    print(f'{client.user} has connected to Discord!')

    if 'geli' in arg:
        response = ''.join(("Green Elizabeth Healer\n\n",
                            "Gear: ATK/DEF\n\n",
                            "Substats: ATK/DEF/HP"))


    # send message to current channel
    await ctx.send(response)


bot.run(TOKEN)
