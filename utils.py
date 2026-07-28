from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts)  # Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
