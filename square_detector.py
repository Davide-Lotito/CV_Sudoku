import itertools
import operator
from formulas import *


class SquareDetector:

    def __init__(self, intersection_pts):

        
        # sort the intersection points
        intersection_pts = sorted(intersection_pts)

        # group the points of intersection by the row they're on
        rows = []
        for key,group in itertools.groupby(intersection_pts,operator.itemgetter(0)):
            rows.append(list(group))
        

        # number of columns MUST be equal to number of rows!
        assert len(rows)==len(rows[0]), "number of columns MUST be equal to number of rows!"
        N = len(rows)
        
        
        #  Find the squares/bounding boxes identified by the points
        self.squares = []

        for r in range(len(rows)-1):
            row1 = rows[r]
            row2 = rows[r+1]

            # print(r, rows[r])
            # print(r+1, rows[r+1])
            # print("-"*100)
            
            for col in range( N-1 ):
                square = (row1[col] , row1[col+1], row2[col] , row2[col+1] )
                self.squares.append(square)
        


def __main__():

    import os
    import sys
    import cv2
    from edge_detector import detect_edges
    from line_detector import LineDetector

    """
    Unit test.
    """

    try:
        path = sys.argv[1]
    except:
        path = os.path.join(".", "images", "sudoku3.png")
    
    # load the image
    img = cv2.imread(path)

    #Find edge-points
    edges = detect_edges(img)

    #Find lines from points
    my_line_detector = LineDetector(edges)

    #Find the points of intersection of the grid lines
    intersection_pts = my_line_detector.intersections()

    # Find the squares/bounding-boxes
    squares = SquareDetector(intersection_pts).squares

    #print(f"Found {len(squares)} squares.")


    


if __name__ == "__main__":
    __main__()







