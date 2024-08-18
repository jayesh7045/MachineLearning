class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
v = Vector(1, 2)
v1 = Vector(3, 4)

print(v + v1)      # Vector(4, 6)
print(v - v1)      # Vector(-2, -2)
print(v * 3)       # Vector(3, 6)
print(v == v1)     # False
print(-v)          # Vector(-1, -2)
print(str(v))      # Vector(1, 2)

