a = int(input())
b = int(input())
c = int(input())
def maximum(a, b, c):
    if (a > b) and (a > c):
        print(a)
    elif (b > a) and (b > c):
        print(b)
    else:
        print(c)
print("Maximum of three:")
print(maximum(a, b, c))

# Bonus question

def maximum(*array):  
  max_value = array[0]
  for argument in array:
    if argument > max_value:
            max_value = argument 

  print("Maximum value:", max_value)
maximum(1, 22, 3, 2)
