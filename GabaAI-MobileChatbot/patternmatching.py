import re
from response_dataset import responses


# Function to match input to pattern and return response
def get_response(user_input):
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that question. Could you try rephrasing?"


# Example usage
chatbot_running = True
while chatbot_running:
    user_input = input("You: ")
    if user_input == 'bye':
        break
    print("Bot:", get_response(user_input))
