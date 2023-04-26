
# 實驗先把background分離出來之後，比較前後兩個frame的mean difference

import cv2
import numpy as np

# Load the video file
cap = cv2.VideoCapture('InputVideo.mp4')

backSub = cv2.createBackgroundSubtractorMOG2()


prev_frame = None
prev_gray = None

# Loop through the frames and display them
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply the background subtractor to the grayscale image
    fgMask = backSub.apply(frame)

    # Invert the foreground mask to obtain the background
    bgMask = cv2.bitwise_not(fgMask)

    # Apply the background mask to the original image
    bgImg = cv2.bitwise_and(frame, frame, mask=bgMask)
    # print(cv2.mean(bgImg)[0], cv2.mean(bgImg)[1], cv2.mean(bgImg)[2])
    if prev_frame is not None:
        frame_diff = cv2.absdiff(bgImg, prev_frame)
        
        th = 15
        if cv2.mean(frame_diff)[0] > th and cv2.mean(frame_diff)[1] > th and cv2.mean(frame_diff)[2] > th:
            print("scene change! at %s"%cap.get(cv2.CAP_PROP_POS_FRAMES)) 
            print("mean diff in each channel are: R: %.1f G: %.1f B: %.1f" %(cv2.mean(frame_diff)[2], cv2.mean(frame_diff)[1], cv2.mean(frame_diff)[0]))
    # Display the frame
    cv2.imshow('FG Mask', bgImg)
    # Exit if the user presses the 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    prev_frame = bgImg

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
