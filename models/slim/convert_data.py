# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
r"""converts a particular dataset.

Usage:
```shell

$ python convert_data.py \
    --dataset_name=flowers_ha \
    --dataset_dir=/tmp/flowers

$ python convert_data.py \
    --dataset_name=dogNcat \
    --dataset_dir=/hyeona/data/dogNcat

```
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from datasets import convert_dogNcat
#from datasets import convert_flowers

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
  'dataset_name',
  None,
  'The name of the dataset to convert, one of "flowers", "dogNcat".')

tf.app.flags.DEFINE_string(
  'dataset_dir',
  None,
  'The directory where the output TFRecords and temporary files are saved.')


def main(_):
  if not FLAGS.dataset_name:
    raise ValueError('You must supply the dataset name with --dataset_name')
  if not FLAGS.dataset_dir:
    raise ValueError('You must supply the dataset directory with --dataset_dir')

  if FLAGS.dataset_name == 'flowers':
    convert_flowers.run(FLAGS.dataset_dir)
  elif FLAGS.dataset_name == 'dogNcat':
    convert_dogNcat.run(FLAGS.dataset_dir)
  else:
    raise ValueError('dataset_name [%s] was not recognized.' % FLAGS.dataset_dir)

if __name__ == '__main__':
  tf.app.run()
