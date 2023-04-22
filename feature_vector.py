
# 實驗先把background分離出來之後，比較前後兩個frame的mean difference

import cv2
import numpy as np
import math

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

def find_split_points(arr, num_splits):
    # Convert array to numpy array
    arr = np.array(arr)
    
    # Compute the pairwise distances between vectors
    dist_matrix = np.linalg.norm(arr[:, np.newaxis] - arr, axis=2)
    
    # Initialize the cost and split arrays
    n = len(arr)
    cost = np.full((n, num_splits+1), np.inf)
    split = np.zeros((n, num_splits+1), dtype=int)
    
    # Compute the cost and split arrays using dynamic programming
    cost[:,0] = 0
    for k in range(1, num_splits+1):
        for i in range(k-1, n):
            for j in range(k-2, i):
                new_cost = cost[j, k-1] + np.sum(dist_matrix[j+1:i+1, j+1:i+1])
                if new_cost < cost[i,k]:
                    cost[i,k] = new_cost
                    split[i,k] = j+1
    
    # Backtrack through the split array to find the split points
    split_points = []
    i = n-1
    for k in range(num_splits, 0, -1):
        split_points.append(split[i,k])
        i = split[i,k]-1
    split_points.reverse()
    
    return split_points


# Load the video file
cap = cv2.VideoCapture('InputVideo.mp4')

backSub = cv2.createBackgroundSubtractorMOG2()


prev_frame = None
prev_gray = None
counter = 0
last_shot = 0

last_ten_frames = []
shot_frames_v = []

# Loop through the frames and display them
while cap.isOpened():
    counter += 1
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break

    frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES);
    

    if prev_frame is not None:

        (means, stds) = cv2.meanStdDev(frame)
        frame_v = np.concatenate([means, stds]).flatten()
        frame_hist = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        frame_hist = frame_hist.flatten()
        (means_prev, stds_prev) = cv2.meanStdDev(prev_frame)
        prev_frame_v = np.concatenate([means_prev, stds_prev]).flatten()
        prev_frame_hist = cv2.calcHist([prev_frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        prev_frame_hist = prev_frame_hist.flatten()
        cos_sim = cosine_similarity(frame_v, prev_frame_v)
        e_dist = euclidean_distance(frame_v, prev_frame_v)
        if e_dist > 20:
            if frame_num - last_shot > 20:
                shot_frames_v.append(frame_v)
                print("shot change dectected, the euclidean_distance is %.4f" %(e_dist))
                print(frame_v)
            last_shot = frame_num
        # if cos_sim <= 0.999:
        #     print("shot change dectected, the cosine similarity is %.4f" %(cos_sim))
        # print(frame_v)
    # Display the frame
    cv2.imshow('FG Mask', frame)
    # Exit if the user presses the 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    prev_frame = frame

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
