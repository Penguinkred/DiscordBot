#!/usr/bin/env python
# Testing out how to make a discord bot.

import discord
import json
import language_check
from discord.ext import commands

spelling = language_check.LanguageTool('en-US')
bot = commands.Bot(description="Test DM reading bot", command_prefix="!", self_bot=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name)
    print("Is Bot?: " + str(bot.user.bot))


@bot.event
async def on_message(message):
    channelid = message.channel
    print("DM From: " + str(channelid.id))
    if discord.channel.DMChannel and channelid.id == "PUT CHANNEL ID HERE" and message.author != bot.user:
        print(message.content)
        matches = spelling.check(message.content)
        if len(matches) > 0:
            correction = spelling.correct(message.content)
            await message.channel.send("Errors Found! Did you mean: " + correction)

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
bot.run(token, bot=False)
