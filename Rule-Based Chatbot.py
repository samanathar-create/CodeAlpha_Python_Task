# Basic Rule-Based Chatbot

def get_response(user_input):
    """Generate a response based on user input."""

    user_input = user_input.lower().strip()

    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "hey": "Hey! How are you doing?",
        "how are you": "I'm fine, thanks! How about you?",
        "what is your name": "I'm a simple Python chatbot.",
        "who are you": "I'm a rule-based chatbot created using Python.",
        "help": "Sure! You can say hello, ask how I am, or say bye.",
        "bye": "Goodbye! Have a great day!"
    }

    return responses.get(
        user_input,
        "Sorry, I don't understand that. Please try again."
    )


def main():
    """Start and run the chatbot."""

    print("=" * 40)
    print("          PYTHON CHATBOT")
    print("=" * 40)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break


if __name__ == "__main__":
    main()




    