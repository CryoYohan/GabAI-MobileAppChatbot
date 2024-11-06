from transformers import pipeline

# Load the fine-tuned model and tokenizer
qa_model = pipeline("text-classification", model="./fine_tuned_GabAI_model", tokenizer="./fine_tuned_GabAI_tokenizer")

# Ask a question
question = "What courses are available at the University of Cebu?"
response = qa_model(question)

print("GabAI's answer:", response)
