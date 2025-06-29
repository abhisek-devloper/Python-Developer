# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# Take user input
comment = input("Enter your comment: ").lower()  # convert to lowercase for case-insensitive check

# List of spam keywords
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# Check if any spam keyword is present in the comment
is_spam = any(keyword in comment for keyword in spam_keywords)

# Output result
if is_spam:
    print("⚠️ This is a SPAM comment.")
else:
    print("✅ This is NOT a spam comment.")
