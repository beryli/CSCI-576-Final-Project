
# 實驗先把background分離出來之後，比較前後兩個frame的mean difference

import cv2
import numpy as np

# Load the pre-trained model
# path to prototxt and model file
model = cv2.dnn.readNetFromCaffe("deploy_resnet152_places365.prototxt", "resnet152_places365.caffemodel")

# load the class label from txt file
file_name = 'categories_places365.txt'
classes = list()
with open(file_name) as class_file:
    for line in class_file:
        classes.append(line.strip().split(' ')[0][3:])
classes = tuple(classes)
# Define a function to classify an image
def classify_image(img):

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    blob = cv2.dnn.blobFromImage(image=rgb_img, size=(224, 224), mean=(cv2.mean(rgb_img)[0], cv2.mean(rgb_img)[1], cv2.mean(rgb_img)[2]))
    
    # set the input blob for the neural network
    model.setInput(blob)
    # forward pass image blog through the model
    # forward pass
    logit = model.forward()
    inx = np.argmax(logit)
    prob = np.max(logit)
    print('{:.3f} -> {}'.format(prob, classes[inx]))



# Load the video file
cap = cv2.VideoCapture('InputVideo.mp4')

backSub = cv2.createBackgroundSubtractorMOG2()


prev_frame = None
prev_gray = None

last_shot = 0

shot_frames = []

# Loop through the frames and display them
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break

    frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)


    blur = cv2.blur(frame, (5, 5))
    
    if prev_frame is not None:
        frame_diff = cv2.absdiff(blur, prev_frame)
        
        th = 15
        if cv2.mean(frame_diff)[0] > th and cv2.mean(frame_diff)[1] > th and cv2.mean(frame_diff)[2] > th:
            if frame_num - last_shot > 20:
                classify_image(img=frame)
                shot_frames.append((frame_num, frame))
                print("scene change! at %s"%(frame_num)) 
                print("mean diff in each channel are: R: %.1f G: %.1f B: %.1f" %(cv2.mean(frame_diff)[2], cv2.mean(frame_diff)[1], cv2.mean(frame_diff)[0]))
            last_shot = frame_num
    # Display the frame
    cv2.imshow('Frame', frame)
    # Exit if the user presses the 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    prev_frame = blur

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

# for img in shot_frames:
#     res = classify_image(img=img[1])
#     print('frame %d is classify as ', res)



