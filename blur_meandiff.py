
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

    blur = cv2.blur(frame, (5, 5))
    # print(cv2.mean(blur)[0], cv2.mean(blur)[1], cv2.mean(blur)[2])
    if prev_frame is not None:
        frame_diff = cv2.absdiff(blur, prev_frame)
        
        th = 15
        if cv2.mean(frame_diff)[0] > th and cv2.mean(frame_diff)[1] > th and cv2.mean(frame_diff)[2] > th:
            print("scene change! at %s"%cap.get(cv2.CAP_PROP_POS_FRAMES)) 
            print("mean diff in each channel are: R: %.1f G: %.1f B: %.1f" %(cv2.mean(frame_diff)[2], cv2.mean(frame_diff)[1], cv2.mean(frame_diff)[0]))
    # Display the frame
    cv2.imshow('Frame', frame)
    # Exit if the user presses the 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    prev_frame = blur

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
