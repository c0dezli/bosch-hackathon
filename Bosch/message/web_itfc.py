from .model import predict_one_record, save_one_record, retrain_model
from .eagle import csvDataToCoordinates
from .vec2img import pts2flatten, pts2image, pos2mnistlike


def predict(x, y, z, t):
    import numpy as np
    #from PIL import Image
    c = csvDataToCoordinates(x, y, z, np.array(t) / (10 ** 9))
    p2d = pts2flatten(c)
    img = pos2mnistlike(p2d[:, 0], p2d[:, 1])
    return predict_one_record(img)

import json
def save_data(x, y, z, t, label):
    print(type(x), x)
    x = json.loads(x)
    y = json.loads(y)
    z = json.loads(z)
    t = json.loads(t)
    save_one_record([x, y, z, t], label)


def retrain():
    retrain_model()
