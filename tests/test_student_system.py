import unittest
from src.student import Student
from src.student_system import StudentSystem

class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        # Tworzymy system i kilku studentów na start
        self.system = StudentSystem()
        self.s1 = Student("Jan", "Kowalski", "1A", "Physics", 2023)
        self.s2 = Student("Anna", "Nowak", "1A", "Math", 2023)
        self.s3 = Student("Adam", "Malinowski", "2B", "Math", 2024)
        self.s4 = Student("Ewa", "Dąbrowska", "1A", "Physics", 2023)

        self.s1.add_grade("math", 4.0)
        self.s1.add_grade("physics", 5.0)
        self.s2.add_grade("math", 3.0)
        self.s3.add_grade("math", 2.0)
        self.s4.add_grade("physics", 4.0)
        self.s4.add_grade("math", 5.0)

        for student in [self.s1, self.s2, self.s3, self.s4]:
            self.system.add_student(student)

    def test_add_and_remove_student(self):
        new_student = Student("Paweł", "Lis", "3A", "Chemistry", 2024)
        self.system.add_student(new_student)
        self.assertEqual(self.system.get_student_count(), 5)
        removed = self.system.remove_student("Paweł", "Lis")
        self.assertTrue(removed)
        self.assertEqual(self.system.get_student_count(), 4)

    def test_remove_student_not_found(self):
        result = self.system.remove_student("Nie", "MaTakiego")
        self.assertFalse(result)
        self.assertEqual(self.system.get_student_count(), 4)

    def test_remove_students_from_year(self):
        removed_count = self.system.remove_students_from_year(2023)
        self.assertEqual(removed_count, 3)
        self.assertEqual(self.system.get_student_count(), 1)

    def test_find_student(self):
        found = self.system.find_student("Adam", "Malinowski")
        self.assertIsNotNone(found)
        self.assertEqual(found.class_grade, "2B")
        not_found = self.system.find_student("Xxx", "Yyy")
        self.assertIsNone(not_found)

    def test_show_all_students(self):
        output = self.system.show_all_students()
        self.assertIn("Jan Kowalski 1A", output)
        self.assertIn("Ewa Dąbrowska 1A", output)
        self.assertEqual(len(output.splitlines()), 4)

    def test_get_student_count(self):
        self.assertEqual(self.system.get_student_count(), 4)

    def test_get_class_average(self):
        # W klasie 1A: Jan (4, 5), Anna (3), Ewa (4, 5)
        avg = self.system.get_class_average("1A")
        # Suma: 4+5+3+4+5=21, liczba: 5
        self.assertAlmostEqual(avg, 4.2, places=2)

    def test_get_class_average_no_grades(self):
        # Brak studentów z ocenami w klasie 3C
        with self.assertRaises(ValueError):
            self.system.get_class_average("3C")

    def test_get_school_average(self):
        # Suma: 4+5+3+2+4+5 = 23, liczba: 6
        avg = self.system.get_school_average()
        self.assertAlmostEqual(avg, 23 / 6, places=2)

    def test_get_school_average_no_grades(self):
        sys = StudentSystem()
        s = Student("X", "Y", "1A", "Physics", 2023)
        sys.add_student(s)
        with self.assertRaises(ValueError):
            sys.get_school_average()

    def test_get_students_from_major(self):
        physics_students = self.system.get_students_from_major("Physics")
        self.assertEqual(len(physics_students), 2)
        math_students = self.system.get_students_from_major("math")
        self.assertEqual(len(math_students), 2)

    def test_sort_students_by_class_grade(self):
        sorted_students = self.system.sort_students_by_class_grade()
        classes = [s.class_grade for s in sorted_students]
        self.assertEqual(classes, ["1A", "1A", "1A", "2B"])

    def test_sort_students_by_major(self):
        sorted_students = self.system.sort_students_by_major()
        majors = [s.major for s in sorted_students]
        self.assertEqual(sorted(majors), majors)  # Alfabet

    def test_sort_class_by_avg_grade(self):
        sorted_students = self.system.sort_class_by_avg_grade()
        # Najlepszy średnia na górze
        avgs = []
        for s in sorted_students:
            try:
                avgs.append(s.average_grade())
            except ValueError:
                avgs.append(None)
        # Sprawdź, że jest malejąco lub None na końcu
        non_null_avgs = [a for a in avgs if a is not None]
        self.assertEqual(non_null_avgs, sorted(non_null_avgs, reverse=True))

    def test_get_students_by_class(self):
        students_1A = self.system.get_students_by_class("1A")
        self.assertEqual(len(students_1A), 3)
        students_2b = self.system.get_students_by_class("2B")
        self.assertEqual(len(students_2b), 1)

    def test_sort_students_by_avg_in_class(self):
        sorted_1A = self.system.sort_students_by_avg_in_class("1A")
        avgs = []
        for s in sorted_1A:
            try:
                avgs.append(s.average_grade())
            except ValueError:
                avgs.append(None)
        non_null_avgs = [a for a in avgs if a is not None]
        self.assertEqual(non_null_avgs, sorted(non_null_avgs, reverse=True))

if __name__ == "__main__":
    unittest.main()
