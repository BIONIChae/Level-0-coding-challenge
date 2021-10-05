def convert(cels, fahr):
    for c in range(cels):
        fahrenheit = (9/5 * cels) + 32
    for f in range(fahr):
        celsius = (fahr - 32) * 5/9
        return fahrenheit, celsius
print(convert(35, 68))

