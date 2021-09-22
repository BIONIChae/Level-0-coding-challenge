def sides_of_triangle(x, y, z):
    semi_perimeter = (x + y + z) / 2
    s = semi_perimeter
    area = (s * (s-x) * (s-y) * (s-z)) ** 0.5
    print(area)
sides_of_triangle()
