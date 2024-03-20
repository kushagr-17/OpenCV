# OpenCV
Cartoonification of image
1. Importing necessary Modules
	cv2 : to use openCV for image processing
	time : for displaying FPS

2. Reading and Rescaling the Image
	cv2.imread() is used to store images in the form of numbers
	cv2.resize() is used to resize the image according to our desired dimension

3. Downsampling the Image
	Down-sampling reduces the image which makes it smaller and faster to process
	cv2.pyrDown() is used for the same

4. Applying Bilateral filtering
	This method smoothens the image while preserving the edges
	cv2.bilateralFilter() is used for the same

5. Up-sampling the Image
	Increases the image size
	cv2.pyrUp() used for the necessary

6. Converting to grayscale and Applying Median Blur
	Grayscaling simplifies the algorithm and reduces computational requirements
	cv2.cvtColor() is used
	Median blur is used to reduce noise and create a smoother appearance
	cv2.medianBlur() is used for the above

7. Creating an edge mask
	In this step, adaptive thresholding is applied to the blurred grayscale image which helps in creating edge mask 
	that separates edges from other regions.
	cv2.adaptiveThreshold() is used in order to create the mask

8. Processing the edge mask
	First, the size of the edge mask is resized to match the dimensions of image after up-sampling using cv2.resize()
	Then the edge mask is then converted to RGB format using cv2.cvtColor()

9. Displaying the result
	The cartoonified image is obtained by performing a bitwise AND operation between the color image and the edge mask
	using cv2.bitwise_and()
	This operation blends the two images, making the edges stand out while maintaining the color information

10. Storing the result file	
	cv2.imwrite() is used to store the cartoonified image in our system
	cv2.imshow() is used to display the result in a separate window

*For real-time capturing
	cv2.VideoCapture(0) is used to capture video frame-by-frame through our in-built webcam. "0" typically represents the default 
	camera
	.read() captures a single frame from the webcam and returns two values : ret and frame
		ret : a boolean variable that returns true if the frame is available
		frame : the captured frame
	cv2.putText() is used to display the FPS of the rendering at the top left corner
	cv2.imshow() is used to display the cartoonified frame in a separate window
	cv2.waitKey(1) & 0XFF==27 checks for a key event and if the key pressed has ASCII value 27 (esc key) the loop is exited
	.release() is used to release the webcam and free up resources
	cv2.destroyAllWindows() closes all openCV windows 

# How to Run the code
	In your python compiler (preferably VS Code) ensure to give the path of your target photo in the "file_name" variable
	For example, if the photo is in "Photos" folder with the name "test.jpg" 
		file_name = "Photos/test.jpg"
	Then in your terminal, write "python <file-name>.py" to run the python file and get your desired cartoonified image.

	For real-time capturing, ensure that your webcam is not blocked and write "python <file-name>.py" in your terminal 
	and get real-time cartoonified result.
