import distances
import processor
import numpy as np
import os

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
        distances.all_distances(img_path, directory + photos[i], save_path, dist)
