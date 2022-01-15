slope = lambda line :  (line[0][3]- line[0][1]) /  (line[0][2]-line[0][0]) 
yintercept = lambda line : line[0][1] - slope(line)*line[0][0]
area_square = lambda square : (square[3][1]-square[0][1])*(square[3][0]-square[0][0])

# intersection_x = lambda line_one, line_two : (yintercept(line_one) - yintercept(line_two) ) / (slope(line_two)-slope(line_one))    
# intersection = lambda line_one, line_two : (intersection_x(line_one, line_two), slope(line_one)*intersection_x(line_one, line_two) + yintercept(line_one)  )
# point_distance = lambda point_one, point_two : ((point_one[0] -  point_two[0])**2 +  (point_one[1] -  point_two[1])**2 )**0.5











