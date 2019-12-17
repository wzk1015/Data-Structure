in_words=input().split()
out_words=[]
for word in in_words:
    if word in ["and","the","of","for"]:
        continue
    out_words.append(word[0].upper())
print("".join(out_words))