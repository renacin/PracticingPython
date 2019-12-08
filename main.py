# Name:                                             Renacin Matadeen
# Date:                                               12/08/2019
# Title                               Implementing Efficient Programming Techniques
#
# ----------------------------------------------------------------------------------------------------------------------

from functions import *

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Make Data
    set_1, set_2 = random_data(100)

    # Find Closest | Save For Comparison | Time As Baseline
    clst_points_distances, clst_point_index = find_closet_point_ver1(set_1, set_2)
