#Student Name: [Yonatan Nof]
#Bot Name: [Tuki]
#Bot Purpose: [have fun!]

import random
import time

#bot variables
bot_name = "Tuki the Bot"

#lists
greetings  = ["Hi!", "Hello!", "Welcome!", "Hey there!", "Nice to neet you!"]

goodbyes = ["Goodbye!", "Bye!", "See you!" "Take care!" "Have a nice day!"]

jokes = ["Why dont scientists trust atoms? Because they make up everything.", 
         "Why did the math book look sad? Because it had too many problems.",
         "Why don’t programmers like nature? It has too many bugs.",
         "Why did the computer go to the doctor? Because it caught a virus.",
         "Why was the equal sign so humble? Because it knew it wasn’t less than or greater than anyone else." 
         ]

compliments = [
    "You're awesome!",
    "Great job!",
    "You’re doing amazing!",
    "Well done!",
    "Keep up the great work!"
]

facts = [
    "Did you know octopuses have three hearts?",
    "Fun fact: Honey never spoils.",
    "Did you know the human brain uses about 20% of the body’s energy?",
    "Fun fact: Bananas are berries, but strawberries aren’t.",
    "Did you know space is completely silent?"
]

tips = [
    "Tip: Take short breaks to stay focused.",
    "Remember to save your work often.",
    "Tip: Practice a little every day.",
    "Remember to stay hydrated.",
    "Tip: Break big problems into smaller ones."
]

#HELPER FUNCTIONS
def print_separator():
    print("==========================================")

def print_bot(message):
    print(f"🤖 {bot_name}:", end=' ', flush=True)
    
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)

    print()

def show_help():
    print_bot("The things that I can do:")
    print()
    print_bot("Tell jokes")
    print()
    print_bot("Play games")
    print()
    print_bot("Or just talk!")
    print()
    print_bot("What do you want to do?")

#GREETING FUNCTION
def greet_user():
    greeting = random.choice(greetings)
    print_bot(greeting)
    print()
    user_name = input("Please enter your name: ")
    print()
    print_bot(f"{random.choice(greetings)}, {user_name}")
    return user_name

#RESPONSE FUNCTIONS
def tell_joke():
    joke = random.choice(jokes)
    return joke

def play_guess_game():
    print_bot("I think about a number between 1 - 20, lets see if you can guess it!")
    print()
    number = random.randint(1, 20)
    attempts = 0
    while True:
        user_guess = int(input("enter number: "))
        print()
        if user_guess > number:
            print_bot("too high!")
            print()
            attempts += 1
        elif user_guess < number:
            print_bot("low!")
            print()
            attempts += 1
        else:
            break
    return f"You did it! it take you {attempts} attempts"

def analyze_mood(message):
    happy_words = [
    "happy",
    "joy",
    "smile",
    "love",
    "excited",
    "cheerful",
    "grateful",
    "laugh",
    "hope",
    "peace",
    "nice"
    "lol"
    ]

    sad_words = [
    "sad",
    "lonely",
    "cry",
    "hurt",
    "tired",
    "upset",
    "broken",
    "hopeless",
    "angry",
    "lost"
    ]

    for word in happy_words:
        if word in message.lower():
            return "happy"
    
    for word in sad_words:
        if word in message.lower():
            return "sad"
        
    return "neutral"


# MAIN RESPONSE FUNCTION
def get_response(message, user_name):
    message_lower = message.lower()

    greetings_user  = ["hi", "hello", "welcome", "hey there", "nice to neet you"]
    for greeting in greetings_user:
        if greeting.lower() in message_lower:
           return f"{greeting}, {user_name}!"
        
    if "how are you" in message_lower:
        return "I'm great! How are you?"
    
    if "how do you feel" in message_lower:
        return "I'm feeling great, how do you feel?"
    
    response_howAreYou_good = ["good", "fine", "okay", "great", "alright"]
    for respone in response_howAreYou_good:
        if respone in message_lower:
            return "Great to hear!"
    response_howAreYou_bad = ["bad", "terrible", "awful", "horrible", "tired", "exhausted", "drained","upset", "stressed", "miserable"]
    for respone in response_howAreYou_bad:
        if respone in message_lower:
            return "I'm sorry for you..."
    
    if "talk" in message_lower:
        return "I'm ready when you are ready!"
    
    if "thank you" in message_lower or "thanks" in message_lower:
        return "You are welcome!"
    
    if "your name" in message_lower or "who are you" in message_lower:
        return bot_name
    
    if "joke" in message_lower or "funny" in message_lower:
        joke = tell_joke()
        return joke
    
    if "game" in message_lower or "play" in message_lower:
        return "game_menu"
    
    if "help" in message_lower or "commands" in message_lower:
        show_help()
        return "what else can I help with?"
    
    if "+" in message_lower or "-" in message_lower or "*" in message_lower:
        try:
            result  = eval(message_lower)
            return result
        except:
            return "Invalid math expression"
        
    if "color" in message_lower:
        return "I don't have a favorite color, but what's yours?"
    
    if "hobby" in message_lower:
        return "I don't have any hobbies, but what are yours?"
    
    if "music" in message_lower:
        return "I don't have a favorite music, but what is your favorite music and singer?"
    
    if "sport" in message_lower:
        return "I don't do any kind of sport, but what kinds of sports do you do?"
    
    if "food" in message_lower:
        return "I don't eat any kind of food, but what kind of food do you like to eat?"
    
    if "fact" in message_lower:
        return random.choice(facts)
    
    if "tip" in message_lower:
        return random.choice(tips)
    
    mood  = analyze_mood(message)
    if mood == "happy":
        return "That’s great to hear!"
    elif mood == "sad":
        return "Hope things get better soon."
    
    default_responses = [
    "That's interesting!",
    "Tell me more!",
    "I see...",
    "Cool!",
    "Got it!",
    "Hmm, okay.",
    "Alright!",
    "Nice!",
    "Sounds good!",
    f"Thanks for sharing, {user_name}!"
    ]

    random_respone = random.choice(default_responses)
    return random_respone

#MAIN CHAT LOOP
def chat():
    print_separator()
    print("BOTI CHAT")
    print_separator()
    print()

    #Greet user and ask from their name
    user_name = greet_user()
    print()

    #Show what bot can do
    show_help()
    print()

    while True:
        #Get user message
        user_massage = input(f"{user_name}: ").strip()
        print()

        #Skip if message is empty
        if not user_massage:
            continue
        
        #Check for goodbye
        if "bye" in user_massage.lower() or "goodbye" in user_massage.lower() or "quit" in user_massage.lower() or "exit" in user_massage.lower():
            goodbye = random.choice(goodbyes)
            print_bot(f"{goodbye}, {user_name}!")
            break
        
        #Get bot response
        response = get_response(user_massage, user_name)

        #Check if response is "game_menu"
        if response == "game_menu":
            print_bot("What would you like to play?")
            print()
            print_bot("1. Number Guessing Game")
            print()
            print_bot("2. Never mind")
            print()

            user_choice = input(f"{user_name}: ").strip()
            print()

            if user_choice == "1":
                result = play_guess_game()
                print_bot(result)
                print()
        else:
            print_bot(response)
            print()

    print()
    print_bot("Thanks for chatting!")

#RUN THE CHATBOT
if __name__ == "__main__":
    chat()
        




        


    







