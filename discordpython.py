
# https://discordapp.com/oauth2/authorize?client_id=669615529937469470&scope=bot&permissions=67648
import discord
#print(discord.__version__)  # check to make sure at least once you're on the right version!
import sys
import time
import asyncio
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

    while not client.is_closed():
        try:
            online,offline,other = server_report(channel)
            with open("ServerReport.csv", "a") as report:
                report.write(f"{int(time.time())}: {online}, {offline}, {other}\n")
            await asyncio.sleep(5)
        except Exception as e:
            print(str(e))
            await asyncio.sleep(5)




@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected   
    global channel
    channel = client.get_guild(669614816431833128)
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
        await message.channel.send(f"```There are {len(channel.members)} members in the channel\nOnline: {online}.\nOffline: {offline}.\nOther: {other}.```")

client.loop.create_task(background_report())    	
client.run(token)  # recall my token was saved!
