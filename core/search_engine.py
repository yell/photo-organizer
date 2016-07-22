import processor
import numpy as np

image = '/home/anton/Downloads/003972915.jpg'
predict = processor.probs(image, '/home/anton/prj/caffe/models/bvlc_googlenet/deploy.prototxt', '/home/anton/prj/caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel')
labels_file = '/home/anton/Downloads/synset_words.txt'
labels = np.loadtxt(labels_file, str, delimiter='\t')

prediction = list(zip(predict, labels))

print prediction
