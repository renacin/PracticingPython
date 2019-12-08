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
    set_1_x, set_1_y, set_2_x, set_2_y = gen_data(100)

    # Find Closest Point
    find_closet_point_ver1(set_1_x, set_1_y, set_2_x, set_2_y)
