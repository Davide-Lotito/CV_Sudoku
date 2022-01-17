import os
import sys
import math

from digit_detection import *
from edge_detector import detect_edges
from line_detector import LineDetector
from square_detector import SquareDetector
from image_cropper import ImageCropper


def __main__():
    
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
    for im in cropped:
        d = image_to_digit(im)    
        print(d)
        digits.append(d)

    print(digits)

    #Show results
    print(f"found {len(cropped)} sudoku squares")

    for crp in cropped:
        try:
            cv2.imshow("", crp)
            cv2.waitKey(0) # press 0 to show next
        except:
           pass



if __name__ == "__main__":
    __main__()




