import pandas as pd
from transformers import DistilBertTokenizerFast
from datasets import Dataset

# Load your CSV file
dataset = pd.read_csv('university_data.csv')
# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(dataset)

tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')


def preprocess_data(examples):
    questions = examples['question']

    # Filter out None values and ensure consistent length
    questions = [q for q in questions if q is not None]

    if len(questions) == 0:
        return {
            'input_ids': [],
            'attention_mask': [],
        }

    # Tokenize
    tokenized = tokenizer(
        questions,
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors='pt'
    )

    # Print lengths for debugging
    print(f"Processed {len(questions)} questions.")
    print(f"Input IDs length: {len(tokenized['input_ids'])}")
    print(f"Attention Mask length: {len(tokenized['attention_mask'])}")

    # Return the tokenized output
    return {
        'input_ids': tokenized['input_ids'].tolist(),  # Convert to list
        'attention_mask': tokenized['attention_mask'].tolist(),  # Convert to list
    }


# Print the dataset structure for debugging
print(dataset)

# Map the preprocessing function
tokenized_data = dataset.map(preprocess_data, batched=True)

# Print output data for verification
print(tokenized_data)
