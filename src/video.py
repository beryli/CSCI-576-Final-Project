# 實驗先把background分離出來之後，比較前後兩個frame的mean difference
import sys
import cv2
import numpy as np
import math
from .split_algorithm import get_splits
from .frame import Frametype

# Analyzes the input video @filename, plot a cluster chart if @plot flag is true,
# and returns a tuple list of frame IDs and frame types
#
# @filename:
#       The name of the input video (AVI file)
# @plot:
#       Plots a cluster chart is @plot is true
#
# Return Value:
#       Returns a tuple list of frames.
#
#       Data type: [(frame-id-1, frame-type-1), (frame-id-2, frame-type-2), ...]
#
#       `frame-type` is defined in `frame.py` and types can be retrieved by
#       bitwise-ANDing with one of the three frame types, `Frametype.SCENE`,
#       `Frametype.SHOT`, and `Frametype.SUBSHOT`.
#
#       For example, if `frame-type-1 & Frame.SHOT` is not zero, then `frame-type-1`
#       is a shot. Note that a single frame can have multiple properties at the same time.
def analyze_video(filename, subdiv_x=6, subdiv_y=6, plot=False):
    def merge_frame_types(scene_ids, shot_ids, subshot_ids):
        d = dict()
        for id in [int(x) for x in shot_ids]:
            d[id] = Frametype.SHOT

        for id in [int(x) for x in scene_ids]:
            if id not in d:
                d[id] = Frametype.SCENE
            else:
                d[id] |= Frametype.SCENE

        for id in [int(x) for x in subshot_ids]:
            if id not in d:
                d[id] = Frametype.SUBSHOT
            else:
                d[id] |= Frametype.SUBSHOT

        frames = []
        for key, value in d.items():
            frames.append([key, value])

        frames.sort(key=lambda x: x[0])

        return frames
    
    """
    Divides @frame and @prev_frame into blocks (subdivisions) and calculates the mean of difference of each channel in a block
    Counts the number of blocks where the means of differences of a channel >= @th_subdiv
    If the proportion of the changed blocks >= @th, then @frame is a subshot (returns True)
    """
    def is_subshot(frame, prev_frame, subdiv_x=8, subdiv_y=8, th=0.4, th_subdiv=10, th_must_change=15, blur=False, ksize=(5, 5)):
        h, w, channels = frame.shape[0], frame.shape[1], frame.shape[2]
        subdiv_w = (w + subdiv_x - 1) // subdiv_x
        subdiv_h = (h + subdiv_y - 1) // subdiv_y

        # Padding with 0-s
        padded_w, padded_h = subdiv_w * subdiv_x, subdiv_h * subdiv_y
        frame_padded = np.zeros(shape=(padded_h, padded_w, channels))
        prev_frame_padded = np.zeros(shape=(padded_h, padded_w, channels))
        frame_padded[:h,:w,:] = cv2.blur(frame, ksize) if blur else frame
        prev_frame_padded[:h,:w,:] = cv2.blur(prev_frame, ksize) if blur else prev_frame

        max_diff = 0.0
        block_change_count = 0
        for i in range(subdiv_x):
            for j in range(subdiv_y):
                x_begin, y_begin = subdiv_w * i, subdiv_h * j
                x_end, y_end = x_begin + subdiv_w, y_begin + subdiv_h
                block = frame_padded[y_begin:y_end, x_begin:x_end]
                prev_block = prev_frame_padded[y_begin:y_end, x_begin:x_end]

                means = cv2.mean(block)
                prev_means = cv2.mean(prev_block)

                frame_diff = cv2.absdiff(means, prev_means)
                if frame_diff[0] > th_subdiv or frame_diff[1] > th_subdiv or frame_diff[2] > th_subdiv:
                    max_diff = max(max_diff, frame_diff[0], frame_diff[1], frame_diff[2])
                    block_change_count += 1

        total_blocks = subdiv_x * subdiv_y
        diff_ratio = block_change_count / total_blocks

        # if diff_ratio >= th:
            # print('diff_ratio %f' % diff_ratio)

        # if max_diff > 1.0:
            # print('frame %d: max diff %f\n' % (frameid, max_diff))

        return True if diff_ratio >= th or max_diff > th_must_change else False

    # Load the video file
    cap = cv2.VideoCapture(filename)

    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    sample_rate = max(int(total_frame * 2e-3), 1)

    # Get the number of frames in the video
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    ret, frame = cap.read()
    if not ret:
        sys.exit()
    
    frame_h = frame.shape[0]
    frame_w = frame.shape[1]
    channels = frame.shape[2]

    prev_frame = 0
    last_shot = 0
    shot_frame_index = [0]

    (means, stds) = cv2.meanStdDev(frame)
    frame_v = np.concatenate([means, stds]).flatten()
    frames = [[],[]]
    frames[0].append(frame_v)
    frames[1].append(0)

    subshot_frame_index = [0]
    last_subshot = 0
    subshot_min_len = 20
    
    bufsize = 4
    frame_buf = np.empty((bufsize, frame_h, frame_w, channels))

    # Loop through the frames and display them
    for i in range(1, num_frames):
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break

        frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES)) - 1
        # print('frame %d' % frame_num)

        frame_diff = cv2.absdiff(frame, prev_frame)

        th = 15

        if cv2.mean(frame_diff)[0] > th and cv2.mean(frame_diff)[1] > th and cv2.mean(frame_diff)[2] > th:
            if frame_num - last_shot > 20:
                subshot_count = 0
                j = len(subshot_frame_index) - 1
                while j >= 0 and subshot_frame_index[j] >= shot_frame_index[-1]:
                    subshot_count += 1
                    j -= 1

                # Deletes subshot if there is only one within a shot
                if subshot_count == 1:
                    subshot_frame_index.pop()
                
                shot_frame_index.append(frame_num)
                print('shot: %d' % frame_num)
                # print("scene change! at %s"%(frame_num))
                # print("mean diff in each channel are: R: %.1f G: %.1f B: %.1f" %(cv2.mean(frame_diff)[2], cv2.mean(frame_diff)[1], cv2.mean(frame_diff)[0]))
            last_shot = frame_num

        (means, stds) = cv2.meanStdDev(frame)
        frame_v = np.concatenate([means, stds]).flatten()

        if frame_num % sample_rate == 0:
            frames[0].append(frame_v)
            frames[1].append(frame_num)

        curr_buf_idx = frame_num % bufsize
        frame_buf[curr_buf_idx] = frame

        if frame_num >= bufsize:
            prev_buf_idx = (frame_num - (bufsize - 1)) % bufsize
            if is_subshot(frame_buf[curr_buf_idx], frame_buf[prev_buf_idx], subdiv_x=subdiv_x, subdiv_y=subdiv_y, th=0.5, th_subdiv=15, th_must_change=20):
                if frame_num - last_subshot >= subshot_min_len:
                    if last_subshot < shot_frame_index[-1]:
                        subshot_frame_index.append(shot_frame_index[-1])
                        print(" |-- subshot: %d" % subshot_frame_index[-1])
                        if frame_num - shot_frame_index[-1] >= subshot_min_len:
                            subshot_frame_index.append(frame_num)
                            print(" |-- subshot: %d" % subshot_frame_index[-1])
                    else:
                        subshot_frame_index.append(frame_num)
                        print(" |-- subshot: %d" % subshot_frame_index[-1])

                    last_subshot = subshot_frame_index[-1]

        prev_frame = frame


    errors = []
    choices = dict()


    split_num = len(shot_frame_index)
    split_points = get_splits(frames[0], split_num, plot=plot)
    scenes = [(frames[1][x]) for x in split_points[0]]
    # print("The scenes are:, ", scenes)

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
    # print("After assign scene to shot, the scenes are:, ", scenes)
    cap.release()
    cv2.destroyAllWindows()

    frames = merge_frame_types(scenes, shot_frame_index, subshot_frame_index)

    return frames
