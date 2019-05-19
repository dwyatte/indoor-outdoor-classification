import os
import pytest
import tensorflow as tf

@pytest.fixture()
def filename():
    return os.path.join(os.path.dirname(__file__), 
                        '../images/test/indoor/6ce124f8e1eeb811a0a4fe3e8451efbd-001.png')

@pytest.fixture()
def predictor():    
    return tf.contrib.predictor.from_saved_model(
            os.path.join(os.path.dirname(__file__), '../outdoornet/1558236691'))
