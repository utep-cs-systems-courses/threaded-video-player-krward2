#!/usr/bin/env python3

import cv2
import os
import sys

def extractFrames(outQueue = None, endOfVideo):
    print('Extract Frames starting.')

    # globals
    outputDir    = 'frames'
    clipFileName = 'clip.mp4'
    # initialize frame count
    count = 0

    # open the video clip
    vidcap = cv2.VideoCapture(clipFileName)

    # create the output directory if it doesn't exist
    if not os.path.exists(outputDir):
      print(f"Output directory {outputDir} didn't exist, creating")
      os.makedirs(outputDir)

    # read one frame
    success,image = vidcap.read()

    print(f'Reading frame {count} {success}')

    if not outQueue:
        while success and count < 72:

          # write the current frame out as a jpeg image
          cv2.imwrite(f"{outputDir}/frame_{count:04d}.bmp", image)

          success,image = vidcap.read()
          #print(f'Reading frame {count}')
          print('Success:', success, type(success), '| frame:', count)
          count += 1
    else:
        while success and count < 72:
          outQueue.enqueue(image)
          success,image = vidcap.read()
          count += 1
          #print('Success:', success, '| frame:', count)

        #End of stream signal for all 3 threads
        outQueue.enqueue(None)
    print('Extractor EXITING')
    sys.exit()
