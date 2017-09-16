# Photo Organizer
This [project](http://cs.ucu.edu.ua/en/summerschool/project-photo-organizer/) 
was completed during the Lviv Data Science Summer School 2016. The project supervisor - 
[Olexandr Baiev](http://cs.ucu.edu.ua/course/deep-neural-networks-for-computer-vision/#lecturer). 
The project goal was to create a core for photo autotagging application using convolutional neural networks.

## Key features
* Automatic image tagging (by utilizing trained CNN model)
* Key-word searching
* Find similar photos for a given one.

Demo for the latter feature is presented below:
![1](https://github.com/monstaHD/photo_organizer/blob/master/imgs/similar_2.png)
For a given photo, 15 the most closest images were shown, almost all of which are turned out to be also tennis photos. 
Remarkably, that the first (most relevant) 3 photos are actually taken from the very same match as the source image is.

## How it was done
For this task we used the open [MPII Human Pose Dataset](http://human-pose.mpi-inf.mpg.de/), 
which contains over 25K images depicting 400 human activities. For the sake of simplicity and more balanced classes we've merged some of the classes and have ended up with 14 of them.

Next, we used the transfer learning technique by fine-tuning the weights of different models with the last (fully-connected) layer being replaced to handle new classes. 
The fine-tuning was done using Caffe in GPU-mode. The best results **7.5%** top-1 error (after the school we dropped the error to **5.0%** by using different optimization parameters) was achieved using GoogLeNet model for ImageNet dataset.
We also tried ResNet-50 and NetworkInNetwork.

For the key-word searching trivial model-less algorithm was used, by simply showing the images for the class, whose label is the closest to the input string. 
For this, Jaro-Winkler string similarity measure is used.

Finally, application is able to find similar images for a given one by computing distance between corresponding feature vectors computed by CNN model.
We tested around 15 different distance metrics, the most successful:
* Mean Squared Error
* Bray-Curtis dissimilarity measure
* Cosine distance

## Possible improvements
* Multiple tagging (perhaps by using several different networks)
* Improve the NLP part (use word2vec/glove models/google API/...)
* Try more network architectures
* Apply networks compression techniques (to ease the embedding into mobile devices, for instance)
