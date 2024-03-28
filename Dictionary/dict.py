import json
import difflib
import sys

# Step 1: Download JSON data (assuming it's saved as "dictionary.json")
# Step 2: Load JSON data into a Python dictionary
with open("data.json", "r") as file:
    dictionary_data = json.load(file)

# Step 3: Define a function to get definition of a word
def get_definition(word):
    # Step 5: Handle input cases (convert to lowercase)
    word = word.lower()
    
    if word in dictionary_data:
        return dictionary_data[word]
    else:
        # Step 6: Spell-check and suggest similar words
        similar_words = difflib.get_close_matches(word, dictionary_data.keys())
        if similar_words:
            suggestion = similar_words[0]  # Taking the closest match
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found in dictionary."

# Check if command-line argument is provided
if len(sys.argv) > 1:
    word = sys.argv[1]
    definition = get_definition(word)
    print(definition)
else:
    print("Please provide a word as a command-line argument.")
