from urllib import request
from bs4 import BeautifulSoup
import cloudscraper
from PIL import Image, ImageDraw, ImageFont
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
import random

load_dotenv('.env')
bot = discord.Client()
bot = commands.Bot(command_prefix="!")

class codpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.site = "https://cod.tracker.gg/warzone/profile/battlenet/"
        self.data = ''
        self.c = '#'
        self.monkeList = ["https://tenor.com/view/monki-monkey-monkeys-drip-swag-gif-20694900", "https://cdn.discordapp.com/attachments/826015642725384198/886673264615759932/chimpanzee-facts.jpg", "https://cdn.discordapp.com/attachments/826015642725384198/885942876473819156/Who2Bape2Ball2Bthe2Bpies2B2BOrangutan2Bkicks2Bback2Bwith2Ba2Bfull2Bbelly2Bin2Bthe2Bmidday2Bsun2B2B1.png", "https://cdn.discordapp.com/attachments/826015642725384198/886673029298536468/IMG_20210908_102456_658.webp", "https://cdn.discordapp.com/attachments/826015642725384198/885942432796135464/USER_SCOPED_TEMP_DATA_orca-image-1631091029884_6841291631009937321.jpeg", "https://cdn.discordapp.com/attachments/886673951701487656/886789481020141638/Monkey-Main-1280x600.jpg", "https://cdn.discordapp.com/attachments/886673951701487656/887188436564447292/images_1.jpeg", "https://cdn.discordapp.com/attachments/886673951701487656/887342741829324870/monke.PNG", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f9208768-ad5e-48ea-afb6-c5ffe6ac0fca/ded13a2-de3b402b-8d51-4fc6-aeec-50746f647fc4.jpg/v1/fill/w_413,h_403,q_75,strp/monke_with_drip_by_2zip_ded13a2-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDAzIiwicGF0aCI6IlwvZlwvZjkyMDg3NjgtYWQ1ZS00OGVhLWFmYjYtYzVmZmU2YWMwZmNhXC9kZWQxM2EyLWRlM2I0MDJiLThkNTEtNGZjNi1hZWVjLTUwNzQ2ZjY0N2ZjNC5qcGciLCJ3aWR0aCI6Ijw9NDEzIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.HmYNxD8raQvZhMGuykYZZyE-uyM8O0VG0gkWIr_mT1g", "https://cdn.discordapp.com/attachments/886673951701487656/886784717708468294/usf2rrSS.jpg", "https://cdn.discordapp.com/attachments/886673951701487656/886735588898766858/2745061459_6d4c9fd140_b.png", "https://cdn.discordapp.com/attachments/886673951701487656/886674246187761675/wbzkd6bk68u41.png"]
        
    def insertAfter(self, usersInput, context, newText):
        i = usersInput.find(context)
        return usersInput[:i + len(context)] + newText + usersInput[i + len(context):]

    def scrapeData(self, messageInput):
        newinput = self.insertAfter(messageInput, self.c, "23")
        userinput = newinput.replace('#', '%')
        print(userinput)
        fullurl = self.site + userinput
        scraper = cloudscraper.create_scraper()
        cod = scraper.get(fullurl).text 
        soup = BeautifulSoup(cod, 'html.parser')
        for div in soup.find_all('div', class_='numbers'):
            fact_title = div.find('span', class_='name').string
            #print(fact_title.string)
            num = div.find('span', class_='value').string
            self.data += fact_title + ": " + num + "\n"

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("!"):
            uinput = message.content
            uinput = uinput.replace('!', '')
            
        if message.content == "!monke":
            x = random.randint(0, len(self.monkeList))
            await message.channel.send(self.monkeList[x])
        
        self.scrapeData(uinput)
        await message.channel.send("```" + self.data + "\n```")

bot.add_cog(codpy(bot))
bot.run(os.getenv('BOT_TOKEN'))
