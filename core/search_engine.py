import numpy as np
import os

import processor
import nlp

class_name = ''

directory = '/home/anton/prj/photo_organizer/data/test/'
photos = os.listdir(directory)
for i in range(len(photos)):
    image = directory + photos[i]
    deploy_path = '/home/anton/prj/photo_organizer/models/googlenet/deploy.prototxt'
    weights_path = '/home/anton/prj/photo_organizer/models/googlenet/_iter_4500.caffemodel'
    predict = processor.probs(image, deploy_path, weights_path)
    prediction = list(zip(predict, nlp.get_labels()))
    prediction.sort()
    prediction_rev = prediction[::-1]
    
