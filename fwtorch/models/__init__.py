import torch.nn as nn
import torch.nn.functional as F
import importlib
from models.base_model import BaseModel

def find_model_by_names(model_name):
    #Import the module "models/[model_name]_model.py".
    model_filename = "models." + model_name + "_model"
    modellib = importlib.import_module(model_filename)
    model = None
    target_model_name = model_name.replace('_', '')
    for name, cls in modellib.__dict__.items():
        if name.lower() == target_model_name.lower() and issubclass(cls, BaseModel):
            model = cls

    if model is None:
        print("In %s.py, there should be a subclass of BaseModel with class name that matches %s in lowercase." % (model_filename, target_model_name))
        exit(0)
    return model

def init_models(config):
    models = {}
    model_names = config.models
    for name in model_names:
        models[name] = find_model_by_name(name)
