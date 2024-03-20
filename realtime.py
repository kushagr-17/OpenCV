import cv2 as cv
import time

prev = 0 
curr = 0

def render(frame): 
        img_rgb = frame
        img_rgb = cv.resize(img_rgb, (700,400)) 
        numDownSamples = 2  
        numBilateralFilters = 50 
        img_color = img_rgb 

        for _ in range(numDownSamples): 
            img_color = cv.pyrDown(img_color) 
        for _ in range(numBilateralFilters): 
            img_color = cv.bilateralFilter(img_color, 9, 9, 7) 
        for _ in range(numDownSamples): 
            img_color = cv.pyrUp(img_color) 

        img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY) 
        img_blur = cv.medianBlur(img_gray, 3) 
        
        img_edge = cv.adaptiveThreshold(img_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 2) 
    
        (x,y,z) = img_color.shape 
        img_edge = cv.resize(img_edge,(y,x)) 
        img_edge = cv.cvtColor(img_edge, cv.COLOR_GRAY2RGB) 
        return cv.bitwise_and(img_color, img_edge) 
    
def main():
    global curr, prev
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        cartoon = render(frame)
        
        curr = time.time()
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        fps = 1/(curr - prev)
        prev = curr
        fps = int(fps)
        fps = str(fps)
        
        cv.putText(cartoon,fps,(10,70),font,3,(100,50,0),3,cv.LINE_AA)
        cv.imshow("Cartoonify",cartoon)
        
        if cv.waitKey(1) & 0xFF == 27:
            break
        
    cap.release()
    cv.destroyAllWindows()
    
if __name__ =="__main__":
    main()