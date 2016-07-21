import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import caffe
import cv2
import csv

def compute_probs(img_path):
    #path to model struct
    model_config = '/home/anton/prj/photo_organizer/models/googlenet/deploy.prototxt'
    #path to caffemodel
    model_weights = '/home/anton/prj/photo_organizer/models/googlenet/_iter_4500.caffemodel'
    caffe.set_mode_gpu()
    net = caffe.Net(model_config, model_weights, caffe.TEST)

    #path to labels names
    labels_file = '/home/anton/Downloads/labels.txt'
    labels = np.loadtxt(labels_file, str, delimiter='\t')
    labels = labels.tolist()
    for i in range(20):
        labels[i] = labels[i].split()

    for i in range(len(file_list)):
        image = caffe.io.load_image(img_path)
        image = cv2.resize(image, (224,224))
        image = image.swapaxes(0,2).swapaxes(1,2)
        image = image.reshape(1, 3, 224, 224)
        net.blobs["data"].data[...] = image
        probs = net.forward()['prob'].flatten()
        probs = list(zip(labels, compute_probs(img_path)))
        prediction.sort(key = lambda t: -t[1])

    return probs
