
# 先把frame轉gray scale在做比較

import cv2

def detect_scene_changes(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    # Initialize variables
    frames = []
    prev_frame = None
    prev_gray = None
    timestamps = []
    # Loop through all frames in the video
    while cap.isOpened():
        # Read the next frame
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
            cap.release()
            cv2.destroyAllWindows()
            break
    
        cv2.imshow('frame',frame)

        # Convert to grayscale for easier processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Compute the absolute difference between the current and previous frames
        if prev_gray is not None:
            frame_diff = cv2.absdiff(gray, prev_gray)
            th = 20
            if cv2.mean(frame_diff)[0] > th:
                print("scene change! at %s\n"%cap.get(cv2.CAP_PROP_POS_FRAMES)) 
            frames.append(frame_diff)

        # Update variables for next iteration
        prev_frame = frame
        prev_gray = gray
        timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))
    cap.release()
    # Compute the mean pixel value difference between adjacent frames
    mean_diffs = [cv2.mean(frame_diff)[0] for frame_diff in frames]
    # Find the indices where the mean pixel difference exceeds a threshold
    threshold = 10.0  # experiment with different values
    scene_changes = [i for i, diff in enumerate(mean_diffs) if diff > threshold]
    # Convert the indices to timestamps
    scene_change_timestamps = [timestamps[i] for i in scene_changes]
    return scene_change_timestamps

changes = detect_scene_changes("InputVideo.mp4")
print("end: changes = ", changes)
