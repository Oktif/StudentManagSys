from src.student import Student
from src.student_system import StudentSystem

def main_menu(system: StudentSystem):
    while True:
        print("\n=== GŁÓWNE MENU ===")
        print("1. Zarządzanie studentem")
        print("2. Zarządzanie ocenami studenta")
        print("3. Zarządzanie szkołą")
        print("0. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            student_management_menu(system)
        elif choice == "2":
            grades_management_menu(system)
        elif choice == "3":
            school_management_menu(system)
        elif choice == "0":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

# --- ZARZĄDZANIE STUDENTEM ---
def student_management_menu(system: StudentSystem):
    while True:
        print("\n--- Zarządzanie studentem ---")
        print("1. Dodaj studenta")
        print("2. Usuń studenta")
        print("3. Edytuj dane studenta")
        print("0. Powrót do głównego menu")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_student_to_system(system)
        elif choice == "2":
            remove_student_from_system(system)
        elif choice == "3":
            edit_student_data(system)
        elif choice == "0":
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

def add_student_to_system(system: StudentSystem):
    print("\nDodawanie nowego studenta:")
    name = input("Imię: ")
    last_name = input("Nazwisko: ")
    class_grade = input("Klasa (np. 1A): ")
    major = input("Specjalizacja: ")
    try:
        year = int(input("Rok (np. 2024): "))
    except ValueError:
        print("Nieprawidłowy rok!")
        return
    student = Student(name, last_name, class_grade, major, year)
    system.add_student(student)
    print(f"Dodano studenta: {student}")

def remove_student_from_system(system: StudentSystem):
    print("\nUsuwanie studenta:")
    name = input("Imię: ")
    last_name = input("Nazwisko: ")
    try:
        year = int(input("Rok (np. 2024): "))
    except ValueError:
        print("Nieprawidłowy rok!")
        return
    if system.remove_student(name, last_name, year):
        print("Student został usunięty.")
    else:
        print("Nie znaleziono takiego studenta.")

def edit_student_data(system: StudentSystem):
    print("\nEdycja danych studenta:")
    name = input("Imię: ")
    last_name = input("Nazwisko: ")
    try:
        year = int(input("Rok (np. 2024): "))
    except ValueError:
        print("Nieprawidłowy rok!")
        return
    student = system.find_student(name, last_name, year)
    if not student:
        print("Nie znaleziono takiego studenta.")
        return
    print("Co chcesz zmienić?")
    print("1. Imię i nazwisko")
    print("2. Klasę")
    print("3. Specjalizację")
    print("4. Usuń wszystkie oceny")
    print("0. Anuluj")
    choice = input("Wybierz opcję: ")
    if choice == "1":
        new_name = input("Nowe imię: ")
        new_last_name = input("Nowe nazwisko: ")
        student.change_name(new_name, new_last_name)
        print("Dane zostały zmienione.")
    elif choice == "2":
        new_class = input("Nowa klasa (np. 2A): ")
        student.change_class_grade(new_class)
        print("Klasa została zmieniona.")
    elif choice == "3":
        new_major = input("Nowa specjalizacja: ")
        student.change_major(new_major)
        print("Specjalizacja została zmieniona.")
    elif choice == "4":
        student.delete_all_grades()
        print("Wszystkie oceny zostały usunięte.")
    else:
        print("Anulowano edycję.")

# --- ZARZĄDZANIE OCENAMI ---
def grades_management_menu(system: StudentSystem):
    while True:
        print("\n--- Zarządzanie ocenami ---")
        print("1. Dodaj ocenę studentowi")
        print("2. Usuń ocenę studenta")
        print("3. Pokaż oceny z przedmiotu")
        print("4. Pokaż średnią z przedmiotu")
        print("5. Pokaż średnią wszystkich ocen studenta")
        print("6. Pokaż podsumowanie studenta")
        print("0. Powrót do głównego menu")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_grade_to_student(system)
        elif choice == "2":
            remove_grade_from_student(system)
        elif choice == "3":
            show_subject_grades(system)
        elif choice == "4":
            show_subject_average(system)
        elif choice == "5":
            show_overall_average(system)
        elif choice == "6":
            show_student_summary(system)
        elif choice == "0":
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

def add_grade_to_student(system: StudentSystem):
    student = find_student_prompt(system)
    if not student:
        return
    subject = input("Przedmiot: ")
    try:
        grade = float(input("Ocena (1.0-6.0): "))
    except ValueError:
        print("Nieprawidłowa ocena!")
        return
    try:
        student.add_grade(subject, grade)
        print("Dodano ocenę.")
    except ValueError as e:
        print(e)

def remove_grade_from_student(system: StudentSystem):
    student = find_student_prompt(system)
    if not student:
        return
    subject = input("Przedmiot: ")
    try:
        removed = student.remove_last_grade(subject)
        print(f"Usunięto ocenę: {removed}")
    except ValueError as e:
        print(e)

def show_subject_grades(system: StudentSystem):
    student = find_student_prompt(system)
    if not student:
        return
    subject = input("Przedmiot: ")
    try:
        grades = student.get_subject_grades(subject)
        print(f"Oceny z przedmiotu {subject}: {grades}")
    except ValueError as e:
        print(e)

def show_subject_average(system: StudentSystem):
    student = find_student_prompt(system)
    if not student:
        return
    subject = input("Przedmiot: ")
    try:
        avg = student.average_subject_grade(subject)
        print(f"Średnia z przedmiotu {subject}: {avg:.2f}")
    except ValueError as e:
        print(e)

def show_overall_average(system: StudentSystem):
    student = find_student_prompt(system)
    if not student:
        return
    try:
        avg = student.average_grade()
        print(f"Średnia wszystkich ocen studenta: {avg:.2f}")
    except ValueError as e:
        print(e)

def show_student_summary(system: StudentSystem):
    student = find_student_prompt(system)
    if not student:
        return
    summary = student.get_student_summary()
    print("Podsumowanie studenta:")
    for k, v in summary.items():
        print(f"{k}: {v}")

def find_student_prompt(system: StudentSystem):
    name = input("Imię studenta: ")
    last_name = input("Nazwisko studenta: ")
    try:
        year = int(input("Rok studenta: "))
    except ValueError:
        print("Nieprawidłowy rok!")
        return None
    student = system.find_student(name, last_name, year)
    if not student:
        print("Nie znaleziono takiego studenta.")
    return student

# --- ZARZĄDZANIE SZKOŁĄ ---
def school_management_menu(system: StudentSystem):
    while True:
        print("\n--- Zarządzanie szkołą ---")
        print("1. Pokaż wszystkich studentów")
        print("2. Pokaż studentów z klasy")
        print("3. Pokaż studentów ze specjalizacji")
        print("4. Liczba studentów")
        print("5. Średnia ocen klasy")
        print("6. Średnia ocen szkoły")
        print("7. Posortuj studentów")
        print("0. Powrót do głównego menu")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            print(system.show_all_students())
        elif choice == "2":
            class_grade = input("Podaj klasę (np. 1A): ")
            students = system.get_students_by_class(class_grade)
            for student in students:
                print(student)
        elif choice == "3":
            major = input("Podaj specjalizację: ")
            students = system.get_students_from_major(major)
            for student in students:
                print(student)
        elif choice == "4":
            print(f"Liczba studentów: {system.get_student_count()}")
        elif choice == "5":
            class_grade = input("Podaj klasę (np. 1A): ")
            try:
                avg = system.get_class_average(class_grade)
                print(f"Średnia ocen w klasie {class_grade}: {avg:.2f}")
            except ValueError as e:
                print(e)
        elif choice == "6":
            try:
                avg = system.get_school_average()
                print(f"Średnia ocen szkoły: {avg:.2f}")
            except ValueError as e:
                print(e)
        elif choice == "7":
            sort_students_menu(system)
        elif choice == "0":
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

def sort_students_menu(system: StudentSystem):
    print("\n--- Sortowanie studentów ---")
    print("1. Po klasie")
    print("2. Po specjalizacji")
    print("3. Po średniej ocen w klasie")
    print("4. Po średniej ocen w szkole")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        students = system.sort_students_by_class_grade()
    elif choice == "2":
        students = system.sort_students_by_major()
    elif choice == "3":
        class_grade = input("Podaj klasę (np. 1A): ")
        students = system.sort_students_by_avg_in_class(class_grade)
    elif choice == "4":
        students = system.sort_class_by_avg_grade()
    else:
        print("Nieprawidłowa opcja sortowania.")
        return

    for student in students:
        print(student)

# --- START PROGRAMU ---
if __name__ == "__main__":
    system = StudentSystem()
    main_menu(system)
