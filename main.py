a = str(input("Input text:"))
text = a.split(" ")
dict_text = {}
for word in text:
    word = word.lower()
    if word in dict_text:
        dict_text[word] += 1
    else:
        dict_text[word] = 1

for key in dict_text:
    print(key, dict_text[key])
