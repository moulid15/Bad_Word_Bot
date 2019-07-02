import discord
import json
import os
from json.decoder import JSONDecodeError
from collections import defaultdict


message='nigger'
user='gecki'
if message.find('nigger')!=-1:
    print('someone said the N word....')
    filename = 'jsonFile.json'
    if os.path.exists(filename):
        with open(filename,'r') as jsonFile:
            d = json.load(jsonFile)
        if user in d:
            d[user] += 1
        else:
            d[user]=1
        with open(filename,'w') as f:
            l=dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
            json.dump(l,f, indent=4)
    else:
        print('wait for the bot to start')
print('finished')
