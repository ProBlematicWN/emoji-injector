import random

def emote():
    all_emojis = list('😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰🤩🙄😛😜🤯😤😨😲😭🥵🤬🤮🥺😈🤓👹💀☠👽🐖🐏🦀💪✌🎈🍑🍆✈🔥⚡') #avaliable emoji list
    random_emoji = str(random.choice(all_emojis))
    random1 = random.randint(0,1)
    if random1 == 0:
        random_emoji = random_emoji*2 #random amount of emojis between words
    return random_emoji

def entered(b):
    a = ' '
    for a in b:
        random2 = random.randint(0, 1)
        if random2 == 0:
            replaced = b.replace(' ', emote(), 1)
        else:
            replaced = b.replace(' ', emote(), 1)

        b = replaced
    b = b.replace('⠀', ' ')
    print(b)
while True:
    inp = input('enter text:')
    entered(inp)

#new list: 😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰🤩🙄😛😜🤯😤😨😲😭🥵🤬🤮🥺😈🤓👹💀☠👽🐖🐏🦀💪✌🎈🍑🍆✈🔥⚡
#old list: 😎🔥🤬😈🤙💥🔥🥰🦀♥️🖕👹😏💪✈✈️💥🤣🍉🔥😎🤙👹🤣💩🤮😈🤣💪🍉🍉🤭🥰🔥

