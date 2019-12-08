# Name:                                             Renacin Matadeen
# Date:                                               12/08/2019
# Title                               Implementing Efficient Programming Techniques
#
# ----------------------------------------------------------------------------------------------------------------------
from functions import *
from time import perf_counter
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Make Data
    df1, df2 = gen_data(10)

    # Find Closest Point
    find_closet_point_ver1(df1, df2)
