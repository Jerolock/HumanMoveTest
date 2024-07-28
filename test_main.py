import unittest
from unittest import TestCase
from HumanMoveTest.main import Student


class StudentTest(TestCase):

    def test_first_walk_10_times(self):
        self.student = Student("Vasya")
        for _ in range(10):
            self.student.walk()
        result = self.student.distance
        self.assertEqual(result,
                         500,
                         f"Дистанции не равны [дистанция человека {self.student.name}] != 500")

    def test_second_run_10_times(self):
        self.student = Student("Katya")
        for _ in range(10):
            self.student.run()
        result = self.student.distance
        self.assertEqual(result,
                         1000,
                         f"Дистанции не равны [дистанция человека {self.student.name}] != 1000")

    def test_third_competition_run_vs_walk(self):
        self.student_1 = Student("Katya")
        self.student_2 = Student("Vasya")
        self.student_1.run(), self.student_2.walk()
        result_1, result_2 = self.student_1.distance, self.student_2.distance
        self.assertGreater(result_1,
                           result_2,
                           f"[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]]")

        self.assertLess(result_2,
                        result_1,
                        f"[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]]")


if __name__ == "__main__":
    unittest.main()