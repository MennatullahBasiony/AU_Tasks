import math

class ComplexNumbers:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "{:.2f} + {:.2f}i".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return ComplexNumbers(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return ComplexNumbers(x, y)
    
    def __mul__(self, other):
        res = complex(self.x, self.y) * complex(other.x, other.y)
        x = res.real
        y = res.imag
        return ComplexNumbers(x, y)
     
    def __truediv__(self, other):

        res = complex(self.x, self.y) / complex(other.x, other.y)
        x = res.real
        y = res.imag
        return ComplexNumbers(x, y)

    def mod(self):
        return "{:.2f}".format(math.sqrt(pow(self.x, 2) + pow(self.y, 2)))

c = input("C = ")
d = input("D = ")

c = c.split(" ")
c1 = float(c[0])
c2 = c[2]
if(c[1] != "-"): 
    c2 = float(c2[:-1])
else:
    c2 = float(c2[:-1]) * -1

d = d.split(" ")
d1 = float(d[0])
d2 = d[2]
if(d[1] != "-"): 
    d2 = float(d2[:-1])
else:
    d2 = float(d2[:-1]) * -1

C = ComplexNumbers(c1, c2)
D = ComplexNumbers(d1, d2)

print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(C.mod())
print(D.mod())



