import discord
from discord.ext import commands
TOKEN = "ODIxODU2NDI0NzYwOTY3MTY5.YFJzcQ.k-KGO5qC7pzbLePZnWEMEbzen9M"
bot = discord.Client()
bot = commands.Bot(command_prefix="!")

site = "https://cod.tracker.gg/warzone/profile/battlenet/"
class codpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def insertAfter(self, usersInput, context, newText):
        i = usersInput.find(context)
        return usersInput[:i + len(context)] + newText + usersInput[i + len(context):]

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content.startswith("!"):
            input = message.content
            input = input.replace('!', '')
            c = "#"

                
        #print([pos for pos, char in enumerate(input) if char == c])
        
        print(input)
        #context = scraper(input)
        #print(context)      
   
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
            await message.channel.send("```" +fact_title + ": " + num.string + "```")

bot.add_cog(codpy(bot))
bot.run(TOKEN)
