import os
import csv
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load private discord token into local environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot object and declare command prefix
bot = commands.Bot(command_prefix="hawk ")

# Declare Constants
DATA_FILENAME = 'static/Units-Grid view.csv'
GREEN = "0x00f510"
RED = "0xf51000"
BLUE = "0x1000f5"

# initializing the titles and rows list 
data = []

# reading csv file 
with open(DATA_FILENAME, 'r') as csvfile:
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    headers = next(csvreader)

    # This might be convoluted. Just single entry in list for each hero
    # then look up baesd on keys later depending on bot subcommand
    # [([ban, bban, nunchuckban], {Name: , Color: , Title: })]

    # extracting each data row one by one
    for row in csvreader:
        hero_dict = {}
        for i in range(len(row):
            hero_dict[headers[i]] = row[i]
        data.append(hero_dict)


"""
Our main INFO command
"""
@bot.command()
async def info(ctx, arg: str):

    # Pull all heroes who might match the request
    possible_request = []
    for hero in data:
        for abbreviation in hero['Command']:
            if arg in str(abbreviation):
                possible_request.append(hero)

    # Match found
    if len(possible_request) == 1:
        # simplify single hero data into variable
        hero = possible_request[0]

        if hero['Type'] == 'Strength':
            color_code = RED
        elif hero['Type'] == 'HP':
            color_code = GREEN
        elif hero['Type'] == 'Speed':
            color_code = BLUE

        # Create Discord EMBED object for hero card
        embed=discord.Embed(title=hero['Name'], description=hero['Title'], color=color_code)
        embed.set_thumbnail(url=hero['Pics'])
        embed.add_field(name="Gear Set", value=hero['Gear'], inline=True)
        embed.add_field(name="Gear Stats", value=hero['Gear Stats'], inline=True)
        embed.add_field(name=hero['Card 1'], value=hero['Card 1 Stats'], inline=False)
        embed.add_field(name=hero['Card 2'], value=hero['Card 2 Stats'], inline=False)
        embed.add_field(name="Ult", value=hero['Ultimate Stats'], inline=False)
        embed.add_field(name="Unique", value=hero['Unique Stats'], inline=False)
        embed.add_field(name="Race", value=hero['Race'], inline=True)
        embed.add_field(name="Rarity", value=hero['Rarity'], inline=True)
        # embed=discord.Embed(title="Green Elizabeth", description="Liones", color=0x00f510)
        # embed.set_thumbnail(url="https://rerollcdn.com/SDSGC/portraits/portrait_61.png")
        # embed.add_field(name="Gear Set", value="4 HP / 2 Def [OR] 4 Atk / 2 Def", inline=True)
        # embed.add_field(name="Gear Stats", value="Atk / Def / HP", inline=True)
        # embed.add_field(name="Card 1 - Attack", value="400% Cancel buff & stance", inline=False)
        # embed.add_field(name="Card 2 - Recovery", value="Heal allies 400% & Remove Debuffs", inline=False)
        # embed.add_field(name="Ult", value="Heal allies 400% & Fill Ultimate x 2", inline=False)
        # embed.add_field(name="Unique", value="Start with Ultimate Move Gauge at 2", inline=False)
        # embed.add_field(name="Type", value="Support / Utility", inline=True)
        # embed.add_field(name="Use", value="PvP / PvE / Grey Demon", inline=True)
        await ctx.send(embed=embed)

    # No matches found
    if len(possible_request) == 0:
        response = "Did not find a matching hero. Please try again."
        # send message to current channel
        await ctx.send(response)

    # Multiple matches found
    if len(possible_request) > 1:
        # Create formatted string with Hero name and Command abbreviations
        # format_possibles = ""
        # for poss in possible_request:
        #     format_possibles += data.name['command'][poss]
        #     format_possibles += "    {}\n".format(poss)
        # response = "Found multiple matches. Please be more specific.\n\n{}".format(format_possibles)
        response = "Found multiple matches. Please be more specific."
        # send message to current channel
        await ctx.send(response)




# Run bot program
bot.run(TOKEN)

# StdOut notice that bot is connected to server
# print(f'{client.user} has connected to Discord!')
