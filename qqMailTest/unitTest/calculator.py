class Count:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)


    def add(self):
        return self.a + self.b


    def is_prime(self):
        if self.a <= 1:
            return False
        for i in range(2,self.a):
            if self.a % i == 0:
                return False
        return True
