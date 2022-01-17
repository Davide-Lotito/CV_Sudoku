import cv2
import sys
import os


def detect_edges(img):

    """
    Given an opencv matrix, detect the edge points 
    """

    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # apply gaussian filter (to filter out 'high freq' noise)
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
    
    # apply the canny filter to find edges.
    low_threshold = 110
    high_threshold = 160
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    return edges



def __main__():
    """
    Unit test.
    """
    
    try:
        path = sys.argv[1]
    except:
        path = os.path.join(".", "images", "sudoku3.png")
        

    img = cv2.imread(path)
    img = detect_edges(img)
    cv2.imshow("Edges:", img)
    cv2.waitKey(0)



if __name__ == "__main__":
    __main__()



