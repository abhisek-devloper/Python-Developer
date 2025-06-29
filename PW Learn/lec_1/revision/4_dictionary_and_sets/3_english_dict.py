# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!


# Hindi to English Dictionary
hindi_to_english = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "शुभ प्रभात": "Good Morning",
    "शुभ रात्रि": "Good Night",
    "आप कैसे हैं?": "How are you?",
    "मुझे माफ करें": "Excuse me"}

# Function to look up Hindi words in the dictionary
def lookup_hindi_word(word):
    return hindi_to_english.get(word, "Word not found in the dictionary.")


# Main program loop
while True:
    print("Welcome to the Hindi-English Dictionary!")
    print("Enter 'exit' to quit the program.")
    hindi_word = input("Enter a Hindi word to look up its English translation: ")
    
    if hindi_word.lower() == 'exit':
        print("Thank you for using the dictionary. Goodbye!")
        break
    
    english_translation = lookup_hindi_word(hindi_word)
    print(f"The English translation of '{hindi_word}' is: {english_translation}")