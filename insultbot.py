import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
from sys import platform


load_dotenv('.env')
bot = commands.Bot(command_prefix='!',
                   description="A bot that hates everyone")


def LoadInsults():
    with open('insults.txt', 'r') as file:
        lines = file.readlines()
    return lines


# ------ EVENTS ---------------------------------------------------------------
@bot.event
async def on_ready():
    global insults, prcnt
    prcnt = 1
    insults = LoadInsults()
    print(f'\n{bot.user.name} is up and running!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Wrong input. Integers only')
    else:
        await ctx.send(f'Error: {error}')


# ------ ADMIN COMMANDS ------------------------------------------------------
@bot.command(pass_context=True)
async def reload_insults(ctx):
    if ctx.message.author.guild_permissions.administrator:
        global insults
        insults = LoadInsults()
        n = len(insults)
        if n == 1:
            await ctx.send('One insult loaded...\n'
                           'Creativity is my middle name')
        elif n < 10:
            await ctx.send(f'{n} insults loaded...')
        else:
            await ctx.send(f'{n} insults loaded...\nI know Kung Fuck U')
            if platform == "linux" or platform == "linux2":
			    await ctx.send(file=discord.File(r'media/showme.png'))
			elif platform == "win32":
			    await ctx.send(file=discord.File(r'media\showme.png'))
    else:
        pass


@bot.command(pass_context=True)
async def killbot(ctx):
    if ctx.message.author.guild_permissions.administrator:
        raise SystemExit
    else:
        pass


# ------ USER COMMANDS -------------------------------------------------------
@bot.command()
async def info(ctx):
    global insults, prcnt
    embed = discord.Embed(title=f"{bot.user.name} info",
                          color=discord.Color.blue())
    embed.add_field(name="Loaded insults",
                    value=f'{len(insults)}',
                    inline=False)
    embed.add_field(name="Chance for an insult",
                    value=f'{prcnt}%',
                    inline=False)
    embed.add_field(name="Available commands",
                    value="""
                    !chance X - Change the % chance for an insult
                    !info - Opens this panel
                    !insult_me - Insult on demand!
                    """,
                    inline=False)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons'
                        '/thumb/2/25/Info_icon-72a7cf.svg/'
                        '1200px-Info_icon-72a7cf.svg.png')
    await ctx.send(embed=embed)


@bot.command()
async def insult_me(ctx):
    global insults
    # Handling empty insult list
    if len(insults) == 0:
        await ctx.send("It doesn't look like anything to me")
    else:
        ins = random.choice(insults).replace('$', ctx.author.name)
        await ctx.send(f'{ins}')


@bot.command()
async def chance(ctx, num=1):
    global prcnt
    prcnt = int(num)

    if prcnt > 100:
        prcnt = 100
    elif prcnt < 0:
        prcnt = 0

    await ctx.send(f'Insult chance changed to {prcnt}%. Good luck!')


# ------ RESPONSE ------------------------------------------------------------
@bot.listen()
async def on_message(message):
    global insults, prcnt

    # Make sure it's not a bot or a command
    if not message.author.bot and not message.content.startswith('!'):

        # Handling empty insult list
        if len(insults) == 0:
            print('Insult list is empty.')
        else:
            roll = random.randint(1, 100)
            if roll <= prcnt:
                ins = random.choice(insults).replace('$', message.author.name)
                await message.channel.send(f'{ins}')
                await bot.process_commands(message)
            else:
                pass

if platform == "linux" or platform == "linux2":
    bot.run(os.environ.get('BOT_TOKEN'))
elif platform == "win32":
    bot.run(os.getenv('BOT_TOKEN'))
