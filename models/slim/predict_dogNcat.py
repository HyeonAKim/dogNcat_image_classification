r"""converts a particular dataset.

Usage:
```shell

$ python predict_dogNcat.py \
    --image_url='https://i.ytimg.com/vi/oqNKD9YVe4U/maxresdefault.jpg' \

```
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from deployment import using_dogNcat

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
  'image_url',
  None,
  'The image url that you want to preidict')

def main(_):
  if not FLAGS.image_url:
    raise ValueError('You must supply the image_url with --image_url')

  if FLAGS.image_url != '':
    using_dogNcat.run(FLAGS.image_url)
  else:
    raise ValueError('image_url [%s] was not recognized.' % FLAGS.image_url)

if __name__ == '__main__':
  tf.app.run()
