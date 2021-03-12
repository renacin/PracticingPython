# Name:                                            Renacin Matadeen
# Date:                                               03/06/2021
# Title                                      Various Practice Questions
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import sys
sys.setrecursionlimit(10000)
# ----------------------------------------------------------------------------------------------------------------------



class recursive_questions:
    """ This class will store the answers to basic recursive python questions """


    @staticmethod
    def question_1a():
        """
        Question:
        Write a program which can compute the factorial of a given number. The results should be printed in a
        comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8
        Then, the output should be: 40320

        Completed:
        03-06-2021
        """

        # Factorial Function | Recursive Programming | Remember Base Case | Implement Cache System: MEMOIZATION
        num_cache = {}
        def fact(num):

            if num not in num_cache:
                if num <= 2:
                    return num
                else:
                    num_cache[num] = num * fact(num - 1)
                    return num_cache[num]
            return num_cache[num]

        print(fact(100))


    @staticmethod
    def question_1b():
        """
        Question:
        Create a function named backwardsby2, which prints numbers in reverse order using steps of 2;
        starting with an initial number. The breaking condition is if the number is less than or equal to zero.
        In that case, we simply print Zero! If that condition is not met, the function calls itself using the current
        number – 2. We also initialize a list and add a smiley emoji equal to the current number.

        Completed:
        03-07-2021
        """

        # Factorial Function | Recursive Programming | Remember Base Case
        def backby2(num):
            if num <= 0:
                print([0])

            else:
                print([x for x in reversed(range(0, num + 1, 2))])
                backby2(num-2)

        backby2(8)


    @staticmethod
    def question_1c():
        """
        Question:
        The Fibonacci sequence happens everywhere in the world and in all of nature. The sequence 0, 1, 1, 2, 3, 5, 8,
        13, 21, 34, and so on is the Fibonacci sequence. Each successive number is found by adding up the two numbers
        before it. Create a recursive function that models this process. The function will take the number of elements
        to be calculated.

        Completed:
        03-07-2021
        """

        num_cache = {}
        def fib(num):

            if num not in num_cache:
                if num <= 1:
                    return num
                num_cache[num] = fib(num - 1) + fib(num - 2)
                return num_cache[num]
            return num_cache[num]

        print(fib(500))



    @staticmethod
    def question_1d():
        """
        Question:
        Create a function to find out the sum of numbers from 1 to n. Where N is a user provided input.
        Ex. n = 4, return 10 [1 + 2 + 3 + 4]

        Completed:
        03-07-2021
        """

        # Define Base Case | Need To Understand Sequence Before Trying To Solve!
        # 0 Sum Equals 0, 1 Sum Equals 1, For 0, 1 Return Num
        num_cache = {}
        def sum_num(num):
            if num not in num_cache:
                if num <= 1:
                    return num
                return num + sum_num(num - 1)
            return num_cache[num]

        print(sum_num(1000))



    @staticmethod
    def question_1e():
        """
        Question:
        Create a recursive function that will reverse a string. Function will take a string and will return the reversed
        version of that string.
        Ex. input = "tag", return "gat"

        Completed:
        03-07-2021
        """

        # Define Base Case | Need To Understand Sequence Before Trying To Solve!
        # Dont Forget String Formatting & Slicing!
        def rev_string(string_input):
            if len(string_input) <= 1:
                return string_input
            else:
                return string_input[-1] + rev_string(string_input[:-1])

        print(rev_string("dictionary"))



    @staticmethod
    def question_1f():
        """
        Question:
        Create a function that takes a number and the power it will be raised to. Return the value of that calculation

        Completed:
        03-07-2021
        """

        # Define Base Case | Need To Understand Sequence Before Trying To Solve!
        def to_power(base_, power_):
            if power_ == 0:
                return 1

            else:
                return base_ * to_power(base_, power_ - 1)

        print(to_power(2, 5))



    @staticmethod
    def question_1g():
        """
        Question:
        Create a function that takes an integer and return the sum of each integer in that number.

        Completed:
        03-07-2021
        """

        # Define Base Case | Need To Understand Sequence Before Trying To Solve!
        # Need a better understanding of math!
        def sum_int(num):
            if num == 0:
                return 0

            else :
                return num%10 + sum_int(int(num/10))

        print(sum_int(1028))



    @staticmethod
    def question_1h():
        """
        Question:
        Create a function that takes a list of lists, and returns a list with all the values of the list in a single
        list

        Notes:
        You iterate through an entire list with: return my_list[0] + function[1:]

        Completed:
        03-12-2021
        """

        # Define Base Case | Need To Understand Sequence Before Trying To Solve!
        def flatten_list(my_list):

            # If Empty List Return List
            if my_list == []:
                return my_list

            # If The First Item In The List Is A List
            # Return Function Call On First Item And Function Call On Everything Else
            if isinstance(my_list[0], list):
                return flatten_list(my_list[0]) + flatten_list(my_list[1:])

            # If The First Item Isn't A List Return It AS A LIST ([0] VS [:1]) And A Function Call On Everything Else
            return my_list[:1] + flatten_list(my_list[1:])


        nested_list = [1, 2, 3, [4, 5, [6, 7, 8, 9], 10, 11, [12, 13]], 14, 15, [16], [[[17]]]]
        print(flatten_list(nested_list))



    @staticmethod
    def question_1i():
        """
        Question:
        Create a function that takes a list finds the sum of the elements in the list

        Completed:
        03-12-2021
        """

        # Define Base Case | Need To Understand Sequence Before Trying To Solve!
        def sum_list(my_list):
            if my_list == []:
                raise Exception("Empty List")
            if len(my_list) == 1:
                return my_list[0]
            return my_list[0] + sum_list(my_list[1:])

        x_list = [345, 67, 78, 34, 123]
        print(sum_list(x_list))



    @staticmethod
    def question_1j():
        """
        Question:
        Create a function that finds the sum of all elements within a list. Nested lists are expected.

        Completed:
        03-12-2021
        """

        # Define Base Case | Need To Understand Sequence Before Trying To Solve!
        val_cache = {"RunningTotal": 0}
        def flatten_sum(my_list):
            if my_list == []:
                return my_list

            if isinstance(my_list[0], list):
                return flatten_sum(my_list[0]) + flatten_sum(my_list[1:])

            else:
                val_cache["RunningTotal"] += my_list[0]
                return my_list[:1] + flatten_sum(my_list[1:])



        nested_list = [1, 2, 3, [4, 5, [6, 7, 8, 9], 10, 11, [12, 13]], 14, 15, [16], [[[17]]]]
        print(flatten_sum(nested_list), val_cache["RunningTotal"])
