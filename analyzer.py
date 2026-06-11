with open("sample.txt") as f:
    text = f.read()

print(text)

text_list = text.lower().split()
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