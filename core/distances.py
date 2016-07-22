import numpy as np
import sklearn
from sklearn import metrics
import scipy
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import pylab

def distance(u, v, p=1, metric_index=0):
    assert len(u) == len(v)
    return {
        0: sklearn.metrics.mean_squared_error(u, v),
        1: sklearn.metrics.median_absolute_error(u, v),
        2: sklearn.metrics.mean_absolute_error(u, v),
        3: sklearn.metrics.r2_score(u, v),
        4: sklearn.metrics.explained_variance_score(u, v),
        5: scipy.spatial.distance.braycurtis(u, v),
        6: scipy.spatial.distance.canberra(u, v),
        7: scipy.spatial.distance.chebyshev(u, v),
        8: scipy.spatial.distance.cityblock(u, v),
        9: scipy.spatial.distance.cosine(u, v),
        10: scipy.spatial.distance.hamming(u, v),
        #11: scipy.spatial.distance.mahalanobis(u, v, np.linalg.pinv(np.ma.cov(u, v))),
        11: scipy.spatial.distance.minkowski(u, v, p),
        12: scipy.spatial.distance.sqeuclidean(u, v)

    }[metric_index]

def all_distances(img_path1, img_path2, save_path, dist):

    img1 = cv2.imread(img_path1)
    pylab.subplot (2, 1, 1)
    pylab.imshow(img1)
    pylab.title ('Original')

    img2 = cv2.imread(img_path2)
    pylab.subplot (2, 1, 2)
    pylab.imshow(img2)
    pylab.title ('Similar')

    pylab.figtext(0.3,0.02, str(dist), fontsize=28)

    plt.savefig(save_path + str(dist)[:10] + '.png')
    plt.close('all')
