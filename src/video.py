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
def analyze_video(filename, plot=False):
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


    # Load the video file
    cap = cv2.VideoCapture(filename)

    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    sample_rate = max(int(total_frame * 2e-3), 1)

    # Get the number of frames in the video
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    ret, frame = cap.read()
    if not ret:
        sys.exit()

    prev_frame = 0
    last_shot = 0
    shot_frame_index = [0]

    (means, stds) = cv2.meanStdDev(frame)
    frame_v = np.concatenate([means, stds]).flatten()
    frames = [[],[]]
    frames[0].append(frame_v)
    frames[1].append(0)


    # Loop through the frames and display them
    for i in range(1, num_frames):
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break

        frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES);

        frame_diff = cv2.absdiff(frame, prev_frame)

        th = 15

        if cv2.mean(frame_diff)[0] > th and cv2.mean(frame_diff)[1] > th and cv2.mean(frame_diff)[2] > th:
            if frame_num - last_shot > 20:
                shot_frame_index.append(frame_num)
                # print("scene change! at %s"%(frame_num))
                # print("mean diff in each channel are: R: %.1f G: %.1f B: %.1f" %(cv2.mean(frame_diff)[2], cv2.mean(frame_diff)[1], cv2.mean(frame_diff)[0]))
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

    frames = merge_frame_types(scenes, shot_frame_index, [])

    return frames
