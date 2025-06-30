import unittest
from unittest.mock import patch
from src.student_system import StudentSystem
from menu import add_student_to_system

class TestMenuAddStudent(unittest.TestCase):
    @patch("builtins.input", side_effect=["Jan", "Kowalski", "1A", "Physics", "2024"])
    def test_add_student_to_system(self, mock_input):
        system = StudentSystem()
        add_student_to_system(system)
        # Sprawdzamy czy student został dodany
        self.assertEqual(system.get_student_count(), 1)
        s = system.students[0]
        self.assertEqual(s.name, "Jan")
        self.assertEqual(s.last_name, "Kowalski")
        self.assertEqual(s.class_grade, "1A")
        self.assertEqual(s.major, "Physics")
        self.assertEqual(s.year, 2024)

class TestMenuRemoveStudent(unittest.TestCase):
    @patch("builtins.input", side_effect=["Jan", "Kowalski", "2024"])
    def test_remove_student_from_system(self, mock_input):
        system = StudentSystem()
        student = Student("Jan", "Kowalski", "1A", "Physics", 2024)
        system.add_student(student)
        remove_student_from_system(system)
        self.assertEqual(system.get_student_count(), 0)

if __name__ == "__main__":
    unittest.main()
