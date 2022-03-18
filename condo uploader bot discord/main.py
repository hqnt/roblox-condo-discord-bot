import sys
from requests import post, get
import requests
from os import name as os_name, system
#and i found an downloader
from discord import Webhook, RequestsWebhookAdapter
import codecs
import json
import discord
from discord.ext import commands
import secrets
from unblacklister import uniqueId, referentt, assetId
import os
from ad import advertise
import lxml.etree
from xml.dom import minidom
from xml.etree import ElementTree as etree
from keep_alive import keep_alive


bot = commands.Bot(command_prefix="-") #prefix for command
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='-Upload', url='https://www.twitch.tv/'))

def main(cookie):
    uniqueId()
    referentt()
    assetId()
    token = post("https://auth.roblox.com/v2/logout", 
                 cookies={
                     ".ROBLOSECURITY": cookie
                 }).headers['X-CSRF-TOKEN']
    userId = requests.get("https://users.roblox.com/v1/users/authenticated",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox',
                                "Connection": "keep-alive"
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["id"]
    print(f" [DATA] {userId}- UserID")
    gameId = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print(f" [DATA] {gameId} - GameID")
    myfiles = open("file.rbxlx", "rb").read()
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"]
    print(f" [DATA] {unvid} - UniverseID")
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration"

    avatartype = "MorphToR6"
    allowprivateservers = True

    gamedatao = {
        "name": "Generated Game",
        "description": " Created by Async ",
        "universeAvatarType": avatartype,
        "universeAnimationType": "Standard",
        "maxPlayerCount": 45,
        "allowPrivateServers": allowprivateservers,
        "privateServerPrice": 0,
        "permissions": {
            "IsThirdPartyTeleportAllowed": True,
            "IsThirdPartyPurchaseAllowed": True
        }
    }
    gameDump = json.dumps(gamedatao)
    gamestats = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameDump)
    gameData2 = {
        "maxPlayerCount": 45,
    }
    gamestat = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameData2)

    print(f" [DATA] {gamestat.status_code} - Successfull upload")
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox', 
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)  
    if upload.status_code == 200:
        webhook = Webhook.from_url(
            "https://discord.com/api/webhooks/931646191517700136/IJZOOfza-WOO5zHsmvY1qxN4IXPtpN6M9Y61MqPZ4mzaZFOaawa0Kvz-T8py-RPKuvTX",
            adapter=RequestsWebhookAdapter())
        webhook.send("💯**NEW GAME UPLOADED**💯")
        e = discord.Embed(title="Automatically Uploaded Condo",
        description="2 Player Condos! **https://discord.gg/eqcsaF2GZ3**")
        e.add_field(
            name="Game Link",
            value=
            f"__**[Click here to play!](https://www.roblox.com/games/{gameId}/)**__",
            inline=True)
        e.set_image(
            url=
            'https://cdn.discordapp.com/attachments/902654074799935538/946537182733172766/standard.png'
        )
        e.set_footer(text='Bot Created by Async#5015')
        webhook.send(embed=e)
        global link
        link = gameId
         

@bot.command()
async def Upload(ctx):
  embed = discord.Embed(
            title = "Condo Uploader v0.9 Created by Async#5015",
            description = "Please Insert a Valid Cookie!"
        )
  sent = await ctx.send(embed=embed)  
  cookieinput = await bot.wait_for("message")
  if '_|WARNING' in cookieinput.content:
         embed = discord.Embed(
            title = "Condo Uploader v0.9 Created by Async#5015",
            description = "Valid Cookie Uploading..."
        )
  else:
     await ctx.send(":x:**Invalid Cookie**:x:")
     return
  sent = await ctx.send(embed=embed) 
  await ctx.send(":white_check_mark:**Successfully Uploaded!**:white_check_mark: ")
  main(cookieinput.content)
  await ctx.send("Do you wish to advertise the game? (Say Y for yes or N for no) ")
  yn = await bot.wait_for("message")
  if 'y' in yn.content.lower():
      await ctx.send("**Marked as (Public)**")
      advertise(link)
  elif 'n' in yn.content.lower():
     await ctx.send(":x:**Marked as (Private)**:x:")
     #return

keep_alive()
bot.run(os.environ['token'])
