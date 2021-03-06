# Name:                                            Renacin Matadeen
# Date:                                               03/06/2021
# Title                                      Various Practice Questions
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys, time
from PIL import Image, ExifTags

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



    @staticmethod
    def question_1k():
        """
        Question:
        Create a function that finds the harmonic sum; given an input integer greater than 2.

        Completed:
        03-12-2021
        """

        def harm_sum(n):
            if n <= 1:
                return 1
            return 1/n + harm_sum(n-1)

        print(harm_sum(10))



    @staticmethod
    def question_1l():
        """
        Question:
        Create a function that finds sum of all values across the range 1 - N; And given the function x = 2/n + 10*n - n.

        Completed:
        03-13-2021
        """

        num_cache = {}
        def sum_func(n):
            if n not in num_cache:
                if n <= 1:
                    num_cache[n] = 4
                    return num_cache[n]
                else:
                    num_cache[n] = int(((2/n) + (2**n) + n))
                    return num_cache[n] + sum_func(n-1)
            return num_cache[n]

        print(sum_func(10))
        print(num_cache)



    @staticmethod
    def question_1m():
        """
        Question:
        Create a function that returns all files within a folder as a list. Must account for nested folders!

        Completed:
        03-13-2021
        """

        file_cache = {"Files": [], "Folders": []}
        def folder_walk(folder_path):

            directory_ = os.listdir(folder_path)
            for item in directory_:

                item_path = folder_path + "\\" + item

                # If The Item Is A Folder Store It & Call Recursive Function
                if os.path.isdir(item_path):
                    file_cache["Folders"].append(item_path)
                    folder_walk(item_path)

                # The Item Is A File | Append Data To Cache
                file_cache["Files"].append(item_path)

        # specify your path of directory
        path = r"C:\Users\renac\Documents\Programming\Python\PracticingPython\PracticeQuestions\PythonQuestions"
        folder_walk(path)
        print(file_cache)



    @staticmethod
    def question_1n():
        """
        Question:
        Create a function that looks for through nested folders for images, and returns their metadata.

        Completed:
        03-14-2021
        """

        picture_cache = []
        def find_picmetadata(path):

            directory_ = os.listdir(path)
            for item in directory_:

                item_path = path + "\\" + item

                # If The Item Is A Folder Call Recursive Function & Look For Pictures
                if os.path.isdir(item_path):
                    find_picmetadata(item_path)

                # The Item Is A File | Append Data To Cache
                root, extension = os.path.splitext(item_path)
                if extension in [".jpeg", ".jpg", ".png", ".tiff", ".tif"]:
                    image = Image.open(item_path)
                    img_exif = image.getexif()

                    # Look For EXIF Data | Create Cleaned DF | Append To List
                    if img_exif:
                        temp_dict = {}
                        img_exif_dict = dict(img_exif)
                        for key, val in img_exif_dict.items():
                            if key in ExifTags.TAGS:
                                temp_dict[ExifTags.TAGS[key]] = val
                        temp_dict["IMAGE_NAME"] = item_path
                        picture_cache.append(temp_dict)

        # specify your path of directory
        path = r"C:\Users\renac\Documents\Programming\Python\PracticingPython\PracticeQuestions\Misc"
        find_picmetadata(path)
        print(picture_cache)



    @staticmethod
    def question_1o():
        """
        Question:
        Create a function that finds the greatest common denominator between two integers.

        Completed:
        03-15-2021
        """

        def gcd(int_1, int_2):
        	low = min(int_1, int_2)
        	high = max(int_1, int_2)

        	if low == 0:
        		return high

        	elif low == 1:
        		return 1

        	else:
        		return gcd(low, high%low)

        print(100, 220)



    @staticmethod
    def question_1p():
        """
        Question:
        There are different types of recursion. From the previous examples we have been calling our recursive functions
        if a certain parametre was met. In some cases you will need your recursive function to be called everytime an
        iteration is completed. This is called tail recursion.

        Create a function that implements tail recursion.

        NOTE PYTHON DOESN'T OPTIMIZE FOR TAIL-RECURSION!

        Why Use Tail Recursion?
            + Allows for some optimization by the compiler
            + No burden of retaining a stack frame
            + More readable

        More Examples Of Tail Recursion
        # Non Tail Recursive
        def fact(n):
            if (n == 0):
                return 1
            return n * fact(n-1)

        # Tail Recursive
        def fact(n, a = 1):
            if (n == 0):
                return a
            return fact(n - 1, n * a)

        Completed:
        03-16-2021
        """

        def tail_recur(n):

            # Case To Break Recursion
            if (n < 0):
                return

            # Else Keep Running | keep Adding To Common Line
            text_ = str(n) + " "
            print(text_, end='')
            tail_recur(n-1)

        tail_recur(5)


    @staticmethod
    def question_1q():
        """
        Question:
        When speaking of recursion there are two general styles of programming. Those two types include basic recursion
        and dynamic programing. Basic recursion requires that a function call itself in order to solve smaller sub-queries.
        As useful as this programming technique may be there are a number of glaring issues. Some of those issues include
        the number of calls to the stack, total runtime, and total memory of algorithms following this programming style.
        An improvement to this would be dynamic programing; specifically, top-down memoization. In a top-down approach,
        making use of dynamic programing a developer tries to minimize the number of redundant calculations executed
        making use of a cache. This is a significant improvement to previous implementations of recursion but still requires
        recursive calls that may be memory intensive. One improvement to this is bottom-up dynamic programming. In this
        style of programming developers look to do without recursion and large memory calls by using simple iterators to
        achieve desired results.

        Create a function that finds the nth value of the Fibonacci sequence making use of a bottom-up approach to
        dynamic programing.

        Completed:
        03-19-2021
        """

        # In This Case Both Space & Time Are O(N)
        def dp_fib_1(n):
          cache = [0, 1]
          for i in range(2, n + 1):
            cache.append(cache[i - 1] + cache[i - 2])
          return cache[n]

        # In This Case Space Is O(1) & Time Is O(N) | This really shows off the power of dynamic programming
        def dp_fib_2(n):
            a = 0
            b = 1
            for i in range(2, n + 1):
                a = a + b
                b, a = a, b
            return b

        print(dp_fib_2(100_000))


    @staticmethod
    def question_1r():
        """
        Question:
        Create a function that first finds the change to be returned to a customer given the total price of their purchase
        as well as the tender given. Additionaly finds the fewest number of coins to return Make note of the number,
        and value of coins returned.

        Completed:
        03-20-2021
        """

        # This Is A Greedy Approach To This Problem | Currently Doesn't Use Recursion
        def make_change(tender_given, total_price):
            if tender_given < total_price:
                return "Insufficient Funds"

            elif tender_given == total_price:
                return "No Change"

            else:
                amount = tender_given - total_price
                change_cache = {50.00: 0, 20.00: 0, 10.00: 0, 5.00: 0, 2.00: 0, 1.00: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
                for change in change_cache:
                    if amount >= change:
                        num_change = amount // change
                        amount = round(amount - (num_change * change), 2)
                        change_cache[change] += num_change

                total_num_change = sum([num for (change, num) in change_cache.items() if num != 0])
                status_string = f"Price: ${total_price},Tender: ${tender_given}, Change: ${tender_given - total_price}, Number Of Change Items: {total_num_change}"
                return {change:num for (change, num) in change_cache.items() if num != 0}, status_string

        print(make_change(100, 23.92))



    @staticmethod
    def question_1s():
        """
        Question:
        Create a function that recursively finds everyway to create change given an input that represents a dollar amount.
        The input value must be an integer greater than 1; the function must also output all possible combinations as well
        as the number of combinations available.

        Completed:
        03-22-2021
        """

        # Find Ways To Make Change With Recursion | This is unfortunately exponential!
        def ways_2_make_change_1(amount, typesofcoins=[1, 2, 3]):

            # If the amount is zero return 1
            if amount == 0:
                return 1
            if amount < 0:
                return 0

            # For Each Coin In List
            result = 0
            for i in range(len(typesofcoins)):
                result += ways_2_make_change(amount - typesofcoins[i])

            return result



        # Find Ways To Make Change With Bottom Up Dynamic Programming | This is Linear In Space & Complexity
        def ways_2_make_change_2(amount, typesofcoins=[1, 2]):

            # Remember This Is Dynamic Programming | Only Called Once | Not Recursive
            # T Represents A List Of Zeros Of Lenght (Amount + 1), The First Value Is Always 1
            T = [0] * (amount + 1)                         # T = [0, 0, 0, 0, 0, 0] 5 + 1
            T[0] = 1                                       # T = [1, 0, 0, 0, 0, 0] Index 0 --> 1

            # Iterate Through Number Of Coins [i = 0, 1]
            for i in range(len(typesofcoins)):

                # j Represents the denomination of a coin [j = 1, 2]
                j = typesofcoins[i]

                # While j (a denomination of coin) is less than or equal to the amount do sub task
                while j <= amount:

                    # List T At Index J                    # 3 - 1
                    print(f"T Before:{T}")
                    T[j] += T[j - typesofcoins[i]]         # 1. (i=0, j=1) T = [1, 2 , 0, 0, 0, 0],    2. (i=0, j=2) T = [1, 2 , 2, 0, 0, 0],     3. (i=0, j=3) T = [1, 2 , 2, 2, 0, 0]
                    print(f"Amount: {amount}, j:{j}, T[j]:{T[j]}, TypeOfCoin:{typesofcoins[i]}")
                    print(f"T Before:{T}")
                    print("")


                    j += 1

            return T[amount]

        print(ways_2_make_change_2(2))

        # Complicated | This isn't the most readable solution!
        # Better Understand This Problem, And Then Maybe Move Onto One More Problem. Need To Start Census Data Cleaning



    @staticmethod
    def question_1t():
        """
        Question:
        Create a function that identifies if a string is a palindrome. Use recursion first, then dynamic programming.
        Note that strings can be either even, or odd lenght. Assume string is common case and no numbers of spaces, and
        you can't use the reverse string function

        Another way to have completed task was to reverse the string and check if both values were equal.

        Completed:
        04-24-2021
        """

        def palin_check(in_string):
            """ Input string, algorithm determines if input is a palindrome """

            # If only one character then string is a palindrome
            if len(in_string) == 1:
                print("Is a palindrome")

            # If two characters & both same them this is a palindrome
            elif (len(in_string) == 2) and (in_string[0] == in_string[-1]):
                print("Is a palindrome")

            # If longer check ends and recursively check for palindrome
            else:
                if in_string[0] == in_string[-1]:
                    palin_check(in_string[1:-1])

                else:
                    print("Not palindrome")


        palin_check("kook")



    @staticmethod
    def question_1u():
        """
        Question:
        Create a function that identifies the index of a capitalized letter within a string.
        Can be completed recursively or linearly.

        Note that string can have more than one capitalized characters.

        Completed:
        04-24-2021
        """

        def cap_check(in_string, ridx = 0) -> "Index & Character Value For Each Capitalized Letter":

            # Make sure input is greater or equal to 1!
            if len(in_string) >= 1:

                # If more that one character check first letter is cap
                if in_string[0].isupper():
                    print(f"Letter: {in_string[0]}, Index: {ridx}")
                    cap_check(in_string[1:], ridx + 1)

                # Move onto next index if none satisfied
                else:
                    cap_check(in_string[1:], ridx + 1)


        cap_check("TheVergeOfGreatness")



    @staticmethod
    def question_1v():
        """
        Question:
        Given a list of numbers, find every permutation possible.
        """

        def permu(in_list: list) -> "List of all permutations":
