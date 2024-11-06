from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import numpy as np

# Example data (user queries and their corresponding intent labels)
queries = ["What are the campus hours?", "How can I contact the admissions office?", "Where is the library?", "What subjects am I enrolled in?"]
labels = ["hours", "contact", "location", "schedule"]

# Create a pipeline with CountVectorizer and DecisionTreeClassifier
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),          # Convert text to numerical data
    ('classifier', DecisionTreeClassifier())     # Use a decision tree as the classifier
])

# Train the model
pipeline.fit(queries, labels)

# Function to get a response based on the intent
def get_response_decision_tree(user_input):
    intent = pipeline.predict([user_input])[0]
    responses = {
        "hours": "Our campus is open from 8 AM to 5 PM, Monday through Friday.",
        "contact": "You can reach us at contact@university.com or call (123) 456-7890.",
        "location": "The library is located at the center of the campus.",
        "schedule": "You can view your enrolled subjects on the university portal."
    }
    return responses.get(intent, "I'm sorry, I don't have information on that topic.")

chatbot_is_running = True
while chatbot_is_running:
# Example usage
    user_input = input("You: ")
    if user_input == 'bye':
        break
    print("Bot:", get_response_decision_tree(user_input))
