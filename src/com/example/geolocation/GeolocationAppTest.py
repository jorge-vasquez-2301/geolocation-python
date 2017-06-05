import unittest

from com.example.geolocation.Classroom import Classroom
from com.example.geolocation.GeolocationApp import student_clusters_in_classes
from com.example.geolocation.Student import Student


class GeolocationAppTest(unittest.TestCase):
    def setUp(self):
        self.classrooms = [
            Classroom("Principles of computational geo-location analysis", (34.069140, -118.442689)),
            Classroom("Sedimentary Petrology", (34.069585, -118.441878)),
            Classroom("Introductory Psychobiology", (34.069742, -118.441312)),
            Classroom("Art of Listening", (34.070223, -118.440193)),
            Classroom("Art Hitory", (34.071528, -118.441211))
        ]

    def test_students_in_cluster(self):
        students = [
            Student("John Wilson", (34.069149, -118.442639)),
            Student("Jane Graham", (34.069149, -118.442639)),
            Student("Pam Bam", (34.069149, -118.442639))
        ]
        self.assertCountEqual(students, student_clusters_in_classes(students, self.classrooms))

    def test_one_student_not_in_cluster(self):
        students = [
            Student("John Wilson", (34.069149, -118.442639)),
            Student("Jane Graham", (34.069149, -118.442639)),
            Student("Pam Bam", (34.071513, -118.441181))
        ]
        self.assertCountEqual(students[:2], student_clusters_in_classes(students, self.classrooms))


if __name__ == '__main__':
    unittest.main()
