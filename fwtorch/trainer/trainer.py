import torch
import torch.nn as nn
import torch.nn.functional as F
from utils.Memory import *
from utils.Loss import *
from apex import amp, optimizers
from utils.optimize import *
import os.path as osp
import optimizer as optim

class Trainer(object):
    def __init__(self, model_dict, optim_dict, data_loader_dict, config, writer=None):
        self.models = model.dict
        self.optims = optim.init(optim_dict, warmup=self.config.optim)
            
        self.loaders = data_loader_dict
        self.config = config
        self.writer = writer
    def forward(self):
        pass
    def backward(self):
        pass
    def iter(self):
        losses = {}
        self.optims.zeor_grad() 
        self.forward()
        self.backward()
        self.optims.step()
        return losses

    def save_model(self, iter):
        for key, params in self.models.items():
            tmp_name = '_'.join(self.models[key], str(iter), '.pth')
            torch.save(model.state_dict(), osp.join(self.config['snapshot'], tmp_name))

    def print_loss(self,iter, loss_dict):
        iter_infor = ('iter = {:6d}/{:6d}, exp = {}'.format(iter, self.config.num_steps, self.config.exp))
        to_print = ['{}:{:.4f}'.format(key, loss_dict[key].item()) for key in loss_dict.keys()]
        loss_infor = '  '.join(to_print)
        print(iter_infor +'  '+ loss_infor)
        if self.writer is not None:
            for key in loss_dict.keys():
                self.writer.add_scalar('train/'+key, self.losses[key], i_iter)
    def train(self):
        for i_iter in range(self.config.num_steps):
            losses = self.iter()
            if i_iter % self.config.print_freq ==0:
                self.print_loss(i_iter, losses)
            if i_iter % self.config.save_freq ==0 and i_iter != 0:
                self.save_model(i_iter)

