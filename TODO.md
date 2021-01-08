List of dicts
	([ban, bban, nunchuckban], {Name: , Color: , Title: })
	tuple with array of commands followed by dict of full character info


Info
	List all character commands
	"Loose" text search
	Suggestions for similar heroes

Ideas for Info embed
	
	Character name (character portrait)
	Rarity 
	Color 
	(support/damage/utility) can be several depending on the hero

	Card 1(insert skill picture)
	:(damage effect, effects,rarity)
	Card 2 insert card picture 
	 ( damage effect,effects rarity)

	Ultimate insert card picture 
	(damage effect and combined hero if possible)
	Unique (effects)
	
	Best Use (game mode (pvp/pve) type of activity(DMs, story etc)
	Training cave (strategy,boss picks)
	Best gear :(general set, special cases (list those)
	Good teams (list those )
	Lore (non spoilered if possible)

How do I make a subcommand?
Use the group decorator. This will transform the callback into a Group which will allow you to add commands into the group operating as “subcommands”. These groups can be arbitrarily nested as well.

Example:

@bot.group()
async def git(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid git command passed...')

@git.command()
async def push(ctx, remote: str, branch: str):
    await ctx.send('Pushing to {} {}'.format(remote, branch))
This could then be used as ?git push origin master.
