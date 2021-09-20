string1 = str(input())
string2 = str(input())
x = list(set(string1) & set(string2))
print("Common letters:")
for item in x:
    print(item)
