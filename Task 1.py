def chatbot():
    responses = {
        'hello': 'Hi there! How can I help you?',
        'hi': 'Hey! Welcome to DecodeLabs.',
        'how are you': 'I am functioning at 100% efficiency!',
        'what is ai': 'AI is the simulation of human intelligence by machines.',
        'bye': 'Goodbye! Have a great day.',
        'help': 'I can answer basic questions. Try: hello, how are you, what is ai.',
    }

    print("Chatbot is online. Type 'exit' to quit.\n")

    while True:
        raw_input_text = input('You: ')
        clean_input = raw_input_text.lower().strip()

        if clean_input == 'exit':
            print('Bot: Shutting down. Goodbye!')
            break

        reply = responses.get(clean_input, "I do not understand that yet.")
        print(f'Bot: {reply}')

chatbot()