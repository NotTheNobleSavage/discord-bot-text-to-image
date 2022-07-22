#Make sure you are using discord py 2.0.0 or higher
import discord
#Pillow Libery
from PIL import Image, ImageDraw, ImageFont

#secret.py with token stored
import secret

#Intents so bot can interact with stuff
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#Creates the command container 
tree = discord.app_commands.CommandTree(client)

#Enter guild_id here
guild_id = discord.Object(id = 'id')

#Simple on ready with command sync
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await tree.sync(guild = guild_id)

#The command
@tree.command(
    guild = guild_id, 
    name = "wordtext", 
    description = "Get an image from text", 
)
#Gets the word that you want to convert into image
async def slash(interaction: discord.Interaction, word: str):
    #Sets the font annd font size and get size of image
    myFont = ImageFont.truetype('C:\Windows\Fonts\calibril.ttf', 200)
    w,h = myFont.getsize(word)

    #Make and draw the image from the imput of the user
    img = Image.new('RGB', (w, h), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((0,0), word, font=myFont, fill=(255,255,0))
    #Saves the image
    img.save('image.png')
    #Sends the image
    await interaction.response.send_message("Here you go", file=discord.File("image.png"))

if __name__ == '__main__':
    client.run(secret.token)
