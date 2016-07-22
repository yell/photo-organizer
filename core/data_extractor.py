#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import plac
import numpy as np
import matplotlib.pyplot as plt
import caffe
import cv2

from repository import Repository


def main(imgs_path, deploy_path, weights_path, blob_name="pool5/7x7_s1", shape=(3, 224, 224), mean_values=(104, 117, 123)):	
	channels, rows, cols = shape

	net = caffe.Net(deploy_path, weights_path, caffe.TEST)
	net.blobs['data'].reshape(1, channels, rows, cols)

	repo = Repository()
	for directory, dirnames, filenames in os.walk(imgs_path):
		for i, img_path in enumerate(sorted(filenames)):

			# image = caffe.io.load_image(img_path)
			image = cv2.imread(img_path)
			image = cv2.resize(image, (rows, cols))
			image = image.swapaxes(0,2).swapaxes(1,2)
			image = image.reshape(1, channels, rows, cols)
			input_img = image.astype(float)
			for channel in xrange(len(channels)):
				input_img[:,channel,:,:] -= mean_values[channel]
			net.blobs["data"].data[...] = input_img
			probs = net.forward()['prob'].flatten()
			feats = net.blobs[blob_name].data

			repo.store(os.path.join(imgs_path, img_path), probs, feats)
			print "{0} of {1} done".format(i, len(filenames))


if __name__ == '__main__':
	plac.call(main)