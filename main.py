import os
import pandas
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load private discord token into local environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot object and declare command prefix
bot = commands.Bot(command_prefix="hawk ")

# Load all data in from airtable-exported .csv
DATA = pandas.read_csv('static/Units-Grid view.csv', index-col='Name')


"""
Our main INFO command
"""
@bot.command()
async def info(ctx, arg: str):

    # Pull all heroes who might match the request
    possible_request = []
    for hero_abbrev in DATA['Command']:
        if arg in hero_abbrev:
            possible_request.append(hero_abbrev)

    # Match found
    if len(possible_request) == 1:
        # Lookup full hero data entry
        requested_hero = DATA.loc(possible_request[0])

        # Create Discord EMBED object for hero card
        response=discord.Embed(title="Green Elizabeth", description="Liones", color=0x00f510)
        response.set_thumbnail(url="https://rerollcdn.com/SDSGC/portraits/portrait_61.png")
        response.add_field(name="Gear Set", value="4 HP / 2 Def [OR] 4 Atk / 2 Def", inline=True)
        response.add_field(name="Gear Stats", value="Atk / Def / HP", inline=True)
        response.add_field(name="Card 1 - Attack", value="400% Cancel buff & stance", inline=False)
        response.add_field(name="Card 2 - Recovery", value="Heal allies 400% & Remove Debuffs", inline=False)
        response.add_field(name="Ult", value="Heal allies 400% & Fill Ultimate x 2", inline=False)
        response.add_field(name="Unique", value="Start with Ultimate Move Gauge at 2", inline=False)
        response.add_field(name="Type", value="Support / Utility", inline=True)
        response.add_field(name="Use", value="PvP / PvE / Grey Demon", inline=True)

    # No matches found
    if len(possible_request) == 0:
        response = "Did not find a matching hero. Please try again."

    # Multiple matches found
    if len(possible_request) > 1:
        # Create formatted string with Hero name and Command abbreviations
        format_possibles = ""
        for poss in possible_request:
            format_possibles += DATA.name.command[poss]
            format_possibles += "    {}\n".format(poss)
        response = "Found multiple matches. Please be more specific.\n\n{}".format(format_possibles)


    # send message to current channel
    await ctx.send(response)


# Run bot program
bot.run(TOKEN)

# StdOut notice that bot is connected to server
print(f'{client.user} has connected to Discord!')
