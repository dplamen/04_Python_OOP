from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Peter", {'Math': [5, 6, 4]})

    def test_initialization_student(self):
        self.assertEqual('Peter', self.student.name)
        self.assertEqual({'Math': [5, 6, 4]}, self.student.courses)
        self.student2 = Student("John")
        self.assertEqual('John', self.student2.name)
        self.assertEqual({}, self.student2.courses)

    def test_enroll_for_enrolled_course(self):
        result = self.student.enroll("Math", [4, 5, 5])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual([5, 6, 4, 4, 5, 5], self.student.courses["Math"])

    def test_enroll_new_course_with_notes(self):
        result = self.student.enroll("History", [4, 6, 6], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual([4, 6, 6], self.student.courses["History"])
        result2 = self.student.enroll("Economics", [5, 5, 5])
        self.assertEqual("Course and course notes have been added.", result2)
        self.assertEqual([5, 5, 5], self.student.courses["Economics"])

    def test_enroll_new_course_without_notes(self):
        result = self.student.enroll("History", [4, 6, 6], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["History"])
        
    def test_add_notes_for_missing_course_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Biology", [3, 4, 6])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_existing_course(self):
        result = self.student.add_notes("Math", 3)
        self.assertEqual("Notes have been updated", result)
        self.assertEqual([5, 6, 4, 3], self.student.courses["Math"])

    def test_leave_course_not_enrolled(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("History")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_enrolled_course(self):
        result = self.student.leave_course("Math")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)


if __name__ == '__main__':
    main()

