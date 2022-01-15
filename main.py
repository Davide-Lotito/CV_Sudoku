import cv2
import numpy as np
import math

import itertools
import operator

from formulas import *

from digit_detection import *

# --------find edge-points-------------

# load the image
img = cv2.imread('./images/sudoku3.png')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# apply gaussian filter (to filter out 'high freq' noise)
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# apply the canny filter to find edges.
low_threshold = 110
high_threshold = 160
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)


#---------find lines from points----------------

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 15  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50  # minimum number of pixels making up a line
max_line_gap = 20  # maximum gap in pixels between connectable line segments
line_image = np.copy(img) * 0  # creating a blank image to draw lines on

# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# separate vertical lines from horizontal lines
vertical = []
horizontal = []

for line in lines:
    for x1,y1,x2,y2 in line:
        if math.isinf(slope(line)):
            vertical.append(line)
        elif slope(line) == 0:
            horizontal.append(line)

        cv2.line(line_image,(x1,y1),(x2,y2), (0,255,0) ,1)


#=---------find the points of intersection of the grid lines-------------

intersection_pts = []

for vert in vertical:
    for horz in horizontal:
        pt = (vert[0][0], horz[0][1])
        intersection_pts.append(pt)
        cv2.line(line_image,pt,pt, (0,0,255) ,10)


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


# filter out squares that are too small:
areas = [area_square(square) for square in squares]
mean_area = sum(areas)/len(areas)

squares = [square for square in squares if area_square(square) >= mean_area]


# ------------------- crop the original image by each square/bounding box------------------
cropped = []

for square in squares:
    x1 = square[0][0]
    y1 = square[0][1]
    
    x2 = square[3][0]
    y2 = square[3][1]

    crop_img = img[y1:y2, x1:x2] # from pixel y to y+h. And from pixel x to x+w
    
    cropped.append(crop_img)


# cv2.imshow("", line_image)
# cv2.waitKey(0)



# ------- detect the digits-------------
digits = []
for im in cropped:
    d = image_to_digit(im)    
    print(d)
    digits.append(d)



print(digits)



#------ show results--------------
print(f"found {len(cropped)} sudoku squares")


for crp in cropped:
    try:
        cv2.imshow("", crp)
        cv2.waitKey(0) # press 0 to show next
    except:
        pass    


