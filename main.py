# Name:                                             Renacin Matadeen
# Date:                                               11/30/2019
# Title                               Implementing Efficient Programming Techniques
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
"""
# ----------------------------------------------------------------------------------------------------------------------
import random
import pandas as pd
import geopy.distance
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

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    set_1, set_2 = random_data(1000)







"""
    for x, y in zip(pt_1_coords, pt_2_coords):
        distance_km = geopy.distance.vincenty(x, y).km
        distance.append(round(distance_km))
"""
