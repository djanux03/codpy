from urllib import request
from bs4 import BeautifulSoup
import cloudscraper
import discord
from discord.ext import commands
TOKEN = "ODIxODU2NDI0NzYwOTY3MTY5.YFJzcQ.RMimsezFMK1Yojn3ElxQovJRbLU"
bot = discord.Client()
bot = commands.Bot(command_prefix="!")

site = "https://cod.tracker.gg/warzone/profile/battlenet/"
class codpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = ''
    def insertAfter(self, usersInput, context, newText):
        i = usersInput.find(context)
        return usersInput[:i + len(context)] + newText + usersInput[i + len(context):]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("!"):
            input = message.content
            input = input.replace('!', '')
            c = "#"

        newinput = self.insertAfter(input, c, "23")
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
            self.data += fact_title + ": " + num + "\n"
        await message.channel.send("```" + self.data + "\n```")
        self.data = ''


bot.add_cog(codpy(bot))
bot.run(TOKEN)
