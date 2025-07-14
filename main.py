import discord
from discord.ext import commands
import os
import uuid
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)




@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment. save(f"./{attachment. filename}")
            await ctx.send(f"Guarda la imagen en ./{attachment. filename}")
            await ctx.send(get_class(model_path="Path to model", labels_path="Path to labels", image_path="Path to image"))
    else:
        await ctx.send("Olvidaste subir la imagen : (")
