import math

# [...]

class Vector(object):
    def __init__(self, length, direction):
        self.length = length
        self.direction = direction
        self.x_component = math.sin(math.radians(direction)) * length
        self.y_component = math.cos(math.radians(direction)) * length
        self.slope = self.y_component / self.x_component


    def __str__(self):
        return 'Length: {}, Direction: {}'.format(self.length, self.direction)

        
    def __add__(self, other):
        new_vector_length = math.sqrt((self.x_component + other.x_component) ** 2 + (self.y_component + other.y_component) ** 2)
        new_vector_direction = math.degrees(math.atan((self.x_component + other.x_component) / (self.y_component + other.y_component)))
        return Vector(new_vector_length, new_vector_direction)


a = Vector(3, 60)
b = Vector(3, 60)
print(a + b)
