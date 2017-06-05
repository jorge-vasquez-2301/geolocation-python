from src.com.example.geolocation.Classroom import Corner


def student_clusters_in_classes(students, classrooms):
    """Returns students that are in classes with clusters"""
    return list(
        filter(
            lambda student: is_student_in_classes_with_cluster(student, classrooms_with_clusters(classrooms, students)),
            students
        )
    )


def is_student_in_classes_with_cluster(student, classrooms_with_clusters):
    """Returns true if a student is in classes with clusters"""
    return len(list(filter(lambda classroom: is_student_in_class(student, classroom), classrooms_with_clusters))) > 0


def classrooms_with_clusters(classrooms, students):
    """Returns classrooms with clusters of students"""
    return list(filter(lambda classroom: classroom_students_count(classroom, students) > 1, classrooms))


def classroom_students_count(classroom, students):
    """Returns the count of students in a classroom"""
    return len(list(filter(lambda student: is_student_in_class(student, classroom), students)))


def is_student_in_class(student, classroom):
    """Returns true if a student is in a classroom"""
    classroom_top_left_coordinates = classroom.get_corner_coordinates(Corner.TOP_LEFT)
    classroom_bottom_right_coordinates = classroom.get_corner_coordinates(Corner.BOTTOM_RIGHT)
    return (student.coordinates[0] < classroom_top_left_coordinates[0] and
            student.coordinates[1] > classroom_top_left_coordinates[1] and
            student.coordinates[0] > classroom_bottom_right_coordinates[0] and
            student.coordinates[1] < classroom_bottom_right_coordinates[1])
