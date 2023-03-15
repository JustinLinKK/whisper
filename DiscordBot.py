import discord
from discord.ext import commands
import whisper



TOKEN = 'Token'
intents = discord.Intents.default()
intents.message_content = True

model = whisper.load_model("base")


# 2
bot = commands.Bot(command_prefix='$',intents=intents)

@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)


@bot.command()
async def audioToText(ctx):
    files = []
    for attachment in ctx.message.attachments:
        # fp = BytesIO()
        audioName = attachment.filename
        await attachment.save(attachment.filename)
        result = model.transcribe(audioName)
        await ctx.send(result["text"])
        


    


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


        

    
        
		
                
    
    







    



    



bot.run(TOKEN)


