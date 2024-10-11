text = "Hello, World!"

# Searching in the entire string
print(text.find("o"))  # Output: 4

# Searching from index 0 to 5 (exclusive)
print(text.find("o", 0, 5))  # Output: 4

# Searching from index 0 to 4 (exclusive)
print(text.find("o", 0, 4))  # Output: -1