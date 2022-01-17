


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




