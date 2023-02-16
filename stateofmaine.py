import os
import random
import discord
import requests
import json
import youtube_dl
import asyncio


from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord import client

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)





load_dotenv()
TOKEN = os.getenv('MTAyODYyMzMyNjA1MjEwNjM5MQ.GwvHuH.zud8a8cPckeavueY_gPSXce9vm9BpvCrw7GpX4')

bot = commands.Bot(command_prefix='!') 

@bot.command(name='Maine_quotes')
async def big_edge(ctx):
    maine = [
        "This is it. It's the end of the line for me. But not for you. Fast is what you do best, ain't it? Just keep running.",
        "Aint nobody gonna set my limits but me.",
        "Ain't no one in this world you can trust more than yourself.",
        "It ain't a waste of ennies if it makes you stronger. That applies to your cyberware. And also, to your crew.",
        "I don't give two shits about people's past. As long as they pull their weight on the job, we're good.",
        "Everybody gets a fair shake. Only way I operate.",
        "You holdin up alright?",

    ]
    response = random.choice(maine)
    await ctx.send(response)

@bot.command(name='Maine_Quotes')
async def big_edge(ctx):
    maine2 = [
        "This is it. It's the end of the line for me. But not for you. Fast is what you do best, ain't it? Just keep running.",
        "Aint nobody gonna set my limits but me.",
        "Ain't no one in this world you can trust more than yourself.",
        "It ain't a waste of ennies if it makes you stronger. That applies to your cyberware. And also, to your crew.",
        "I don't give two shits about people's past. As long as they pull their weight on the job, we're good.",
        "Everybody gets a fair shake. Only way I operate.",
        "You holdin up alright?",

    ]
    response = random.choice(maine2)
    await ctx.send(response)

@bot.command(name='maine_quotes')
async def big_edge(ctx):
    maine3 = [
        "This is it. It's the end of the line for me. But not for you. Fast is what you do best, ain't it? Just keep running.",
        "Aint nobody gonna set my limits but me.",
        "Ain't no one in this world you can trust more than yourself.",
        "It ain't a waste of ennies if it makes you stronger. That applies to your cyberware. And also, to your crew.",
        "I don't give two shits about people's past. As long as they pull their weight on the job, we're good.",
        "Everybody gets a fair shake. Only way I operate.",
        "You holdin up alright?",

    ]
    response = random.choice(maine3)
    await ctx.send(response)

@bot.command(name='MAINE_QUOTES')
async def big_edge(ctx):
    maine4 = [
        "This is it. It's the end of the line for me. But not for you. Fast is what you do best, ain't it? Just keep running.",
        "Aint nobody gonna set my limits but me.",
        "Ain't no one in this world you can trust more than yourself.",
        "It ain't a waste of ennies if it makes you stronger. That applies to your cyberware. And also, to your crew.",
        "I don't give two shits about people's past. As long as they pull their weight on the job, we're good.",
        "Everybody gets a fair shake. Only way I operate.",
        "You holdin up alright?",

    ]
    response = random.choice(maine4)
    await ctx.send(response)



@bot.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('maine.wav')
        player = voice.play(source)
    else:
        await ctx.send("Get in this voice channel before I kick your ass dawg.")

@bot.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("End of the line for me, no more running. The Reaper finally calling my name.")
    else:
        await ctx.send("Keep Running David.")      












bot.run('')
    
