def maximum(a, b, c):
    if (a > b) and (a > c):
        print(a)
    elif (b > a) and (b > c):
        print(b)
    else:
        print(c)
print("Maximum of three:")
maximum()

def maximum(*array):
    max_value = array[0]
    for argument in array:
      if argument > max_value:
          max_value = argument

    print("Maximum value:", max_value)
maximum() 
