# Name:                                            Renacin Matadeen
# Date:                                               03/06/2021
# Title                                      Various Practice Questions
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------


class basic_questions:
    """ This class will store the answers to basic python questions """


    @staticmethod
    def question_1():
        """
        Question:
        Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5;
        Between 2000 and 3200 (both included). The numbers obtained should be printed in a
        comma-separated sequence on a single line.

        Completed:
        03-06-2021
        """

        # List Comprehension Is Incredible! Look For Functions That Require Filtered Lists
        list_of_numbers = [str(x) for x in range(2000, 3201) if (x % 7 == 0) and (x % 5 != 0)]
        str_answer = ", ".join(list_of_numbers)

        print(str_answer)


    @staticmethod
    def question_2():
        """
        Question:
        Write a program which can compute the factorial of a given number. The results should be printed in a
        comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8
        Then, the output should be: 40320

        Completed:
        03-06-2021
        """

        # Factorial Function | Recursive Programming
        # Sets Up Code & Holds In Memory Until Last Value Is Identified | Then Performs Major Arithmetic
        # Recursive Programming Is Hard | Need More Examples
        def fact(num):
            if num == 0:
                return 1
            return num * fact(num - 1)

        print(fact(8))
