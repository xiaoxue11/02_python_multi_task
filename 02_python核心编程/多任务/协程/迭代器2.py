class FibIterator():

    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.n:
            ret = self.a
            self.a, self.b = self.b, self.a+self.b
            self.current +=1
            return ret
        else:
            raise StopIteration


fib = FibIterator(10)
for num in fib:
    print(num)


    