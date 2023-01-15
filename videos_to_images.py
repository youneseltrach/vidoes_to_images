import cv2
import os
import glob
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

def videosToImages(pathvideos, pathsave, second):
    # videos path
    path = pathvideos

    # create a dir file
    print ('create image_v1======================================= ')
    # os.makedirs (str(pathsave)+'/images/images_v1')

    # Loop over the frames
    index = 1

    # iterate over videos
    totale_videos = len(glob.glob(path+'/*.mp4'))
    percent = 1
   
    for file in glob.glob(path + '/*.mp4'):
        # print('read file : ', file)
        # Open the video file

        percent
        # percent +=1
        # print(int(percent*100/totale_videos))
        # self.progressBar.setProperty("value", int(percent*100/totale_videos))

        video = cv2.VideoCapture(file)
        # Get the total number of frames in the video
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        end_frame = total_frames

        # for  1s ,  CUZ we use 30FPS
        fps = int(video.get(cv2.CAP_PROP_FPS))
        print(fps)
        frame_interval = fps*second
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
            cv2.imwrite('{}/images/images_v{}/frame_{}.jpg'.format(pathsave,index,frame_index), frame)
            # Increment the frame & index
            
            frame_index += frame_interval
            if frame_index > end_frame:
                index +=1
                print ('create image_v{}============================================================= '.format (index))
                os.makedirs ('{}/images/images_v{}'.format(pathsave,index))
        video.release()
    