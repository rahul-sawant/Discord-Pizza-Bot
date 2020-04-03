
import discord
from discord.ext import commands
import pprint
from googleapiclient.discovery import build


api_key = ""
cs_key = ""

resource = build("customsearch", 'v1', developerKey=api_key).cse()

client = commands.Bot(command_prefix = 'order ')
@client.event
async def on_ready():
    print('Chef is ready')

@client.command(pass_context = True)
async def pizzu(ctx, *,question):
    await ctx.send(f'{question} pizzu for {ctx.message.author.mention} :pizza:')
    if "pizza" not in question:
        result = resource.list(q=question+'pizza', cx=cs_key, searchType='image').execute()
    else:
        result = resource.list(q=question, cx=cs_key, searchType='image').execute()
    l=[]
    for item in result['items']:
        link=item['link']
        l.append(link)
    await ctx.send(f'{l[0]}')

@client.command(pass_context = True)
async def juice(ctx, *,question):
    await ctx.send("Hi i am sharbu's assistant, filling in for sharbu while he is offline ^_^")
    await ctx.send(f'{question} juice for {ctx.message.author.mention} :beverage_box:')
    if "juice" not in question:
        result = resource.list(q=question+'juice', cx=cs_key, searchType='image').execute()
    else:
        result = resource.list(q=question, cx=cs_key, searchType='image').execute()
    l=[]
    for item in result['items']:
        link=item['link']
        l.append(link)
    await ctx.send(f'{l[0]}')

client.run('')
