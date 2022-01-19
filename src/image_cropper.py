import numpy as np


class ImageCropper:
    
    def __init__(self, img, squares):

        self.cropped = []
        
        for square in squares:
            x1 = square[0][0]
            y1 = square[0][1]
    
            x2 = square[3][0] 
            y2 = square[3][1] 

            crop_img = img[y1:y2, x1:x2] # from pixel y to y+h. And from pixel x to x+w

            self.cropped.append(crop_img)



def __main__():

    import os
    import sys
    import cv2
    from edge_detector import detect_edges
    from line_detector import LineDetector
    from square_detector import SquareDetector

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

    # CROP THE IMAGE BY THE BOUNDING BOXES
    cropped = ImageCropper(img, squares).cropped

    #Show results
    for crp in cropped:
        try:
            cv2.imshow("", crp)
            cv2.waitKey(0) # press 0 to show next
        except:
           pass



if __name__ == "__main__":
    __main__()

