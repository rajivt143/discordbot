import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

jokeMessage = "The bot is malfunctioning if this is showing."


print("The bot has been created by Rajiv Thakar")
Client = discord.Client()
client = commands.Bot(command_prefix = "!")
def sendJoke():
    global jokeMessage
    secure_random = random.SystemRandom()
    randomJokes = ["When my Grandad was 65 he started running a mile a day to keep fit. He's 70 now and we have no idea where he is","Did you hear about the two guys that stole a calender? They each got six months", "I'm really good friends with 25 letters of the alphabet... I dont know Y.", "I wondered why the ball was getting bigger. And then it hit me!", "What did the pirate say when he turned 80? Aye matey!","Why cant bicycles stand up on their own? They are two tired"]
    jokeMessage = (secure_random.choice(randomJokes))
def rpsgame():
    global rockps
    randomchoice = ["Rock", "Paper", "Scissors"]
    secure_random = random.SystemRandom()
    rockps = (secure_random.choice(randomchoice))


@client.event
async def on_ready():
    print("Bot has just connected to the discord!")


@client.event
async def on_message(message):
    if message.content.lower() == "!commands":
        await client.send_message(message.channel, "Commands:\n !shrug - Puts a shrug emoji\n !ping - replies with pong\n !joke - Displays a random joke message\n !rock - its a rock paper scissors command. If you type this in, you have selected rock\n !paper - its a rock paper scissors command. If you type this in, you have selected paper.\n !scissors - its a rock paper scissors command. If you type this in, you have selected scissors.")
    if message.content.lower() == "!shrug":
        await client.send_message(message.channel, "¯\_(ツ)_/¯")
    if message.content.lower().startswith("!ping"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!"% (userID))
    if message.content.lower().startswith("!joke"):
        sendJoke()
        await client.send_message(message.channel, jokeMessage)
    if message.content.lower() == ("!paper" and "!scissors" and "!rock"):
        for i in range(1):
            rpsgame()
        await client.send_message(message.channel, rockps)
client.run("Mzk4NjA1Nzg2MDA1MzcyOTU4.DTA-9Q.-c74hUO4Ch-jM-NtWKvWDkrwMuc")
