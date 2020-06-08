# Client ID: 669615529937469470
# Token: NjY5NjE1NTI5OTM3NDY5NDcw.XiiaFg.efu5F9wCUm8gaB30TJ7uGtZsZ7c
# Permission Int: 67648

# https://discordapp.com/oauth2/authorize?client_id=669615529937469470&scope=bot&permissions=67648
import discord
#print(discord.__version__)  # check to make sure at least once you're on the right version!
import sys
token = "NjY5NjE1NTI5OTM3NDY5NDcw.XiiaFg.efu5F9wCUm8gaB30TJ7uGtZsZ7c"

client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    channel = client.get_guild(669614816431833128)
    if "!hi there" in  message.content.lower():
    	await message.channel.send("Sup!")
    if "!logout" in  message.content.lower():
    	await message.channel.send("Hypy out!")
    	sys.exit()
    if "!memberstatus" in message.content.lower():
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
        await message.channel.send(f"```There are {len(channel.members)} members in the channel\nOnline: {online}.\nOffline: {offline}.\nOther: {other}.```")

    	
client.run(token)  # recall my token was saved!
