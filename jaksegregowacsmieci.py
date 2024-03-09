import discord
from discord.ext import commands
import os 


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def wyrzucam_plastik(ctx):
    wastebasket = os.listdir('kosze')
    eco='plastik_metal.webp'
    with open(f'kosze/{eco}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def wyrzucam_szkło(ctx):
    wastebasket = os.listdir('kosze')
    eco='szklo.jpg'
    with open(f'kosze/{eco}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def wyrzucam_papier(ctx):
    wastebasket = os.listdir('kosze')
    eco='papier.jpg'
    with open(f'kosze/{eco}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def wyrzucam_bioodpady(ctx):
    wastebasket = os.listdir('kosze')
    eco='bio.webp'
    with open(f'kosze/{eco}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
