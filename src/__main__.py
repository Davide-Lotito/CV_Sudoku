import os
import sys
import math
import warnings 

from digit_detection import *
from edge_detector import detect_edges
from line_detector import LineDetector
from square_detector import SquareDetector
from image_cropper import ImageCropper
import numpy as np
from tabulate import tabulate 
from tqdm import tqdm

def __main__():

    warnings.filterwarnings("ignore")

    """
    Run the program.
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

    # Crop the original image by each square/bounding box
    cropped = ImageCropper(img, squares).cropped


   # Detect the digits
    digits = []
    for im in tqdm(cropped):
        d = image_to_digit(im)    
        digits.append(d)

    # convert to an np array, reshape, transpose, convert to table and pretty-print
    digits = np.reshape(np.asanyarray(digits), (9, 9)).transpose()
    table = tabulate(digits, [], tablefmt="fancy_grid")
    print(table)
    


if __name__ == "__main__":
    __main__()




