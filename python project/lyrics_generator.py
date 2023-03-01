print("Please select a song from this top 5 songs")

artists = ['Justin Bieber', 'Lewis Capaldi', 'Charlie Puth']

print(artists)
user_input = ''

input_message = "Pick an option: \n"

for index, item in enumerate(artists):
    input_message += f'{index+1}) {item}\n'
input_message += 'Your choice: '

while artists:
    user_input = input(input_message)
    if(user_input == "Justin Bieber"):
        justin_song = "Baby, Love Me, Ghost"
        justin = input("These are some of his songs; " + justin_song + ", choose one: ")
        if(justin == "Baby"):
            print("--Baby by Justin Bieber--")
            print("...You know you love me, I know you care")
            print("Just shout whenever and I'll be there")
            print("You are my love, you are my heart")
            print("and we will never, ever, ever be apart...")
        elif(justin == "Love Me"):
            print("...love me, love me")
            print("say that you love me...")
        elif(justin == "Ghost"):
            print("...Since the love that you left is all that i get")
            print("I want you to know that if i can't be close to you")
            print("I'll settle for the ghost of you")
            print("I miss you more than life")
            print("And if you can't be next to me")
            print("Your memory is ecstasy")
            print("I miss you more than life")
            print("I miss you more than life...")
        else:
            print("Sorry we did not find anything")
        star = input("press * to choose again: ")
        if(star == "*"):
            print(user_input)
    elif(user_input == "Lewis Capaldi"):
        lewis_song = "Before you go, Someone you loved, Hold me while you wait"
        lewis = input("These are some of his songs; " + lewis_song + ", choose one: ")
        if(lewis == "Before you go"):
            print("--Before you go--")
            print("... So, before you go, was there something I could've said to make your heart beat better?")
            print(" If only I'd have known you had a storm to weather")
            print("So, before you go, was there something I could've said to make it all stop hurting?")
            print("So, before you go...")
        elif(lewis == "Someone you loved"):
            print("... Now the day bleeds")
            print("Into nightfall")
            print("And you're not here")
            print("To get me through it all")
            print("I let my guard down")
            print("And then you pulled the rug")
            print("I was getting kinda used to being someone you loved...")
        elif(lewis == "Hold me while you wait"):
            print("... I wish you cared a little more (Hold me while you wait)")
            print("I wish you'd told me this before (Hold me while you wait)")
            print("My love, my love, my love, my love")
            print("Won't you stay a while? (Hold me while you wait)...")
        else:
            print("Sorry we did not find anything")
        star = input("press * to choose again: ")
        if(star == "*"):
            print(user_input)
    elif(user_input == "Charlie Puth"):
        Charlie_song = "Attention, We don't talk anymore, One call away"
        Charlie = input("These are some of his songs; " + Charlie_song + ", choose one: ")
        if(Charlie == "Attention"):
            print("...You just want attention, you don't want my heart")
            print("Maybe you just hate the thought of me with someone new")
            print("Yeah, you just want attention, I knew from the start")
            print("You're just making sure I'm never getting over you, oh...")
        elif(Charlie == "We don't talk anymore"):
            print("We don't talk anymore")
            print("We don't talk anymore")
            print("We don't talk anymore")
            print("Like we used to do")
            print("We don't love anymore")
            print("What was all of it for?")
            print("Oh, we don't talk anymore")
            print("Like we used to do...")
        elif(Charlie == "One call away"):
            print("--One Call Away( by Charlie Puth)--")
            print("I'm only one call away")
            print("I'll be here to save the day")
            print("Superman got nothing on me")
            print("I'm only one call away...")
        else:
            print("Sorry we did not find anything")
        star = input("press * to choose again: ")
        if(star == "*"):
            print(user_input)
    else:
        print("Sorry we did not find anything")

print("GoodBye")