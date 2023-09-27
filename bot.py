import discord
import aiohttp
import io
import responses
from dotenv import dotenv_values


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_image(message, image_url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status != 200:
                    print('Could not download image.')
                    return

                image_data = await resp.read()

                # Send the image as a file
                file = discord.File(io.BytesIO(image_data), filename="image.png")
                await message.channel.send(file=file)
    except Exception as e:
        print(e)


def generate_rules_and_abilities():
    return (
        "Hi! I am discord bot\n\n"
        "Here are some rules and abilities of me:\n"
        "- Type 'hello' to greet the me.\n"
        "- Type 'roll' to roll a dice.\n"
        "- Type '!help' to get a help message.\n"
        "- Type '!rules' to get the rules and abilities."
        "- Type `!joke` - Tell a joke\n"
        "- Type `!quote` - Get a random quote\n"
        "- Type `!cat` - Show a random cat picture\n"
        "- Type `!fact` - Tells you a random fact"
    )


def run_discord_bot():
    TOKEN = dotenv_values('.env')['TOKEN']
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user}: is now running!")
        for guild in client.guilds:
            for channel in guild.text_channels:
                try:
                    await channel.send(generate_rules_and_abilities())
                except discord.Forbidden:
                    pass
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = message.content
        channel = str(message.channel)

        print(f"{username} said: '{user_message} ({channel})'")

        if len(user_message) > 0:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            elif user_message.lower() == '!rules':
                await message.channel.send(generate_rules_and_abilities())
            elif user_message.lower().startswith('!cat'):
                image_url = responses.get_random_cat_picture()
                await send_image(message, image_url)
            else: 
                await send_message(message, user_message, is_private=False)

    client.run(TOKEN)