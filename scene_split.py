
# 實驗先把background分離出來之後，比較前後兩個frame的mean difference

import cv2
import numpy as np
import math
from split_algorithm import get_splits

def normalize_vector(vector):
    """Normalize a given vector to a unit vector."""
    norm = math.sqrt(sum(i**2 for i in vector))
    return [i / norm for i in vector]


def cosine_similarity(vector1, vector2):
    dot_product = sum(p*q for p,q in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum([(val)**2 for val in vector1]))
    magnitude2 = math.sqrt(sum([val**2 for val in vector2]))
    return dot_product / (magnitude1 * magnitude2)

def euclidean_distance(vector1, vector2):
    distance = 0
    for i in range(len(vector1)):
        distance += (vector1[i] - vector2[i]) ** 2
    return math.sqrt(distance)

# Load the video file
cap = cv2.VideoCapture('InputVideo.mp4')

total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

sample_rate = int(total_frame * 3e-3)

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

        (means, stds) = cv2.meanStdDev(frame)
        frame_v = np.concatenate([means, stds]).flatten()

        if frame_num % sample_rate == 0:
            frames[0].append(frame_v)
            frames[1].append(frame_num)

    
        frame_hist = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        frame_hist = frame_hist.flatten()
        (means_prev, stds_prev) = cv2.meanStdDev(prev_frame)
        prev_frame_v = np.concatenate([means_prev, stds_prev]).flatten()
        prev_frame_hist = cv2.calcHist([prev_frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        prev_frame_hist = prev_frame_hist.flatten()
        cos_sim = cosine_similarity(frame_hist, prev_frame_hist)
        e_dist_hist = euclidean_distance(frame_hist, prev_frame_hist)
        e_dist_v = euclidean_distance(frame_v, prev_frame_v)

        if ((e_dist_hist > 10000 and e_dist_v >= 10) or e_dist_v > 20):
            if frame_num - last_shot > 10:
                shot_frame_index.append(frame_num)
                print("shot change dectected, the euclidean_distance is (%.4f, %4f), and the frame index is %f" %(e_dist_hist, e_dist_v, frame_num))
            last_shot = frame_num
    prev_frame = frame

errors = []
choices = dict()


split_num = int(len(shot_frame_index)-1)
split_points = get_splits(frames[0], split_num)
scenes = [(frames[1][x]) for x in split_points[0]]
print("The scenes are:, ", scenes)

for i in range(len(scenes)):
    for j in range(len(shot_frame_index)):
        if shot_frame_index[j] < scenes[i]:
            if j == len(shot_frame_index) - 1:
                scenes[i] = shot_frame_index[j]
            elif shot_frame_index[j + 1] > scenes[i]:
                if (shot_frame_index[j + 1] - scenes[i]) > 200 and (scenes[i] - shot_frame_index[j]) > 200:
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
