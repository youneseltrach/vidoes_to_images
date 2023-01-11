import cv2
import os
import glob

# videos path
path = "D:/DesktopP/trunk detection/videos"

# create a dir file
print ('create image_v1============================================================= ')
os.mkdir ('images/images_v1')

# Loop over the frames
index = 1

# iterate over videos
for file in glob.glob(path + '/*.mp4'):
    print('read file : ', file)
    # Open the video file
    video = cv2.VideoCapture(file)
    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    end_frame = total_frames

    # for  1s ,  CUZ we use 30FPS
    frame_interval = 30  
    # set the start of the frame
    start_frame = 0
    frame_index = start_frame

    while video.isOpened():
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = video.read()

        if not ret:
            print ('Error: Unread frame !')
            break
        
        print ('frame saved: ', frame_index)
        # Save
        cv2.imwrite('images/images_v{}/frame_{}.jpg'.format(index,frame_index), frame)
        # Increment the frame & index
        
        frame_index += frame_interval

        if frame_index > end_frame:
            index +=1
            print ('create image_v{}============================================================= '.format (index))
            os.mkdir ('images/images_v{}'.format(index))
    video.release()
    