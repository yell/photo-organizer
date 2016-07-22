#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import plac
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from metrics import distance, mahalanobis
from repository import Repository


def main(img_path, imgs_path, metric=0, csv_path='data.csv'):
    repo = Repository(csv_path)
    feats_map = []
    for fpath, _, feats in repo:
        if fpath.split('/')[-1] == img_path.split('/')[-1]:
            source_feats = feats
        else:
            feats_map.append((fpath, feats))

    if metric.startswith('m'):
        dim = int(metric.split('_')[-1])
        all_feats = [feats[:dim] for _, feats in feats_map[:dim]]
        cov = np.cov(np.array(all_feats))
        VI = np.linalg.pinv(cov)
        distance_map = map(lambda (fpath, feats): (mahalanobis(feats[:dim], source_feats[:dim], VI), fpath), feats_map)
    else:
        metric = int(metric)
        distance_map = map(lambda (fpath, feats): (distance(feats, source_feats, metric), fpath), feats_map)

    distance_map.sort()

    f, axarr = plt.subplots(4, 5)
    axarr[0, 2].imshow(mpimg.imread(img_path))
    axarr[0, 2].set_title("Source image")
    for i in xrange(15):
        axarr[1 + i / 5, i % 5].imshow(mpimg.imread(os.path.join(imgs_path, distance_map[i][1])))
        axarr[1 + i / 5, i % 5].set_title("{0:.3f}".format(distance_map[i][0]))
    plt.show()
    plt.close(f)


if __name__ == '__main__':
    plac.call(main)