import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from keep_alive import keep_alive
from discord.utils import get
from itertools import cycle
from yt import yt
from dice_roll import dice_roll
from ruokalista import ruokalista

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

#status = cycle(['Status1','Status2'])

@bot.event
async def on_ready():
  #change_status.start()
  print(f'{bot.user.name} has connected to Discord!')

'''@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))'''

@bot.event
async def on_member_join(member):
  print(member)
  await member.create_dm()
  await member.send('Tervetuloa. Kirjoita eteiskanavalle !ihminen päästäksesi muillekin kanaville.')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  if message.content.startswith('vastaa'):
    print(message.content)
    await message.channel.send('ootas')
    #await member.create_dm()
    #await member.dm_channel.send('testii')
  
  await bot.process_commands(message)

@bot.event
async def on_error(event, *args, **kwargs):
  with open('err.log', 'a') as f:
    if event == 'on_message':
      f.write(f'Unhandled message: {args[0]}\n')
    else:
      raise

@bot.command(name='dm')
@commands.has_role('Admin')
async def dmsg(ctx, member:discord.Member, *, message=None):
  message = message or "testiviesti"
  await member.send(message)

@bot.command(name='idea')
@commands.has_role('Admin')
async def idea(ctx, *args):
  with open('ideat.txt', 'a') as f:
    f.write('Idea: '+' '.join(args)+'\n')

@bot.command(name='yt', help='Hae videota youtubesta kirjoittamalla hakusanoja, esim. !yt davie504 slap bass.')
async def hae(ctx, *args):
  query = '+'.join(args) or 'mariah+carrey+all+i+want+for+christmas+is+you'
  await ctx.send('https://www.youtube.com/watch?v='+yt(query))

@bot.command(name='roll', help='Heitä noppaa kirjoittamalla esim. !roll 3d7.')
async def roll(ctx, throw):
  await ctx.send(dice_roll(throw))

@bot.command(name='ihminen')
async def addrole(ctx):
  member = ctx.author
  role = get(member.guild.roles, name='Normi')
  if ctx.channel.id == 909155927205245008:
    channel = bot.get_channel(908427006465687576)
    await member.add_roles(role)
    await channel.send(f'{member} liittyi serverille.')

@bot.command(name='skribbl', help='Avaa uuden pelin. Sanalista ja varsinainen privapeli täytyy tehdä itse :(')
async def skribl(ctx):
  await ctx.send('https://skribbl.io/')

@bot.command(name='ruoka', help='Arvo haluamasi määrä ruokaideoita kirjoittamalla esim. !ruoka 5.')
async def ruoka(ctx, numero=1):
  try:
    num = int(numero)
    await ctx.send(', '.join(ruokalista(num)))
  except:
    await ctx.send('Liikaa vaadittu!')
    raise Exception('jeejee')
  
    
  

@bot.command(name='clear')
@commands.has_role('Admin')
async def clear(ctx):
  await ctx.channel.purge()


keep_alive()

def run():
  bot.run(TOKEN)
