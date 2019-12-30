'''
    Change to use HoG or if any GPU available, DNN.
'''


import pandas as pd
import numpy as np
import cv2

df_filepath='./portrait_itep.csv'
outfile='./3x4_faces'

df = pd.read_csv(df_filepath)
rects = []

for file in df['PortraitFilepath']:
    print('processing file {}...'.format(file), end='')
    # Load image
    img = cv2.imread(file)

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the classifier
    haar_cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')
    
    # Get the biggest rectangle
    faces = haar_cascade_face.detectMultiScale(img_gray)
    #faces = haar_cascade_face.detectMultiScale(img_gray, cv2.CASCADE_FIND_BIGGEST_OBJECT)

    print('Detected {} faces.'.format(len(faces)))
    
    # Get only the first one just to play safe
    if len(faces) > 0:
        rects.append(faces[0])
    else:
        rects.append((None, None, None, None))


#print(list(zip(*rects)))
#for rect in list(zip(rects)):
#    print(rect)
print('filling new coordinates to the dataset...')
x, y, w, h = list(zip(*rects))
df['face_rect_x'] = x
df['face_rect_y'] = y
df['face_rect_w'] = h
df['face_rect_h'] = w

print('saving file...', end='')
df.to_csv(df_filepath)
print('done.')

