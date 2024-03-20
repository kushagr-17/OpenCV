import cv2 as cv

def render(img_rgb): 
    img_rgb = cv.imread(img_rgb) 
    img_rgb = cv.resize(img_rgb, (750,450)) 
    numDownSamples = 2  
    numBilateralFilters = 50
    img_color = img_rgb 

    for _ in range(numDownSamples): 
        img_color = cv.pyrDown(img_color) 
    for _ in range(numBilateralFilters): 
        img_color = cv.bilateralFilter(img_color,   9, 9, 7) 
    for _ in range(numDownSamples): 
        img_color = cv.pyrUp(img_color) 

    img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY) 
    img_blur = cv.medianBlur(img_gray, 3) 
    
    img_edge = cv.adaptiveThreshold(img_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 2) 

    (x,y,z) = img_color.shape 
    img_edge = cv.resize(img_edge,(y,x)) 
    img_edge = cv.cvtColor(img_edge, cv.COLOR_GRAY2RGB) 
    
    return cv.bitwise_and(img_color, img_edge) 


file_name = "" #path of photo goes here  
result = render(file_name) 

cv.imwrite("Cartoon_version.jpg", result) 
cv.imshow("Cartoon version", result) 
cv.waitKey(0) 
cv.destroyAllWindows()