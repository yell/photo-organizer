#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import numpy as np
import plac
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from nlp import identify_class, get_labels
from repository import Repository


def safe_mkdir(dirpath):
	try:
	    os.stat(dirpath)
	except:
	    os.mkdir(dirpath)

def clear_dir(dirpath):
    files = os.listdir(dirpath)
    if len(files) != 0:
        shutil.rmtree(dirpath)
       	safe_mkdir(dirpath)

def search_by_class(query, imgs_path='./', csv_path='data.csv', destination_path='./search_result/'):
    num_classes, labels = (14, get_labels('mpii')) if csv_path == 'data.csv' else (1000, get_labels('imagenet'))
    repo = Repository(csv_path, num_classes=num_classes)
    print num_classes
    print "Your input is '{0}'".format(query)
    class_name = identify_class(query, labels)
    print "[ Searching for category '{0}' ... ]".format(class_name)
    retrieved = []
    for img_path, probs, _ in repo:
    	img_path = os.path.join(imgs_path, img_path)
        probs = list(zip(probs, get_labels()))
        probs.sort()
        if probs[-1][1] == class_name:
        	retrieved.append((img_path, probs[-1][0]))
    retrieved.sort(key=lambda t: -t[1])
    print "Found {0} images".format(len(retrieved))
    safe_mkdir(destination_path)
    clear_dir(destination_path)
    print "Copying images to {0} ...".format(destination_path)
    for img_path, prob in retrieved:
    	shutil.copyfile(img_path, os.path.join(destination_path, "{0:.3f}_{1}".format(prob, img_path.split('/')[-1])))
    return retrieved
    print "Done!"

def main(imgs_path='./', csv_path='data.csv', destination_path='./search_result/'):
	count = 0
	plt.ion()
	while True:
		count += 1
		sys.stdout.write("Search: ")
		query = raw_input()
		if not query:
			break

		if count > 1:
			plt.close(f)

		retrieved = search_by_class(query, imgs_path=imgs_path, csv_path=csv_path, destination_path=destination_path)
		if not retrieved:
			print "No images found\n\n\n"
			continue
		n = min(5, len(retrieved))
		f, axarr = plt.subplots(1, n)
		for i in xrange(n):
			axarr[i].imshow(mpimg.imread(retrieved[i][0]))
			axarr[i].set_title(str(retrieved[i][1]))
		plt.draw()

		print '\n' * 3
		

if __name__ == '__main__':
	plac.call(main)