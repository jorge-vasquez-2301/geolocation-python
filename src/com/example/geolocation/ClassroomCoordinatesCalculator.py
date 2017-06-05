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
        bearing_in_radians = radians(corner.value)
        sin_of_latitude = sin(self.centerCoordinatesInRadians[0])
        cos_of_latitude = cos(self.centerCoordinatesInRadians[0])
        sin_of_distance_earth_radius_ratio = sin(self.distanceFromCenterToCorner/ClassroomCoordinatesCalculator.EARTHS_RADIUS_IN_METERS)
        cos_of_distance_earth_radius_ratio = cos(self.distanceFromCenterToCorner/ClassroomCoordinatesCalculator.EARTHS_RADIUS_IN_METERS)
        sin_of_bearing = sin(bearing_in_radians)
        cos_of_bearing = cos(bearing_in_radians)
        latitude_in_radians = asin(sin_of_latitude * cos_of_distance_earth_radius_ratio +
                                   cos_of_latitude * sin_of_distance_earth_radius_ratio * cos_of_bearing)
        longitude_in_radians = self.centerCoordinatesInRadians[1] +\
                             atan2(sin_of_bearing * sin_of_distance_earth_radius_ratio * cos_of_latitude,
                                   cos_of_distance_earth_radius_ratio - sin_of_latitude * sin(latitude_in_radians))

        return degrees(latitude_in_radians), degrees(longitude_in_radians)
