#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import numpy as np
import plac

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

def search_by_class(query, csv_path='data.csv', destination_path='./search_result/'):
    repo = Repository(csv_path)
    class_name = identify_class(query)
    retrieved = []
    print "Searching for category '{0}' ...".format(class_name)
    for img_path, probs, _ in repo:
        probs = list(zip(probs, get_labels()))
        probs.sort()
        if probs[-1][1] == class_name:
        	retrieved.append((img_path, probs[-1][0]))
    retrieved.sort(key=lambda t: -t[1])
    print "Found {0} images".format(len(retrieved))
    safe_mkdir(destination_path)
    clear_dir(destination_path)
    print "Moving found images to {0} ...".format(destination_path)
    for img_path, prob in retrieved:
    	shutil.copyfile(img_path, os.path.join(destination_path, "{0:.3f}_{1}".format(prob, img_path.split('/')[-1])))
    print "Done!"


if __name__ == '__main__':
	plac.call(search_by_class)