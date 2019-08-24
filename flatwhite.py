import torch
import os.path as osp

#class Recorder(object):
def print_loss(loss_dic):
    result = []
    for key in loss_dict.keys():
        value = loss_dict[key]
        if isinstance(value, torch.Tensor):
            value = value.item()
        tmp = "{} : {:.4f}".format(key, value)
        result.append(tmp)
    result = '__'.join(result)
    return result
def mkdir(p):
    if not osp.exists(p):
        os.mkdirs(p)
    print('DIR {} created'.format(p))

#def yml_record(path, dict):
    
    
