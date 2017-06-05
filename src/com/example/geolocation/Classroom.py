from enum import Enum

from com.example.geolocation.ClassroomCoordinatesCalculator import ClassroomCoordinatesCalculator
from src.com.example.geolocation.Entity import Entity


class Classroom(Entity):
    SIZE = 20

    def __init__(self, name, coordinates):
        """Creates a new instance of Classroom"""
        super().__init__(name, coordinates)
        self.cornerCoordinatesMap = {}
        self.classroomCoordinatesCalculator = ClassroomCoordinatesCalculator(coordinates)
        self.cornerCoordinatesMap[Corner.TOP_LEFT.name] = self.classroomCoordinatesCalculator.get_corner_coordinates(Corner.TOP_LEFT)
        self.cornerCoordinatesMap[Corner.BOTTOM_RIGHT.name] = self.classroomCoordinatesCalculator.get_corner_coordinates(Corner.BOTTOM_RIGHT)

    def get_corner_coordinates(self, corner):
        return self.cornerCoordinatesMap[corner.name]

class Corner(Enum):
    TOP_LEFT = 315
    BOTTOM_RIGHT = 135
