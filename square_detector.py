import itertools
import operator
from formulas import *

class SquareDetector:

    def __init__(self, intersection_pts):
        # sort the intersections points
        intersection_pts = sorted(intersection_pts)

        # group the points of intersection by the row they're on
        rows = []
        for key,group in itertools.groupby(intersection_pts,operator.itemgetter(0)):
            rows.append(list(group))
    
        # --------- find the squares/bounding boxes identified by the points------------
        squares = []
        for row_ctr in range(len(rows)-1):
            row1 = rows[row_ctr]
            row2 = rows[row_ctr+1]
            
            for col in range( min(len(row1), len(row2)) -1 ):
                print("square start:")
                print(row1[col] , row1[col+1]  )
                print(row2[col] , row2[col+1]  )   
                square = (row1[col] , row1[col+1], row2[col] , row2[col+1] )
                squares.append(square)
        
        # filter out squares that are too small
        areas = [area_square(square) for square in squares]
        mean_area = sum(areas)/len(areas)
        squares = [square for square in squares if area_square(square) >= mean_area]
        
        self.squares = squares
        print("HELOOOOOOOOOOOOOOOO", len(self.squares))






