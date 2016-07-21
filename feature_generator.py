
# coding: utf-8

# In[ ]:

channels = 3
rows = 224
cols = 224


def feature_generator(img_file, model_deploy, model_weight):
    net = caffe.Net(model_deploy, model_weights, caffe.TEST)
    net.blobs['data'].reshape(1, channels, rows, cols)
    
    img = caffe.io.load_image(img_file)
    img = cv.resize(img, (224, 224)) 
    img = img.swapaxes(0,2).swapaxes(1,2)
    imgn = img.reshape(1, channels, rows, cols)
    input_img = imgn.astype(float)
    net.blobs["data"].data[...] = input_img
    prob = net.forward()['prob'].flatten()
    feat = net.blobs["pool5/7x7_s1"].data
    #return(feat)
    return([elem[0][0] for elem in feat[0].tolist()])
    

