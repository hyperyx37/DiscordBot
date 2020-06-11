import discord
#print(discord.__version__)  # check to make sure at least once you're on the right version!
import sys
import time
import asyncio
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored

#Access to the token
f = open("discordbot.txt")
t = f.readlines()
token = t[1][9:-1]

client = discord.Client()  # starts the discord client.
def server_report(channel):
    online = 0
    offline = 0
    other = 0
    for m in channel.members:
        if str(m.status) == "online":
            online+=1
        elif str(m.status) == "offline":
            offline+=1
        else:
            other+=1
    return online,offline,other

async def background_report():
    await client.wait_until_ready()
    global channel
    channel = client.get_guild(669614816431833128)
    while not client.is_closed():
        try:
            online,offline,other = server_report(channel)
            with open("ServerReport.csv", "a") as report:
                report.write(f"{int(time.time())}, {online}, {offline}, {other}\n")
            
            #Visualize the server report
            plt.clf()
            df = pd.read_csv("ServerReport.csv", names = ['time', 'online', 'offline', 'other'])
            df["time(s)"] = pd.to_datetime(df['time'], unit = 's')
            df['total'] = df['online'] + df['offline'] + df['other']
            df.drop("time",1,inplace = True)
            df.set_index('time(s)', inplace = True)
            df.plot()
            plt.legend(loc = "upper right")
            plt.savefig("ServerReport.png")

            await asyncio.sleep(10)

        except Exception as e:
            print(str(e))
            await asyncio.sleep(10)




@client.event  # event decorator/wrapper.
async def on_ready():  # method expected by client. This runs once when connected   
    global channel

    print(f'We have logged in as {client.user}')  # notification of login.
@client.event
async def on_message(message):  # event that happens per any message.
    global channel
    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "!hi there" in  message.content.lower():
    	await message.channel.send("Sup!")
    if "!logout" in  message.content.lower():
    	await message.channel.send("Hypy out!")
    	sys.exit()
    if "!memberstatus" in message.content.lower():
        online,offline,other = server_report(channel)
        await message.channel.send(f"```cssThere are {len(channel.members)} members in the channel\nOnline: {online}.\nOffline: {offline}.\nOther: {other}.```")
        await message.channel.send(file = discord.File('ServerReport.png', filename = "ServerReport.png"))
client.loop.create_task(background_report())    	
client.run(token)  
