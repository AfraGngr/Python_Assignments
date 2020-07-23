sentence = input("Please enter a statement: ").lower()

letters = sorted(set(sentence))

ltr_count = {}

for i in letters:
    
    ltr_count[i] = sentence.count(i)
    
print(ltr_count)