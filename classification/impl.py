import os
import grpc
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2_grpc

channel = grpc.insecure_channel(os.environ['TF_SERVING_URL'])
conn = prediction_service_pb2_grpc.PredictionServiceStub(channel)
classnames = ['Indoor', 'Outdoor']

def read_image(filename):
    image = np.array(Image.open(filename).convert('RGB'), dtype=np.float32)
    image = np.expand_dims(image, 0)
    return image

def make_request(filename):
    image = read_image(filename)
    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'outdoornet'
    request.model_spec.signature_name = tf.saved_model.signature_constants.PREDICT_METHOD_NAME
    request.inputs[tf.saved_model.signature_constants.PREDICT_INPUTS].CopyFrom(
        tf.contrib.util.make_tensor_proto(image)
    )
    return request

def classify_image(filename):    
    request = make_request(filename)
    response = conn.Predict(request)
    score = np.array(response.outputs['scores'].float_val)
    print('{}: {} (outdoor: {:.4f}, indoor: {:.4f})'.format(filename,
                                                            classnames[int(np.round(score))], 
                                                            float(score), float(1-score)))
    return response
