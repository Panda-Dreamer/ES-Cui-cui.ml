import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = ''

import numpy as np
np.finfo(np.dtype("float32"))
np.finfo(np.dtype("float64"))

try:
    import tflite_runtime.interpreter as tflite
except ModuleNotFoundError:
    from tensorflow import lite as tflite

def loadModel(class_output=True):
    #Tensorflow documentation
    model = {
    'INTERPRETER':"",
    'INPUT_LAYER_INDEX':"",
    'OUTPUT_LAYER_INDEX':"",
    }
    model['INTERPRETER'] = tflite.Interpreter(model_path='./Files/Model.tflite', num_threads=8)
    model['INTERPRETER'].allocate_tensors()
    input_details = model['INTERPRETER'].get_input_details()
    output_details = model['INTERPRETER'].get_output_details()
    model['INPUT_LAYER_INDEX'] = input_details[0]['index']
    model['OUTPUT_LAYER_INDEX'] = output_details[0]['index']
    return model


def flat_sigmoid(x, sensitivity=-1):
    return 1 / (1.0 + np.exp(sensitivity * np.clip(x, -15, 15)))

def predict(sample):


    model = loadModel()
    model['INTERPRETER'].resize_tensor_input(model['INPUT_LAYER_INDEX'], [len(sample), *sample[0].shape])
    model['INTERPRETER'].allocate_tensors()
    model['INTERPRETER'].set_tensor(model['INPUT_LAYER_INDEX'], np.array(sample, dtype='float32'))
    model['INTERPRETER'].invoke()
    prediction = model['INTERPRETER'].get_tensor( model['OUTPUT_LAYER_INDEX'])

    return prediction

