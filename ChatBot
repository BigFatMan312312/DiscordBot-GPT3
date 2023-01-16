import discord
import openai

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
openai_token = None

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
    msg = await channel.fetch_message(message.id)
    print(msg.content.replace("!chat ",""))
    if msg.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif msg.content.startswith('!help'):
        await message.channel.send('!set_token <token> - Set the OpenAI token\n!chat <text> - Chat with the bot')
    elif msg.content.startswith('!set_token'):
        global openai_token
        openai_token = msg.content.split(' ')[1]
        await message.channel.send(f'OpenAI token set to: {openai_token}')
    elif msg.content.startswith('!chat'):
        if openai_token is None:
            await message.channel.send("Please set the OpenAI token before using this command.")
        else:
            openai.api_key = openai_token
            text = msg.content.replace("!chat ","")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=text,
                max_tokens=1024,
                n = 1,
                stop=None,
                temperature=0.7,
            )
            await message.channel.send(response["choices"][0]["text"])



client.run('OTU3MTU3ODAyODM5NzczMTg0.GyCcsP.k-tBeDXtj8CJNkI1R9oJWklyzR8jEve82BoyQE')
