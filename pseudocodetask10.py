def common(string1, string2):
    common_values = list(set(string1) & set(string2))
    print("Common letters: ")
    for items in common_values:
        print(items)
common()
