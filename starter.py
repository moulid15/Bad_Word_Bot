import discord
import json
from json.decoder import JSONDecodeError

token = 'NTkzOTM1MzQxOTA0MzMwNzU0.XRjAzA.2_cgw5ie7VYB5zdfj-nU1BmZ86Y'

count = dict = {}

client = discord.Client()

# counter = 0
counter=dict={}
async def counter1(channel):
    count1=dict={}
    buffer2=''
    async for message in channel.history(limit=200):
        if message.content.lower().find('nigger') != -1 or message.content.lower().find('nigga') != -1:
            user = message.author.display_name
            # print(type(user))
            if user in count1:
                count1[user] += 1
            else:
                count1[user]=1

    for i in count1.keys():
        buffer1='|        '+ str(i)+ '    |        ' +str(count1[i]) +  '     |'+'\n'
        buffer2 += buffer1
    await message.channel.send(" ``<-------------- N Word Score board ---------------->\n"+buffer2 +'``')
    # await message.channel.send('``'+json.dumps(count1,sort_keys=True, indent=4)+'``')

@client.event
async def on_message(message):


    if message.content.lower().find('!ncount') != -1:
        user = message.author.display_name
        if user in count:
            await message.channel.send(str(count[user]))
        else:
            await message.channel.send('You are not a Racist')


        # print(message.author)
    if message.content.lower().find('!allncount') != -1:
        # count = counter(message.channel)
        # print(list(count))
        await counter1(message.channel)

        # for i in count:
        #     await message.channel.send('user: '+ str(i) + '  Count: ' + str(count[i]))
    if message.content.lower().find('send1') != -1:
        await message.channel.send('nigger')

# print(counter)
client.run(token)
