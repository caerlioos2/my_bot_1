import discord
from discord.ext import commands
import random
import os

 

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)
cot_2 = [ "Puedes reciclar basura.",
         "Utiliza bicicleta.",
         "Intenta no tirar basura al agua."
         
                  
         
         ]

cot_3 = [ "Tu reto diario es: ¡Botar basura! (0/10)",
         "Tu reto diario es: ¡Utilizar bicicleta! (0/2km)",
         "Tu reto diario es: ¡No botes basura al agua! (0/10h)",
        "Tu reto diario es: ¡Recoje busara por tu casa! (0/10)",
        "Tu reto diario es: ¡Recoje busara de tu sector! (0/50)",
]

cot_4 = [ "Tu reto semanal es: ¡Botar basura! (0/100)",
         "Tu reto semanal es: ¡Utilizar bicicleta! (0/12km)",
         "Tu reto semanal es: ¡No botes basura al agua! (0/24h)",
        "Tu reto semanal es: ¡Recoje busara por tu casa! (0/30)",
        "Tu reto semanal es: ¡Recoje busara de tu sector! (0/250)",
]

ayuda_1 = ["Comandos disponibles:   !cot     !cot2     !cot3     !cot4"]
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def cot(ctx):

    img_name = random.choice(os.listdir("conta"))
    with open(f'conta/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.

    await ctx.send(file=picture)

@bot.command()
async def cot2(ctx):
     
     pre = random.choice(cot_2)
     await ctx.send(pre)

@bot.command()
async def cot3(ctx):
     
     ret = random.choice(cot_3)
     await ctx.send(ret)

@bot.command()
async def cot4(ctx):
     
     sem = random.choice(cot_4)
     await ctx.send(sem)

@bot.command()
async def ayuda(ctx):
     
     ayuda1 = random.choice(ayuda_1)
     await ctx.send(ayuda1)
     



bot.run("token")
