import cv2
import numpy as np
import skimage

fileName = "InputVideo.rgb"
chunk_size = 1  # Define the size of each chunk in bytes

frames = []
channel_r = []
channel_g = []
channel_b = []
width = 270
height = 480
frame_size = width * height * 3
readCount = 10000
count = 0
prev_frame = None

# Read the binary file in chunks
with open(fileName, 'rb') as file:
    while True:
        count += 1
        frame = [[[0 for i in range(3)] for w in range(height)] for h in range(width)]
        for i in range(width):
            for j in range(height):
                chunk = file.read(chunk_size)
                if not chunk:  # If the chunk is empty, we've reached the end of the file
                    break
                frame[i][j][2] = (int.from_bytes(chunk, 'big'))
                chunk = file.read(chunk_size)
                if not chunk:  # If the chunk is empty, we've reached the end of the file
                    break
                frame[i][j][1] = (int.from_bytes(chunk, 'big'))
                chunk = file.read(chunk_size)
                if not chunk:  # If the chunk is empty, we've reached the end of the file
                    break
                # Process the chunk (e.g., print, store or manipulate the data as needed)
                frame[i][j][0] = int.from_bytes(chunk, "big")
        frame = np.asarray(frame, dtype="uint8")
        if prev_frame is not None:
            simlarityIndex = skimage.metrics.structural_similarity(frame, prev_frame, channel_axis = 2)
            if simlarityIndex < 0.6:
                print("shot change at frame: ", count)
        prev_frame = frame
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or frame is None:
            cv2.destroyAllWindows()
            break
        cv2.imshow('frame',frame)
