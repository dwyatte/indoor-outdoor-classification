import numpy as np
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from classification import read_image, make_request, \
                           classify_image_local, classify_image_remote

def test_read_image(filename):
    image = read_image(filename)
    assert type(image) == np.ndarray
    assert image.shape == (1, 720, 960, 3)
    assert image.dtype == np.float32

def test_make_request(filename):    
    request = make_request(filename)
    assert type(request) is predict_pb2.PredictRequest
    assert request.model_spec.name == 'outdoornet'
    assert request.model_spec.signature_name == tf.saved_model.signature_constants.PREDICT_METHOD_NAME
    assert hasattr(request, 'inputs')

def test_classify_image_remote(filename):
    response = classify_image_remote(filename)
    assert type(response) is predict_pb2.PredictResponse
    assert response.model_spec.name == 'outdoornet'
    assert response.model_spec.signature_name == tf.saved_model.signature_constants.PREDICT_METHOD_NAME
    assert hasattr(response, 'outputs')
    assert 'scores' in response.outputs

def test_classify_image_local(filename, predictor):
    outputs = classify_image_local(filename, predictor)
    assert type(outputs) is dict
    assert 'scores' in outputs
