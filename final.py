
# 實驗先把background分離出來之後，比較前後兩個frame的mean difference

import cv2
import numpy as np
import math
from split_algorithm import get_splits


# Load the video file
cap = cv2.VideoCapture('InputVideo.mp4')

total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

sample_rate = max(int(total_frame * 2e-3), 1)

prev_frame = None
last_shot = 0

shot_frame_index = []
frames = [[],[]]

# Get the number of frames in the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop through the frames and display them
for i in range(num_frames):
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break


    frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES);

    if prev_frame is not None:

        frame_diff = cv2.absdiff(frame, prev_frame)
        
        th = 15

        if cv2.mean(frame_diff)[0] > th and cv2.mean(frame_diff)[1] > th and cv2.mean(frame_diff)[2] > th:
            if frame_num - last_shot > 20:
                shot_frame_index.append(frame_num)
                print("scene change! at %s"%(frame_num)) 
                print("mean diff in each channel are: R: %.1f G: %.1f B: %.1f" %(cv2.mean(frame_diff)[2], cv2.mean(frame_diff)[1], cv2.mean(frame_diff)[0]))
            last_shot = frame_num

        (means, stds) = cv2.meanStdDev(frame)
        frame_v = np.concatenate([means, stds]).flatten()

        if frame_num % sample_rate == 0:
            frames[0].append(frame_v)
            frames[1].append(frame_num)

    prev_frame = frame
        

errors = []
choices = dict()


split_num = len(shot_frame_index)
split_points = get_splits(frames[0], split_num)
scenes = [(frames[1][x]) for x in split_points[0]]
print("The scenes are:, ", scenes)

for i in range(len(scenes)):
    for j in range(len(shot_frame_index)):
        if shot_frame_index[j] < scenes[i]:
            if j == len(shot_frame_index) - 1:
                scenes[i] = shot_frame_index[j]
            elif shot_frame_index[j + 1] > scenes[i]:
                if min((shot_frame_index[j + 1] - scenes[i]),(scenes[i] - shot_frame_index[j])) > 200:
                    break
                if scenes[i] - shot_frame_index[j] <= shot_frame_index[j + 1] - scenes[i]:
                    scenes[i] = shot_frame_index[j]
                else:
                    scenes[i] = shot_frame_index[j + 1]
print("After assign scene to shot, the scenes are:, ", scenes)
# Reset the video capture to the beginning of the video
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

while True:
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break


    frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES);
    
    for s in scenes:
        if frame_num == s:
            print("scene change")

    for s in shot_frame_index:
        if frame_num == s:
            print("shot change change at %f"%(frame_num))

    
    cv2.imshow('Video', frame)
    # Exit if the user presses the 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
