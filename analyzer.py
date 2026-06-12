import string 
stopwords = {"the", "a", "an", "on", "in", "and", "are", "is", "to", "of"}
with open("sample.txt") as f:
    text = f.read()

print(text)
text=text.translate(str.maketrans("","",string.punctuation))
text_list = text.lower().split()
text_list = [w for w in text_list if w not in stopwords]
print(text_list)
text_dict= {}
for word in text_list:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1
print(text_dict)
sorted_items = sorted(text_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)
print(len(text_list))
print(len(text_dict))
for word, count in sorted_items[:5]:
    print(f"{word}: {count}")
