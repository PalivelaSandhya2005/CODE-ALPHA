def chatbot():
    print("Welcome to ChatBot! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'hello':
            print("Bot: Hi!")
        elif user_input == 'how are you':
            print("Bot: I'm fine, thanks!")
        elif user_input == 'bye':
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()
