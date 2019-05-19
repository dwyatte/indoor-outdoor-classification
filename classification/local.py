import argparse
import tensorflow as tf
from impl import classify_image_local

parser = argparse.ArgumentParser()
parser.add_argument('--model', required=True, help='Path to saved model')
parser.add_argument('images', nargs='+', help='Image(s) to classify')
args = parser.parse_args()

predictor = tf.contrib.predictor.from_saved_model(args.model)

for image in args.images:   
    classify_image_local(image, predictor)
