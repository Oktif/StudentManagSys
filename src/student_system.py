from src.student import Student

class StudentSystem:
    """
    System to manage a collection of Student objects. Provides methods to add, remove, search,
    sort, and retrieve statistical information about students.
    """

    def __init__(self):
        """
        Initializes the StudentSystem with an empty student list.
        """
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        """
        Adds a student to the system.

        Args:
            student (Student): The student to be added.
        """
        self.students.append(student)

    def remove_student(self, name: str, last_name: str, year: int) -> bool:
        """
        Removes a student with the given name and last name from the system.

        Args:
            name (str): First name of the student.
            last_name (str): Last name of the student.

        Returns:
            bool: True if the student was removed, False if not found.
        """
        for student in self.students:
            if (student.name == name and student.last_name == last_name and student.year == year):
                self.students.remove(student)
                return True
        return False

    def remove_students_from_year(self, year: int) -> int:
        """
        Removes all students from the given year.

        Args:
            year (int): The year to remove students from.

        Returns:
            int: The number of students removed.
        """
        original_count = len(self.students)
        self.students = [student for student in self.students if student.year != year]
        removed_count = original_count - len(self.students)
        return removed_count

    def find_student(self, name: str, last_name: str, year: int) -> Student | None:
        """
        Finds and returns a student by their first and last name.

        Args:
            name (str): First name of the student.
            last_name (str): Last name of the student.

        Returns:
            Student | None: The found student, or None if not found.
        """
        for student in self.students:
            if (student.name == name and student.last_name == last_name and student.year == year):
                return student
        return None

    def show_all_students(self) -> str:
        """
        Returns a formatted string listing all students.

        Returns:
            str: String with all students' names and class grades, one per line.
        """
        return "\n".join(f"{s.name} {s.last_name} {s.class_grade}" for s in self.students)

    def get_student_count(self) -> int:
        """
        Returns the number of students in the system.

        Returns:
            int: The number of students.
        """
        return len(self.students)

    def get_class_average(self, class_grade: str) -> float:
        """
        Calculates the average grade for all students in a specific class.

        Args:
            class_grade (str): The class grade to calculate the average for.

        Returns:
            float: The average grade for the class.

        Raises:
            ValueError: If no students with grades are found in the class.
        """
        total = 0
        count = 0
        for student in self.students:
            if student.class_grade == class_grade:
                for grades_list in student.grades.values():
                    total += sum(grades_list)
                    count += len(grades_list)
        if count == 0:
            raise ValueError(f"No students with grades in class {class_grade}")
        return total / count

    def get_school_average(self) -> float:
        """
        Calculates the average grade for all students in the system.

        Returns:
            float: The overall school average grade.

        Raises:
            ValueError: If no students with grades are found.
        """
        total = 0
        count = 0
        for student in self.students:
            for grades_list in student.grades.values():
                total += sum(grades_list)
                count += len(grades_list)
        if count == 0:
            raise ValueError(f"No students with grades")
        return total / count

    def get_students_from_major(self, major: str) -> list[Student]:
        """
        Returns a list of students with a specific major (specialization).

        Args:
            major (str): The major to filter students by.

        Returns:
            list[Student]: List of students with the given major.
        """
        return [student for student in self.students if student.major.lower() == major.lower()]

    def sort_students_by_class_grade(self) -> list[Student]:
        """
        Returns a list of all students sorted alphabetically by class grade.

        Returns:
            list[Student]: Sorted list of students by class grade.
        """
        return sorted(self.students, key=lambda student: student.class_grade.lower(), reverse=False)

    def sort_students_by_major(self) -> list[Student]:
        """
        Returns a list of all students sorted alphabetically by major.

        Returns:
            list[Student]: Sorted list of students by major.
        """
        return sorted(self.students, key=lambda student: student.major.lower(), reverse=False)

    def sort_class_by_avg_grade(self) -> list[Student]:
        """
        Returns a list of all students sorted by their average grade (descending).
        Students with no grades are placed at the end.

        Returns:
            list[Student]: Sorted list of students by average grade (highest first).
        """
        def safe_avg(student: Student) -> float:
            try:
                return student.average_grade()
            except ValueError:
                return float('-inf')
        return sorted(self.students, key=safe_avg, reverse=True)

    def get_students_by_class(self, class_grade: str) -> list[Student]:
        """
        Returns a list of students belonging to a specific class grade.

        Args:
            class_grade (str): The class grade to filter students by.

        Returns:
            list[Student]: List of students in the given class grade.
        """
        return [student for student in self.students if student.class_grade.lower() == class_grade.lower()]

    def sort_students_by_avg_in_class(self, class_grade: str) -> list[Student]:
        """
        Returns a list of students in a given class, sorted by their average grade (descending).
        Students with no grades are placed at the end.

        Args:
            class_grade (str): The class grade to filter and sort students by.

        Returns:
            list[Student]: Sorted list of students in the class by average grade.
        """
        students_in_class = self.get_students_by_class(class_grade)
        def safe_avg(student: Student) -> float:
            try:
                return student.average_grade()
            except ValueError:
                return float('-inf')
        return sorted(students_in_class, key=safe_avg, reverse=True)

