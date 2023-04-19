
# 實驗先把background分離出來之後，使用ssim比較前後兩個frame背景的相似度

import cv2
import numpy as np
import skimage

# Load the video file
cap = cv2.VideoCapture('InputVideo.mp4')

backSub = cv2.createBackgroundSubtractorMOG2()


prev_bg = None
last_shot = 0

# Loop through the frames and display them
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply the background subtractor to the grayscale image
    fgMask = backSub.apply(gray)

    # Invert the foreground mask to obtain the background
    bgMask = cv2.bitwise_not(fgMask)

    # Apply the background mask to the original image
    bgImg = cv2.bitwise_and(frame, frame, mask=bgMask)

    if prev_bg is not None:
        frame_diff = cv2.absdiff(bgImg, prev_bg)
        
        th = 0.58
         # 用scructural similarity來判斷前後兩個Frame的差異，藉以偵測shot change
        simlarityIndex = skimage.metrics.structural_similarity(bgImg, prev_bg, channel_axis = 2)
        frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)
        if simlarityIndex < th :
            if frame_num - last_shot > 10:
                print("scene change! at %s" %(frame_num))
                print("the ssim is: %.4f" %(simlarityIndex))
            last_shot = frame_num
            
    # Display the frame
    cv2.imshow('Video', frame)
    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    prev_bg = bgImg

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
