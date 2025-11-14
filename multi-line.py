def word_count(text):
    text = text.lower()
    words = text.split()
    count = {}

    for word in words:
        word = word.strip(",.!?;-()\"'") 
        if word:
            count[word] = count.get(word, 0) + 1

    return count
                        

print(word_count("hello prince"))

