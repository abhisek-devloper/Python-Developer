# 7. Write a program to find out whether a given post is talking about “code” or not

# Input post content
post = input("Enter the post: ")

# Check for 'code' (case-insensitive)
if "code" in post.lower():
    print("📢 The post is talking about Harry.")
else:
    print("❌ The post does not mention Harry.")
