import discord
import openai

client = discord.Client()
openai_token = None

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('!set_token'):
        global openai_token
        openai_token = message.content.split(' ')[1]
        await message.channel.send(f'OpenAI token set to: {openai_token}')
    elif message.content.startswith('!chat'):
        if openai_token is None:
            await message.channel.send("Please set the OpenAI token before using this command.")
        else:
            openai.api_key = openai_token
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=(f"{message.content.split(' ')[1]}"),
                max_tokens=1024,
                n = 1,
                stop=None,
                temperature=0.7,
            )
            await message.channel.send(response["choices"][0]["text"])

client.run('OTU3MTU3ODAyODM5NzczMTg0.GibJPD.aOpPNj3F_MmQlqd1NMVlLQ_FaP0xN7NPqLBKIw')
