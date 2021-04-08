import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('Who is Rex\'s Cute Wife?'):
        await message.channel.send('The smartest girl Sammie!')
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))
    if message.content.startswith('👍'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
    if message.content.startswith('$clap'):
        channel = message.channel
        await channel.send('Send me that 👏 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👏'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('😒')
        else:
            await channel.send('😘')

client.run('ODI0NDkzOTI3NjU4Njg0NDc3.YFwLzg.53PGoON1M9_bPBwZ3l8sGMcivM0')
