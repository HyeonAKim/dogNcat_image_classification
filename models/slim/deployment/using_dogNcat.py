from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os
import random
import sys

import numpy as np
import tensorflow as tf
from nets import inception
from datasets import dogNcat
from datasets import load_dogNcat
from datasets import imagenet
from datasets import dataset_utils

import os
import urllib2
import matplotlib
#%matplotlib inline
#import matplotlib.pyplot as plt

from datasets import imagenet
from nets import inception
from preprocessing import inception_preprocessing

slim = tf.contrib.slim
image_size = inception.inception_v1.default_image_size

dogNcat_data_dir = '/root/data/dogNcat'
train_dir = '/root/inception_model/inception_dogNcat/'

def run(image_url):
    with tf.Graph().as_default():
        tf.logging.set_verbosity(tf.logging.INFO)

        url = image_url
        image_string = urllib2.urlopen(url).read()
        image = tf.image.decode_jpeg(image_string, channels=3)
        processed_image = inception_preprocessing.preprocess_image(image, image_size, image_size, is_training=False)
        processed_images  = tf.expand_dims(processed_image, 0)


        # Create the model, use the default arg scope to configure the batch norm parameters.
        with slim.arg_scope(inception.inception_v1_arg_scope()):
            logits, _ = inception.inception_v1(processed_images, num_classes=2, is_training=False)

        probabilities = tf.nn.softmax(logits)

        checkpoint_path = tf.train.latest_checkpoint(train_dir)
        init_fn = slim.assign_from_checkpoint_fn(
          checkpoint_path,
          slim.get_variables_to_restore())

        with tf.Session() as sess:
            sess.run(tf.initialize_local_variables())
            init_fn(sess)
            np_image, probabilities = sess.run([image, probabilities])
            probabilities = probabilities[0, 0:]
            sorted_inds = [i[0] for i in sorted(enumerate(-probabilities), key=lambda x:x[1])]

    #    plt.figure()
    #    plt.imshow(np_image.astype(np.uint8))
    #    plt.axis('off')
    #    plt.show()

        names = dataset_utils.read_label_file(dogNcat_data_dir)

        for i in range(2):
            index = sorted_inds[i]
            # Shift the index of a class name by one.
            print('Probability %0.2f%% => [%s]' % (probabilities[index] * 100, names[index]))
