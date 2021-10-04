def maximum(*array):
    max_value = array[0]
    for argument in array:
      if argument > max_value:
          max_value = argument

    print("Maximum value:", max_value)
maximum(1, 22, 3, 2) 
