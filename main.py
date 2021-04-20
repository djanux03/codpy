from urllib import request
from bs4 import BeautifulSoup
import cloudscraper
import discord
from discord.ext import commands
TOKEN = "ODIxODU2NDI0NzYwOTY3MTY5.YFJzcQ.w8VpmqAjun8vBrgolTPDWrBtPKM"
bot = discord.Client()
bot = commands.Bot(command_prefix="!")

site = "https://cod.tracker.gg/warzone/profile/battlenet/"


def insertAfter(usersInput, context, newText):
 
  i = usersInput.find(context)
  return usersInput[:i + len(context)] + newText + usersInput[i + len(context):]

@bot.event
async def on_message(message):

    if message.content.startswith("!"):
        input = message.content
        input = input.replace('!', '')
        c = "#"
        
        #print([pos for pos, char in enumerate(input) if char == c])
        
        print(input)
        #context = scraper(input)
        #print(context)      
   
        newinput = insertAfter(input, c, "23")
        userinput = newinput.replace('#', '%')
        
        print(userinput)
        

        fullurl = site + userinput
        scraper = cloudscraper.create_scraper()
        cod = scraper.get(fullurl).text 

        soup = BeautifulSoup(cod, 'html.parser')
       
     
        for div in soup.find_all('div', class_='numbers'):
            fact_title = div.find('span', class_='name').string
            #print(fact_title.string)
            num = div.find('span', class_='value').string
            await message.channel.send("```" +fact_title + ": " + num.string + "```")

bot.run(TOKEN)
