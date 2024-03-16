import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f' no witam ja jestem {bot.user} a ty? ')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def mem_p(ctx):
    pictures_names = os.listdir('images')
    meme= random.choice(pictures_names)
    with open(f'images/{meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem_a(ctx):
    meme_names = os.listdir('animals')
    memes= random.choice(meme_names)
    with open(f'animals/{memes}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

@bot.command('password')
async def password(ctx, length= 5):
    await ctx.send(gen_pass(length))

@bot.command('pomocy')
async def pomocy(ctx):
    await ctx.send('żeby korzystać z komend nalezy użyć znaku --> $ ')
    await ctx.send('w przyszłości pojawią się tu informacje dotyczące działania komend, wyczekuj!!!')

bot.run("TOKEN")
