def IsFloatOrInt(number):
    return isinstance(number, (float,int))

class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def conjugate(self):
        return self.real - self.imaginary

    def modulus(self):
        pass

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        if IsFloatOrInt(other):
            return Complex(self.real * other, self.imaginary * - other)
        else:
            return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __neg__(self):
        return Complex(-self.real, - self.imaginary)
