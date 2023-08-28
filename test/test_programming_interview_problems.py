from unittest import TestCase

from main.programming_interview_problems import ProgrammingInterviewProblems


class TestProgrammingInterviewProblems(TestCase):

    def testProblem1InvalidInputNoNumberMissingCase(self):
        prob1_arr = []
        for i in range(1, 101):
            prob1_arr.append(i)

        try:
            ProgrammingInterviewProblems.findMissingNumber(prob1_arr)
        except ValueError as context:
            self.assertTrue('Invalid input: there are no numbers missing.' in context.__str__())

    def testProblem1FirstNumberMissingCase(self):
        prob1_arr = []
        for i in range(1, 101):
            if i != 1:
                prob1_arr.append(i)

        missing_number = ProgrammingInterviewProblems.findMissingNumber(prob1_arr)
        self.assertEqual(1, missing_number)

    def testProblem1LastNumberMissingCase(self):
        prob1_arr = []
        for i in range(1, 101):
            if i != 100:
                prob1_arr.append(i)

        missing_number = ProgrammingInterviewProblems.findMissingNumber(prob1_arr)
        self.assertEqual(100, missing_number)

    def testProblem1MissingNumberGeneralCase(self):
        prob1_arr = []
        for i in range(1, 101):
            if i != 2:
                prob1_arr.append(i)

        missing_number = ProgrammingInterviewProblems.findMissingNumber(prob1_arr)
        self.assertEqual(2, missing_number)
