import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        # Każdy test zaczyna z nowym studentem
        self.student = Student("Jan", "Kowalski", "1B", "Physics", 2024)

    # Podstawowe testy inicjalizacji
    def test_initial_data(self):
        self.assertEqual(self.student.name, "Jan")
        self.assertEqual(self.student.last_name, "Kowalski")
        self.assertEqual(self.student.class_grade, "1B")
        self.assertEqual(self.student.major, "Physics")
        self.assertEqual(self.student.year, 2024)
        self.assertEqual(self.student.grades, {})

    # Test dodawania oceny i jej istnienia
    def test_add_grade(self):
        self.student.add_grade("math", 4.5)
        self.assertIn("math", self.student.grades)
        self.assertEqual(self.student.grades["math"], [4.5])

    # Test zakresu oceny (za niska i za wysoka)
    def test_grade_out_of_range(self):
        with self.assertRaises(ValueError):
            self.student.add_grade("math", 0.5)
        with self.assertRaises(ValueError):
            self.student.add_grade("math", 6.5)

    # Test obliczania średniej z przedmiotu
    def test_average_subject_grade(self):
        self.student.add_grade("math", 4.0)
        self.student.add_grade("math", 5.0)
        avg = self.student.average_subject_grade("math")
        self.assertAlmostEqual(avg, 4.5, places=2)

    # Test średniej bez ocen w danym przedmiocie
    def test_average_subject_grade_no_grades(self):
        with self.assertRaises(ValueError):
            self.student.average_subject_grade("biology")

    # Test usuwania ostatniej oceny
    def test_remove_last_grade(self):
        self.student.add_grade("math", 3.0)
        self.student.add_grade("math", 4.0)
        last = self.student.remove_last_grade("math")
        self.assertEqual(last, 4.0)
        self.assertEqual(self.student.grades["math"], [3.0])

    # Usuwanie, gdy nie ma ocen
    def test_remove_last_grade_error(self):
        with self.assertRaises(ValueError):
            self.student.remove_last_grade("math")

    # Test pobierania ocen z przedmiotu
    def test_get_subject_grades(self):
        self.student.add_grade("physics", 5.0)
        self.student.add_grade("physics", 4.5)
        grades = self.student.get_subject_grades("physics")
        self.assertEqual(grades, [5.0, 4.5])

    # Próba pobrania ocen z pustego przedmiotu
    def test_get_subject_grades_error(self):
        with self.assertRaises(ValueError):
            self.student.get_subject_grades("history")

    # Test średniej ze wszystkich ocen
    def test_average_grade(self):
        self.student.add_grade("math", 3.0)
        self.student.add_grade("physics", 5.0)
        avg = self.student.average_grade()
        self.assertAlmostEqual(avg, 4.0)

    # Brak ocen do średniej globalnej
    def test_average_grade_no_grades(self):
        with self.assertRaises(ValueError):
            self.student.average_grade()

    # Usuwanie przedmiotu
    def test_delete_subject(self):
        self.student.add_grade("chemistry", 4.5)
        result = self.student.delete_subject("chemistry")
        self.assertTrue(result)
        self.assertNotIn("chemistry", self.student.grades)

    # Usuwanie nieistniejącego przedmiotu
    def test_delete_subject_error(self):
        with self.assertRaises(ValueError):
            self.student.delete_subject("biology")

    # Usuwanie wszystkich ocen
    def test_delete_all_grades(self):
        self.student.add_grade("math", 3.0)
        self.student.add_grade("physics", 5.0)
        result = self.student.delete_all_grades()
        self.assertTrue(result)
        self.assertEqual(self.student.grades, {})

    # Zmiana imienia i nazwiska
    def test_change_name(self):
        changed = self.student.change_name("Adam", "Nowak")
        self.assertTrue(changed)
        self.assertEqual(self.student.name, "Adam")
        self.assertEqual(self.student.last_name, "Nowak")
        not_changed = self.student.change_name("Adam", "Nowak")
        self.assertFalse(not_changed)

    # Zmiana klasy
    def test_change_class_grade(self):
        changed = self.student.change_class_grade("2C")
        self.assertTrue(changed)
        self.assertEqual(self.student.class_grade, "2C")
        not_changed = self.student.change_class_grade("2C")
        self.assertFalse(not_changed)

    # Zmiana profilu
    def test_change_major(self):
        changed = self.student.change_major("Mathematics")
        self.assertTrue(changed)
        self.assertEqual(self.student.major, "Mathematics")
        not_changed = self.student.change_major("Mathematics")
        self.assertFalse(not_changed)

    # Test podsumowania ucznia
    def test_get_student_summary(self):
        self.student.add_grade("math", 3.0)
        self.student.add_grade("math", 5.0)
        self.student.add_grade("physics", 4.0)
        summary = self.student.get_student_summary()
        self.assertEqual(summary["name"], "Jan Kowalski")
        self.assertEqual(summary["class"], "1B")
        self.assertEqual(summary["major"], "Physics")
        self.assertEqual(summary["year"], 2024)
        self.assertEqual(summary["subjects"], 2)
        self.assertEqual(summary["total_grades"], 3)
        self.assertAlmostEqual(summary["average"], 4.0)

    # Test podsumowania, gdy brak ocen
    def test_get_student_summary_no_grades(self):
        summary = self.student.get_student_summary()
        self.assertEqual(summary["average"], None)
        self.assertEqual(summary["subjects"], 0)
        self.assertEqual(summary["total_grades"], 0)

if __name__ == "__main__":
    unittest.main()
