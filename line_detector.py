import cv2
import numpy as np
import math
from formulas import *
import os
import sys


class LineDetector:

    """
    Detects lines from a set of edges.
    Calculates the intersection-points between vertical and horizontal lines.
    """
    
    def __init__(self, edges):
        self.edges = edges
        rho = 1  # distance resolution in pixels of the Hough grid
        theta = np.pi / 180  # angular resolution in radians of the Hough grid
        threshold = 15  # minimum number of votes (intersections in Hough grid cell)
        min_line_length = 43  # minimum number of pixels making up a line
        max_line_gap = 10  # maximum gap in pixels between connectable line segments
        # Output "lines" is an array containing endpoints of detected line segments
        self.lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
        # separate vertical lines from horizontal lines
        self.vertical = []
        self.horizontal = []
        for line in self.lines:
            for x1,y1,x2,y2 in line:
                # TODO: add a margin of error! Not exactly 0 or 'exacatly inf'.
                if math.isinf(slope(line)):
                    self.vertical.append(line)
                elif slope(line) == 0:
                    self.horizontal.append(line)


        # TODO: refactor it! It's crappy        
        # consider parallel lines with similar distances to each other the same line


        # if distance between two parallel lines is greater than this, they're different lines
        MAGIC_NUMBER = 20

        # horizontal
        self.horizontal = sorted(self.horizontal, key=lambda e : e[0][1] )
        buffer = []
        for i in range(len(self.horizontal)-1):
            y_l1 = self.horizontal[i][0][1]
            y_l2 = self.horizontal[i+1][0][1]

            if(abs(y_l1-y_l2) > MAGIC_NUMBER):
                buffer.append(self.horizontal[i])
        
        # TODO: fix this!
        buffer.append(self.horizontal[-1])

        self.horizontal = buffer
                
        # vertical
        self.vertical = sorted(self.vertical, key=lambda e : e[0][0] )
        buffer = []
        for i in range(len(self.vertical)-1):
            x_l1 = self.vertical[i][0][0]
            x_l2 = self.vertical[i+1][0][0]

            if(abs(x_l1-x_l2) > MAGIC_NUMBER):
                buffer.append(self.vertical[i])
        
        # TODO: fix this!
        buffer.append(self.vertical[-1])
        self.vertical = buffer

    
    def intersections(self):
        intersection_pts = []
        
        for vert in self.vertical:
            for horz in self.horizontal:
                pt = (vert[0][0], horz[0][1])
                intersection_pts.append(pt)
        return intersection_pts
    


def __main__():

    """
    Unit test.
    """

    import edge_detector

    try:
        path = sys.argv[1]
    except:
        path = os.path.join(".", "images", "sudoku3.png")

    
    img = cv2.imread(path)
    line_image = np.copy(img) * 0  
    edges = edge_detector.detect_edges(img)
    line_det = LineDetector(edges)
    
    # plot vertical lines
    for vert in line_det.vertical:
        pt1 = (vert[0][0], vert[0][1])
        pt2 = (vert[0][2], vert[0][3])
        cv2.line(line_image,pt1,pt2, (0,0,255) ,1)
    
    # plot horizontal lines
    for horz in line_det.horizontal:
        pt1 = (horz[0][0], horz[0][1])
        pt2 = (horz[0][2], horz[0][3])
        cv2.line(line_image,pt1,pt2, (0,255,0) ,1)
    
    # plot the intersections between vertical and horizontal lines
    for pt in line_det.intersections():
        cv2.line(line_image,pt,pt, (255,0,0) ,2)

    cv2.imshow("Lines:", line_image)
    cv2.waitKey(0)



if __name__ == "__main__":
    __main__()










