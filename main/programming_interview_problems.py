class ProgrammingInterviewProblems:

    """
    Return the missing number in a given integer array of 1 to 100
    """
    @staticmethod
    def findMissingNumber(arr):
        is_number_missing = False
        for i in range(100):
            if i == 99 and len(arr) == 99:
                is_number_missing = True
                break

            if i + 1 < arr[i]:
                is_number_missing = True

        if not is_number_missing:
            raise ValueError('Invalid input: there are no numbers missing.')

        for i in range(99):
            if i + 1 < arr[i]:
                return i + 1

        return 100
