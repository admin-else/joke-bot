import interactions, random, dotenv, os, json

with open('./dataset/jokes.json', 'r') as f:
    jokes = json.load(f)

dotenv.load_dotenv('settings.env')

bot = interactions.Client(token=os.getenv('DISCORD_BOT_TOKEN'))

@bot.event
async def on_ready():
    print(f'ready as {bot.me.name}')

@bot.command(name='gimmeajoke',
             description='Gives you a random joke.',
             options=[
                interactions.Option(
                    type=interactions.OptionType.STRING,
                    name='joke_type',
                    description='Choose what kinda Joke you want.',
                    required=False,
                    choices=[
                        interactions.Choice(name = 'Reddit',         value = 'Reddit'),
                        interactions.Choice(name = 'Animal',          value = 'Animal'),
                        interactions.Choice(name = 'Other / Misc',    value = 'Other / Misc'),
                        interactions.Choice(name = 'Bar',             value = 'Bar'),
                        interactions.Choice(name = 'One Liners',      value = 'One Liners'),
                        interactions.Choice(name = 'Puns',            value = 'Puns'),
                        interactions.Choice(name = 'Lawyer',          value = 'Lawyer'),
                        interactions.Choice(name = 'Sports',          value = 'Sports'),
                        interactions.Choice(name = 'Medical',         value = 'Medical'),
                        interactions.Choice(name = 'News / Politics', value = 'News / Politics'),
                        interactions.Choice(name = 'Men / Women',     value = 'Men / Women'),
                        interactions.Choice(name = 'Gross',           value = 'Gross'),
                        interactions.Choice(name = 'Blond',           value = 'Blond'),
                        interactions.Choice(name = 'Yo Momma',        value = 'Yo Momma'),
                        interactions.Choice(name = 'Redneck',         value = 'Redneck'),
                        interactions.Choice(name = 'Religious',       value = 'Religious'),
                        interactions.Choice(name = 'At Work',         value = 'At Work'),
                        interactions.Choice(name = 'College',         value = 'College'),
                        interactions.Choice(name = 'Lightbulb',       value = 'Lightbulb'),
                        interactions.Choice(name = 'Children',        value = 'Children'),
                        interactions.Choice(name = 'Insults',         value = 'Insults'),
                        interactions.Choice(name = 'Knock-Knock',     value = 'Knock-Knock'),
                        interactions.Choice(name = 'Tech',            value = 'Tech'),
                        interactions.Choice(name = 'Yo Mama',         value = 'Yo Mama'),
                        interactions.Choice(name = 'Blonde',          value = 'Blonde'),
                    ]
                )
             ])
async def gimmeajoke(ctx: interactions.CommandContext, joke_type = None):
    filtered_jokes = jokes
    embed_fieleds = []

    if joke_type == None:
        joke_type = random.choice(['Reddit', 'Animal', 'Other / Misc', \
        'Bar','One Liners', 'Puns', 'Lawyer', 'Sports', 'Medical',     \
        'News / Politics', 'Men / Women', 'Gross', 'Blond','Yo Momma', \
        'Redneck','Religious','At Work','College','Lightbulb',         \
        'Children','Insults', 'Knock-Knock', 'Tech','Yo Mama','Blonde'
        ])

    filtered_jokes = [joke for joke in jokes if joke['category'] == joke_type]
    joke = random.choice(filtered_jokes)
    await ctx.send('**{}**\n\n{}\n\nCategory: {}'.format(joke.get('title', ''), joke['body'], joke['category']))

bot.start()

