import numpy as np
import matplotlib.pyplot as plt
import sys
import caffe

#path to image to classify
image = caffe.io.load_image('')
plt.imshow(image)

#path to caffe
caffe_root = ''

#path to model struct
model_def = caffe_root + ''
#path to caffemodel
model_weights = caffe_root + ''

caffe.set_mode_gpu()
net = caffe.Classifier(model_def, model_weights,
                       mean=np.load(caffe_root + 'path to mean image!!!').mean(1).mean(1), #path to mean image
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))

#path to labels names
labels_file = ''

labels = np.loadtxt(labels_file, str, delimiter='\t')

labels = labels.tolist()

for i in range(20):
    labels[i] = labels[i].split()

prediction = net.predict([image])
prediction = prediction[0].tolist()
prediction = list(zip(labels, prediction))

prediction.sort(key = lambda t: -t[1])
print prediction

print 'Top-5 most probable classes:'
for i in range(5):
    print i + 1, '-th | ', 'class number:', prediction[i][0][0], '| class name:', prediction[i][0][1], '| prob:', prediction[i][1]

plt.show()
