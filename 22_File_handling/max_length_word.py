with open('document.txt', 'r') as f:
    words = f.read().split()
    
max_len = len(max(words, key=len))
max_length_words = [w for w in words if len(w) == max_len]

print(max_length_words)