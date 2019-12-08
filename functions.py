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


# Create Test Data, Use Slower Calculation With GeoPy, Turn Into Pandas DF
def random_data(number_rows):
    # Initialize Random System
    secure_random = random.SystemRandom()

    # X, Y For List One
    pt_1_coords = []
    for x in range(number_rows):
        point_4_1 = (round(secure_random.uniform(45.50, 49.50), 2), round(secure_random.uniform(75.50, 79.50), 2))
        pt_1_coords.append(point_4_1)

    # X, Y For List Two
    pt_2_coords = []
    for x in range(number_rows):
        point_4_2 = (round(secure_random.uniform(45.50, 49.50), 2), round(secure_random.uniform(75.50, 79.50), 2))
        pt_2_coords.append(point_4_2)

    return pt_1_coords, pt_2_coords


# Version #1 Of Search Function - Basic Calculate, Compare, and Retrieve
def find_closet_point_ver1(data_1, data_2):
    # Lists To Be Populated
    clst_point_distance = []
    clst_point_index = []

    # Loop Through Dataset 1 & Find Closet Point In Dataset 2
    for point_1 in data_1:
        temp_list = []

        # Find Distance To All Other Points
        for point_2 in data_2:
            distance_km = geopy.distance.distance(point_1, point_2).km # According To Line Profiler Alot Of Time Wasted Here
            temp_list.append(round(distance_km, 2))

        # Find Smallest Distance In List, and Return Index
        clst_distance = min(temp_list)
        clst_point_idx = temp_list.index(min(temp_list))

        # Append Data
        clst_point_distance.append(clst_distance)
        clst_point_index.append(clst_point_idx)

    return clst_point_distance, clst_point_index


# Version #2 Of Search Function - Find Closest Point, While Focusing On Small Datasets, Then Compare, and Pull
def find_closet_point_ver2(data_1, data_2):
    # Lists To Be Populated
    clst_point_distance = []
    clst_point_index = []

    # Loop Through Dataset 1 & Find Closet Point In Dataset 2
    for point_1 in data_1:
        temp_list = []

        # Find Distance To All Other Points
        for point_2 in data_2:
            distance_km = geopy.distance.distance(point_1, point_2).km # According To Line Profiler Alot Of Time Wasted Here
            temp_list.append(round(distance_km, 2))

        # Find Smallest Distance In List, and Return Index
        clst_distance = min(temp_list)
        clst_point_idx = temp_list.index(min(temp_list))

        # Append Data
        clst_point_distance.append(clst_distance)
        clst_point_index.append(clst_point_idx)

    print(statistics.mean(clst_point_distance))
    return clst_point_distance, clst_point_index
