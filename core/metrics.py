import numpy
import sklearn
import scipy
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import pylab

def distance(u, v, p=1, metric_index=0):
    return {
        0: sklearn.metrics.mean_squared_error(u, v),
        1: sklearn.metrics.median_absolute_error(u, v),
        2: sklearn.metrics.mean_absolute_error(u, v),
        3: sklearn.metrics.r2_score(u, v),
        4: sklearn.metrics.explained_variance_score(u, v),
        5: scipy.braycurtis(u, v),
        6: scipy.canberra(u, v),
        7: scipy.chebyshev(u, v),
        8: scipy.cityblock(u, v),
        9: scipy.cosine(u, v),
        10: scipy.hamming(u, v),
        11: scipy.spatial.distance.mahalanobis(u, v, numpy.linalg.inv(numpy.ma.cov(u, v))),
        12: scipy.minkowski(u, v, p),
        13: scipy.sqeuclidean(u, v)

    }[metric_index]

def all_distances(image, p=1, metric_index=0):

    image1 = ''
    image2 = ''

    img1 = cv2.imread(image1)
    pylab.subplot (2, 1, 1)
    pylab.imshow(img1)
    pylab.title ('Original')

    img2 = cv2.imread(image2)
    pylab.subplot (2, 1, 2)
    pylab.imshow(img2)
    pylab.title ('Similar')

    pylab.figtext(0.3,0.02, '0.25346324', fontsize=28)

    #pylab.show()

    plt.savefig('')

all_distances('asd')
