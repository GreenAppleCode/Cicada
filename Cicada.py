import discord
from dotenv import load_dotenv
import os
import random
import requests
import json

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def joke():
  URL = requests.get('https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky')
  JSON_URL = URL.json()
  if JSON_URL["type"] == "twopart":
    return(JSON_URL["setup"], JSON_URL["delivery"])
  elif JSON_URL["type"] == "single":
    return(JSON_URL["joke"])

def bored():
    URL = requests.get("https://www.boredapi.com/api/activity")
    JSON_URL = URL.json()
    return(JSON_URL["activity"])

def quote():
    url = requests.get("https://api.kanye.rest/")
    json_url = url.json()
    return(json_url["quote"])

def dankmeme():
    url = requests.get("https://meme-api.herokuapp.com/gimme")
    json_url = url.json()
    return(json_url["url"])

def wholesome():
    url = requests.get("https://meme-api.herokuapp.com/gimme/wholesomememes")
    json_url = url.json()
    return(json_url["url"])

def cursed():
    url = requests.get("https://meme-api.herokuapp.com/gimme/cursed_images")
    json_url = url.json()
    return(json_url["url"])

def dice():
    dice = random.randint(1, 6)
    dice = str(dice)
    return("You rolled a " + dice + "!")

def d20():
    dice = random.randint(1, 20)
    dice = str(dice)
    return("You rolled a " + dice + "!")
load_dotenv('TOKEN.env')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$quote'):
        await message.channel.send(get_quote())
    if message.content.startswith('$help'):
        await message.channel.send('List of commands: $quote, $cheese, $joke, $bored, $kanyequote, $dankmeme, $wholesome, $dice, $d20')
    if message.content.startswith('$cheese'):
        await message.channel.send('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3FgIikw0pL7oRkr7rCwWNePwA-9yPfOduMw&usqp=CAU')
    if message.content.startswith('$joke'):
        await message.channel.send(joke())
    if message.content.startswith('$bored'):
        await message.channel.send(bored())
    if message.content.startswith('$kanyequote'):
        await message.channel.send(quote())
    if message.content.startswith('$dankmeme'):
        await message.channel.send(dankmeme())
    if message.content.startswith('$wholesome'):
        await message.channel.send(wholesome())
    if message.content.startswith('$cursed'):
        await message.channel.send(cursed())
    if message.content.startswith('$dice'):
        await message.channel.send(dice())
    if message.content.startswith('$d20'):
        await message.channel.send(d20())
client.run(os.getenv('TOKEN'))
