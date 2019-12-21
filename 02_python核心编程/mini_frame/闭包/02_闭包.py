def line(k, b):
    def create_line(x):
        print(k*b + x)
    return create_line

line = line(1,2)
line(0)
line(1)
line(2)