import random

def handle_response(message) -> str:
    p_message = message.lower()
    match p_message:
        case str if p_message.startswith(('hello', 'hi', 'hey')):
            return get_random_greeting()
        case 'roll':
            return f'You rolled a {random.randint(1, 6)}!'
        case '!help':
            return (
                "Here are some commands you can use:\n"
                "`hello` - Greet the bot\n"
                "`roll` - Roll a dice\n"
                "`!help` - Display this help message\n"
                "`!joke` - Tell a joke\n"
                "`!quote` - Get a random quote\n"
                "`!cat` - Show a random cat picture"
                "`!fact` - Tells you a random fact"
            )
        case '!joke':
            return get_random_joke()
        case '!quote':
            return get_random_quote()
        case '!cat':
            return get_random_cat_picture()
        case '!fact':
            return generate_random_fact()
        case _:
            return "I don't understand what you said"


def get_random_greeting() -> str:
    greetings = [
        "Hey there!",
        "Hello!",
        "Hi!",
        "Greetings!",
        "Howdy!",
        "Hey!",
        "Hey, how's it going?",
    ]
    return random.choice(greetings)


def get_random_joke() -> str:
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I used to play piano by ear, but now I use my hands.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
        "Parallel lines have so much in common. It's a shame they'll never share a joke.",
        "Why don't skeletons fight each other? They don't have the guts! Well, technically, they don't have much of anything.",
    ]
    return random.choice(jokes)


def get_random_quote() -> str:
    quotes = [
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston S. Churchill",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
    ]
    return random.choice(quotes)


def get_random_cat_picture() -> str:
    base_url = "https://placekitten.com/"
    width = random.randint(200, 800)
    height = random.randint(200, 600)
    return f"{base_url}{width}/{height}"

def generate_random_fact() -> str:
    facts = [
        "Did you know that honey never spoils? Archaeologists have discovered pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly good to eat!",
        "In Japan, there's a town called 'Nagoro' where there are more scarecrows than humans. An artist created over 350 scarecrow dolls to represent the dwindling human population.",
        "Bananas are berries, but strawberries are not!",
        "The inventor of the frisbee was turned into a frisbee. Walter Morrison, the inventor of the frisbee, was turned into a frisbee-like flying disc when he passed away in 2010.",
        "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
        "The unicorn is the national animal of Scotland.",
        "A day on Venus is longer than its year. Venus takes about 243 Earth days to rotate on its axis, but only about 225 Earth days to orbit the Sun.",
        "Bananas are berries, but strawberries aren't.",
        "Octopuses have three hearts.",
        "Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "The world's largest desert is Antarctica.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896, lasting only 38 minutes.",
        "Cows have best friends and can become stressed when separated from them.",
        "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of iron in the heat.",
        "Banging your head against a wall burns 150 calories per hour (but we don't recommend it!)",
        "In Switzerland, it's illegal to own just one guinea pig because they're prone to loneliness.",
        "There are more possible iterations of a game of chess than there are atoms in the known universe.",
        "Did you know that honey never spoils? Archaeologists have discovered pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly good to eat!",
        "In Japan, there's a spa where you can swim in a pool of red wine. It's believed to be good for the skin!",
        "The unicorn is the national animal of Scotland.",
    ]
    return random.choice(facts)
