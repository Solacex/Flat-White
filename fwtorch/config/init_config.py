from easydict import EasyDict as edict
from yaml import load, dump
import yaml
from utils.flatwhite import *
from torch.utils.tensorboard import SummaryWriter

def easy_dic(dic):
    dic = edict(dic)
    for key, value in dic.items():
        if isinstance(value, dict):
            dic[key] = edict(value)
    return dic
def show_config(config, sub=False):
    msg = ''
    for key, value in config.items():
        if isinstance(value, dict):
            msg += show_config(value, sub=True)
        else :
            msg += '{:>25} : {:<15}\n'.format(key, value)
    return msg
def type_align(source, target):
    if isinstance(source, int):
        return int(target)
    elif isinstance(source, float):
        return float(target)
    elif isinstance(source, str):
        return target
def config_parser(config, args):
    for arg in args:
        if ':' not in arg:
            continue
        else:
            key, value = arg.split(':')
        if key in config:
            value = type_align(config[key]) 
            config[key] = value
def init_config(env_path, config_path):
    with open(env_path,'r') as f:
        env =yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    with open(config_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    
    env    = easy_dic(env)
    config = easy_dic(config)
    config['snapshot'] = osp.join(env.snapshot, config.note)
    mkdir(config.snapshot)

    if config.log.tensorboard:
        config.log.tb = osp.join(env.log, config.note)
        mkdir(config.log.tb)
        writer = SummaryWriter(config.log.tb)
    else:
        writer = None

    message = show_config(config)
    print(message)
    return env, config, writer
