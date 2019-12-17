name = input()
name_out=""

mark=0
for i in range(len(name)):
    if name[i].isupper():
        name_out = name_out + str(name[mark:i]).lower() + "_"
        mark=i
name_out = name_out + str(name[mark:]).lower()
name_out = name_out[1:]        

print(name_out)