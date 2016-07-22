import numpy as np
import os
import shutil

import processor
import nlp

def safe_mkdir(dirpath):
	try:
	    os.stat(dirpath)
	except:
	    os.mkdir(dirpath)

def contents_dir(dirpath):
    files = os.listdir(dirpath)
    if len(files) != 0:
        shutil.rmtree(dirpath)



def search_by_class(class_name, photos_path, photos_class_path, deploy_path, weights_path):
    photos = os.listdir(photos_path)
    class_prob = []
    photo_name = []
    for i in range(len(photos)):
        image = photos_path + photos[i]
        predict = processor.probs_feats(image, deploy_path, weights_path)[0]
        prediction = list(zip(predict, nlp.get_labels()))
        prediction.sort()
        prediction_rev = prediction[::-1]
        if prediction_rev[0][1] == class_name:
            class_prob.append(prediction_rev[0][0])
            photo_name.append(photos[i])

    prob_name = list(zip(class_prob, photo_name))
    if len(prob_name) > 1:
        prob_name = prob_name.sort(key=lambda t: -t[0])

    safe_mkdir(photos_class_path)
    contents_dir(photos_class_path)

    for j in range(len(prob_name)):
        shutil.copyfile(photos_path + prob_name[j][1], photos_class_path + prob_name[j][1])
