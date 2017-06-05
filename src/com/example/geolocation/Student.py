from src.com.example.geolocation.Entity import Entity


class Student(Entity):
    def __init__(self, name, coordinates):
        super().__init__(name, coordinates)
