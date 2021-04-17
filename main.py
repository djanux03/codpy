from urllib import request
from bs4 import BeautifulSoup
import cloudscraper
import discord

TOKEN = "ODIxODU2NDI0NzYwOTY3MTY5.YFJzcQ.w8VpmqAjun8vBrgolTPDWrBtPKM"
site = "https://cod.tracker.gg/warzone/profile/battlenet/"
username = "BabaBlanco%232902/overview"
bot = discord.Client()

url = site + username
scraper = cloudscraper.create_scraper()
cod = scraper.get(url).text 

soup = BeautifulSoup(cod, 'html.parser')
title = soup.find('title')

@bot.event
async def on_message(message):
    if message.content == "cod":
        for div in soup.find_all('div', class_='numbers'):
            fact_title = div.find('span', class_='name').string
            #print(fact_title.string)
            num = div.find('span', class_='value').string
            await message.channel.send("```" +fact_title + ": " + num.string + "```")
      

def get_stats():
            
    
    return num
#, num


bot.run(TOKEN)
