from math import radians, sqrt, sin, cos, asin, atan2, degrees

class ClassroomCoordinatesCalculator:
    EARTHS_RADIUS_IN_METERS = 6371000
    SIZE = 20

    def __init__(self, classroom_coordinates):
        """Creates a new instance of ClassroomCoordinatesCalculator"""
        self.centerCoordinatesInRadians = (radians(classroom_coordinates[0]), radians(classroom_coordinates[1]))
        self.distanceFromCenterToCorner = sqrt(2 * (ClassroomCoordinatesCalculator.SIZE / 2) * (ClassroomCoordinatesCalculator.SIZE / 2))

    def get_corner_coordinates(self, corner):
        """Returns the coordinates for a given corner"""
        bearingInRadians = radians(corner.value)
        sinOfLatitude = sin(self.centerCoordinatesInRadians[0])
        cosOfLatitude = cos(self.centerCoordinatesInRadians[0])
        sinOfDistanceEarthRadiusRatio = sin(self.distanceFromCenterToCorner/ClassroomCoordinatesCalculator.EARTHS_RADIUS_IN_METERS)
        cosOfDistanceEarthRadiusRatio = cos(self.distanceFromCenterToCorner/ClassroomCoordinatesCalculator.EARTHS_RADIUS_IN_METERS)
        sinOfBearing = sin(bearingInRadians)
        cosOfBearing = cos(bearingInRadians)
        latitudeInRadians = asin(sinOfLatitude * cosOfDistanceEarthRadiusRatio +
                                 cosOfLatitude * sinOfDistanceEarthRadiusRatio * cosOfBearing)
        longitudeInRadians = self.centerCoordinatesInRadians[1] +\
                             atan2(sinOfBearing * sinOfDistanceEarthRadiusRatio * cosOfLatitude,
                                   cosOfDistanceEarthRadiusRatio - sinOfLatitude * sin(latitudeInRadians))

        return degrees(latitudeInRadians), degrees(longitudeInRadians)
