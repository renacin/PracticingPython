# Name:                                             Renacin Matadeen
# Date:                                               11/30/2019
# Title                           Functions For Implementing Efficient Programming Techniques
#
# ----------------------------------------------------------------------------------------------------------------------
"""
Source:
    + Following - https://www.lynda.com/Python-tutorials/Tracing-memory-allocations/661762/716923-4.html?autoplay=true

Notes:
    + Create A SQLite Database and Practice SQL Queries
    + Create Test Data in Pandas - Save As CSV For SpeedUp

Questions Answered:
    + How do I create a list of random floats?
    + How do I calculate the distance between two coordinates?
    + Loop through one set of coords, and find the closest in another set
    + How do I profile my code and identify areas of improvement?
"""
# ----------------------------------------------------------------------------------------------------------------------
import random
import pandas as pd
import geopy.distance

import statistics

import line_profiler
from time import perf_counter
# ----------------------------------------------------------------------------------------------------------------------

def random_gen(number_of_rows):
    # Initialize Random System
    secure_random = random.SystemRandom()

    xs = [round(secure_random.uniform(45.50, 49.50), 2) for num in range(number_of_rows)]
    ys = [round(secure_random.uniform(75.50, 79.50), 2) for num in range(number_of_rows)]

    return xs, ys

# Create Test Data, Use Slower Calculation With GeoPy, Turn Into Pandas DF
def gen_data(num):
    dataset_1_xs, dataset_1_ys = random_gen(num)
    dataset_2_xs, dataset_2_ys = random_gen(num * 2)

    data_1 = {
        "Xs_1": dataset_1_xs,
        "Ys_1": dataset_1_ys
    }

    data_2 = {
        "Xs_2": dataset_2_xs,
        "Ys_2": dataset_2_ys
    }

    df1 = pd.DataFrame.from_dict(data_1)
    df2 = pd.DataFrame.from_dict(data_2)

    return df1, df2

# ----------------------------------------------------------------------------------------------------------------------
"""
Version 1.0
Notes:
    + Basic Comparison Between Points
"""

# Version #1 Of Search Function - Basic Calculate, Compare, and Retrieve
def find_closet_point_ver1(df1, df2):

    # Lists To Be Populated
    clst_point_distance = []
    clst_point_index = []

    # Loop Through Dataset 1 & Find Closet Point In Dataset 2
    for index1, row1 in df1.iterrows():
        point_1 = (row1['Xs_1'], row1['Ys_1'])

        # To Temporarily Store Distance Data
        temp_list = []

        # Find Distance To All Other Points
        for index2, row2 in df2.iterrows():
            point_2 = (row2['Xs_2'], row2['Ys_2'])
            distance_km = geopy.distance.distance(point_1, point_2).km
            temp_list.append(round(distance_km, 2))

        # Find Smallest Distance In List, and Return Index
        clst_distance = min(temp_list)
        clst_point_idx = temp_list.index(min(temp_list))

        # Append Data
        clst_point_distance.append(clst_distance)
        clst_point_index.append(clst_point_idx)

    df1["Clst_Point_1"] = clst_point_distance
    df1["Clst_Index_1"] = clst_point_index

# ----------------------------------------------------------------------------------------------------------------------
"""
Version 1.1
Notes:
    + Basic Comparison Between Points, However, Using Cython
"""
