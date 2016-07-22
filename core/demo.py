import distances
import processor
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import pylab

def all_distances(img_path1, img_path2, save_path, dist):

    img1 = cv2.imread(img_path1)[:,:,::-1]
    pylab.subplot (2, 1, 1)
    pylab.imshow(img1)
    pylab.title ('Original')

    img2 = cv2.imread(img_path2)[:,:,::-1]
    pylab.subplot (2, 1, 2)
    pylab.imshow(img2)
    pylab.title ('Similar')

    pylab.figtext(0.3,0.02, str(dist), fontsize=28)

    plt.savefig(save_path + str(dist)[:10] + '.png')
    plt.close('all')


img_path = '/home/anton/Downloads/003972915.jpg'
feats_1 = processor.feats(img_path, '/home/anton/prj/photo_organizer/models/googlenet/deploy.prototxt', '/home/anton/prj/photo_organizer/models/googlenet/_iter_4500.caffemodel')
feat_1 = np.array(feats_1)
directory = '/home/anton/prj/photo_organizer/data/test/'
photos = os.listdir(directory)
for i in range(len(photos)):
    feats_2 = processor.feats(directory + photos[i], '/home/anton/prj/photo_organizer/models/googlenet/deploy.prototxt', '/home/anton/prj/photo_organizer/models/googlenet/_iter_4500.caffemodel')
    feat_2 = np.array(feats_2)
    for j in range(13):
        save_path = '/home/anton/Downloads/' + str(j) + '_metric/'
        dist = distances.distance(feat_1, feat_2, metric_index=j)
        all_distances(img_path, directory + photos[i], save_path, dist)
