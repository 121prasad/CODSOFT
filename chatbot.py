import re

def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()

    # Define patterns for matching specific user queries
    greeting_patterns = ['hello', 'hi', 'hey', 'greetings']
    weather_patterns = ['weather', 'how is the weather', 'what\'s the weather like']
    day_of_week_patterns = ['day of the week', 'what day is it today']
    chatbot_info_patterns = ['who are you', 'what can you do', 'tell me about yourself']

    # Check if the user input matches any greeting pattern
    if any(pattern in user_input_lower for pattern in greeting_patterns):
        return "Hello! How can I help you today?"

    # Check if the user input matches any weather-related pattern
    elif any(pattern in user_input_lower for pattern in weather_patterns):
        return "I'm sorry, I don't have information about the weather right now."

    # Check if the user input is asking about the day of the week
    elif any(pattern in user_input_lower for pattern in day_of_week_patterns):
        import datetime
        current_day = datetime.datetime.now().strftime("%A")
        return f"Today is {current_day}."

    # Check if the user input is asking about the chatbot
    elif any(pattern in user_input_lower for pattern in chatbot_info_patterns):
        return "I am a simple rule-based chatbot. I can help you with basic queries."

    # If no specific pattern matches, provide a generic response
    else:
        return "I'm not sure how to respond to that. Can you please provide more information?"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
