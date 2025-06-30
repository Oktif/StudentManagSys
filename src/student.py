class Student:
    """
    Represents a student with basic information, specialization, class, and a record of grades for each subject.
    """

    def __init__(self, name: str, last_name: str, class_grade: str, major: str, year: int):
        """
        Initializes a Student object.

        Args:
            name (str): First name of the student.
            last_name (str): Last name of the student.
            class_grade (str): Class grade (e.g., '1A', '2B').
            major (str): Specialization or major of the student.
            year (int): Enrollment or graduation year of the student.
        """
        self.name = name
        self.last_name = last_name
        self.class_grade = class_grade
        self.major = major
        self.year = year
        self.grades: dict[str, list[float]] = {}

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the student, including name, class, major, and year.

        Returns:
            str: Basic info about the student.
        """
        return f"Student {self.name} {self.last_name}, class {self.class_grade}, major: {self.major}, year: {self.year}"

    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation of the student, including all key attributes for debugging.

        Returns:
            str: All key attributes of the student.
        """
        return (f"Student (name={self.name!r}, last_name={self.last_name!r}, "
                f"class={self.class_grade!r}, major={self.major!r}, year={self.year!r})")

    def add_grade(self, subject: str, grade: float) -> None:
        """
        Adds a grade for the specified subject.

        Args:
            subject (str): Name of the subject.
            grade (float): Grade value (between 1.0 and 6.0).

        Raises:
            ValueError: If the grade is not in the valid range (1.0–6.0).
        """
        if grade < 1.0 or grade > 6.0:
            raise ValueError("Grade must be between 1.0 and 6.0")
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def remove_last_grade(self, subject: str) -> float:
        """
        Removes and returns the last grade added for the specified subject.

        Args:
            subject (str): Name of the subject.

        Returns:
            float: The removed grade.

        Raises:
            ValueError: If the subject has no grades.
        """
        if subject not in self.grades or not self.grades[subject]:
            raise ValueError(f"No grades for subject: {subject}")
        return self.grades[subject].pop()

    def get_subject_grades(self, subject: str) -> list[float]:
        """
        Retrieves all grades for the specified subject.

        Args:
            subject (str): Name of the subject.

        Returns:
            list[float]: List of grades for the subject.

        Raises:
            ValueError: If the subject has no grades.
        """
        if subject not in self.grades or not self.grades[subject]:
            raise ValueError(f"No grades for subject: {subject}")
        return self.grades[subject]

    def get_all_grades(self) -> dict[str, list[float]]:
        """
        Returns a copy of all grades for all subjects.

        Returns:
            dict[str, list[float]]: Dictionary of all subjects and their grades.
        """
        return self.grades.copy()

    def average_subject_grade(self, subject: str) -> float:
        """
        Calculates the average grade for a given subject.

        Args:
            subject (str): Name of the subject.

        Returns:
            float: Average grade for the subject.

        Raises:
            ValueError: If the subject has no grades.
        """
        if subject not in self.grades or not self.grades[subject]:
            raise ValueError(f"No grades for subject: {subject}")
        return sum(self.grades[subject]) / len(self.grades[subject])

    def average_grade(self) -> float:
        """
        Calculates the average grade across all subjects.

        Returns:
            float: Overall average grade.

        Raises:
            ValueError: If the student has no grades at all.
        """
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        if count == 0:
            raise ValueError(f"Student {self.name} {self.last_name} has no grades")
        return total / count

    def delete_subject(self, subject: str) -> bool:
        """
        Deletes all grades for the specified subject.

        Args:
            subject (str): Name of the subject.

        Returns:
            bool: True if the subject was deleted.

        Raises:
            ValueError: If the subject does not exist for this student.
        """
        if subject not in self.grades:
            raise ValueError(f"{subject} is not a valid subject for this student")
        del self.grades[subject]
        return True

    def change_name(self, new_name: str, new_last_name: str) -> bool:
        """
        Changes the student's name and last name.

        Args:
            new_name (str): New first name to set.
            new_last_name (str): New last name to set.

        Returns:
            bool: True if the name or last name was changed, False if both are already set.
        """
        if self.name == new_name and self.last_name == new_last_name:
            return False
        self.name = new_name
        self.last_name = new_last_name
        return True

    def change_major(self, new_major: str) -> bool:
        """
        Changes the student's major.

        Args:
            new_major (str): New major to set.

        Returns:
            bool: True if the major was changed, False if it was already set.
        """
        if self.major == new_major:
            return False
        self.major = new_major
        return True

    def change_class_grade(self, new_class_grade: str) -> bool:
        """
        Changes the student's class grade.

        Args:
            new_class_grade (str): New class grade to set.

        Returns:
            bool: True if the class grade was changed, False if it was already set.
        """
        if self.class_grade == new_class_grade:
            return False
        self.class_grade = new_class_grade
        return True

    def delete_all_grades(self) -> bool:
        """
        Deletes all grades for the student.

        Returns:
            bool: True after all grades are cleared.
        """
        self.grades.clear()
        return True

    def get_student_summary(self) -> dict[str, object]:
        """
        Returns a summary of the student's basic information and statistics.

        Returns:
            dict[str, object]: Summary dictionary including name, class, major, number of subjects,
                               total number of grades, and average grade (or None if no grades).
        """
        summary = {
            "name": f"{self.name} {self.last_name}",
            "class": self.class_grade,
            "major": self.major,
            "year": self.year,
            "subjects": len(self.grades),
            "total_grades": sum(len(g) for g in self.grades.values()),
        }
        try:
            summary["average"] = self.average_grade()
        except ValueError:
            summary["average"] = None
        return summary
