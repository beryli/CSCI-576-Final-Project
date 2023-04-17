import cv2
import numpy as np
import skimage
print(skimage.__version__)

# 計算img1 和 img2 的 difference
def diff(img1, img2):
   h, w, c = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum((diff))
   return err

def avgDiff(img1, img2):
    h_diff = np.sum(img1[:,:,0] - img2[:,:, 0])
    s_diff = np.sum(img1[:,:,1] - img2[:,:, 1])
    v_diff = np.sum(img1[:,:,2] - img2[:,:, 2])
    return (h_diff + s_diff + v_diff) / 3000

cap = cv2.VideoCapture("InputVideo.mp4")
ret, frame = cap.read()
fps = cap.get(cv2.CAP_PROP_FPS)
h, w , c = frame.shape
last_mean = 0  
last_frame = None
count = 1
scene_frame = frame
while(1):
    # count第幾個Frame
    count += 1
    ret, frame = cap.read()
    frame_mean = frame.mean()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow('frame',frame)
    if last_frame is not None:
        prevHSVImg = cv2.cvtColor(last_frame, cv2.COLOR_BGR2HSV)
        HSVImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 用scructural similarity來判斷前後兩個Frame的差異，藉以偵測shot change
        simlarityIndex = skimage.metrics.structural_similarity(frame, last_frame, channel_axis = 2)
        if simlarityIndex < 0.6:
            print("shot change! ssim = " + str(simlarityIndex) + " at frame " + str(count))

        # 用average difference of H, S, and V channel
        # avg_diff = avgDiff(cv2.cvtColor(scene_frame, cv2.COLOR_BGR2HSV), HSVImg)
        # if avg_diff > 12000:
        #     scene_frame = frame
        #     scene_count = 0

        # 用MSE來比較前後兩個Frame
        mse = skimage.metrics.mean_squared_error(prevHSVImg, HSVImg)
        if mse > 2000:
            print("shot change! mse = " + str(mse) + " at frame " + str(count))
    last_frame = frame

