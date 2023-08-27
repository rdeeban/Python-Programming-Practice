class ProgrammingInterviewProblems:

    """
    Return the missing number in a given integer array of 1 to 100
    """
    @staticmethod
    def findMissingNumber(arr):
        for i in range(99):
            if i + 1 < arr[i]:
                return i + 1

        return 100