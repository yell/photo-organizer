import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import caffe
import cv2

def feats(img_path, deploy_path, weights_path):
    channels = 3
    rows = 224
    cols = 224

    net = caffe.Net(deploy_path, weights_path, caffe.TEST)
    net.blobs['data'].reshape(1, channels, rows, cols)

    image = caffe.io.load_image(img_path)
    image = cv2.resize(image, (224, 224))
    image = image.swapaxes(0,2).swapaxes(1,2)
    image = image.reshape(1, channels, rows, cols)
    input_img = image.astype(float)
    net.blobs["data"].data[...] = input_img
    probs = net.forward()['prob'].flatten()
    feats = net.blobs["pool5/7x7_s1"].data

    return([elem[0][0] for elem in feats[0].tolist()])

def probs(img_path, deploy_path, weights_path):
    channels = 3
    rows = 224
    cols = 224

    net = caffe.Net(deploy_path, weights_path, caffe.TEST)
    net.blobs['data'].reshape(1, channels, rows, cols)

    image = caffe.io.load_image(img_path)
    image = cv2.resize(image, (224,224))
    image = image.swapaxes(0,2).swapaxes(1,2)
    image = image.reshape(1, channels, rows, cols)
    input_img = image.astype(float)
    net.blobs["data"].data[...] = input_img
    probs = net.forward()['prob'].flatten()

    return list(probs)
