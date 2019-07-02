import discord
import json
from json.decoder import JSONDecodeError

token = 'NTkzOTM1MzQxOTA0MzMwNzU0.XRjAzA.2_cgw5ie7VYB5zdfj-nU1BmZ86Y'

count = dict = {}
client = discord.Client()
counter=dict={}
count1=dict={}

async def counter1(channel):
    async for message in channel.history(limit=None):
        if message.content.lower().find('nigger') != -1 or message.content.lower().find('nigga') != -1:
            user = message.author.display_name
            if user in count1:
                count1[user] += 1
            else:
                count1[user]=1


async def counter2(channel):
    buffer2=''
    async for message in channel.history(limit=None):
        if message.content.lower().find('nigger') != -1 or message.content.lower().find('nigga') != -1:
            user = message.author.display_name
            # print(type(user))
            if user in count1:
                count1[user] += 1
            else:
                count1[user]=1
            counter=count1
    for i in count1.keys():
        buffer1='|        '+ str(i)+ '    |        ' +'$'+str(count1[i]*4) +  '     |'+'\n'
        buffer2 += buffer1
    await channel.send(" ``<-------------- N Word Score board ---------------->\n"+buffer2 +'``')


@client.event
async def on_message(message):
    if message.content.lower().find('!ncount') != -1:
        await counter1(message.channel)
        user = message.author.display_name
        print(count1)
        if user in count1:
            await message.channel.send('Hey thot you owe Snow:    ``'+'$'+ str(count1[user]*4)+'``')
        else:
            await message.channel.send('You are not a Racist')
        count1.clear()

    if message.content.lower().find('!allncount') != -1:
        await counter2(message.channel)
        count1.clear()

    if message.content.lower().find('send1') != -1:
        await message.channel.send('nigger')

# print(counter)
client.run(token)
