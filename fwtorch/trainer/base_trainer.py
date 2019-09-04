import torch
from apex import amp, optimizers
import os.path as osp
from utils.Memory import Memory

class BaseTrainer(object):
    def __init__(self, models, optimizers, loaders, up_s, up_t, config,  writer):
        self.model = models
        self.optim = optimizers
        self.loader = loaders
        self.coeff = config.coeff
        self.hyper = config.hyper
        self.config = config
        self.output_dict = {}
        self.up_src = up_s
        self.up_tgt = up_t
        self.writer = writer

    def backward_loss(self,loss, optimizer):
        if self.config.model.fp16:
            with amp.scale_loss(loss, optimizer) as scaled_loss:
                scaled_loss.backward()
        else:
            loss.backward()

    def forward(self):
        pass
    def backward(self):
        pass

    def iter(self):
        pass

    def train(self):
        for i_iter in range(self.config.optim.num_steps):
            losses = self.iter(i_iter)
            if i_iter % self.config.log.print_freq ==0:
                self.print_loss(i_iter)
            if i_iter % self.config.log.save_freq ==0 and i_iter != 0:
                self.save_model(i_iter)

    def save_model(self, iter):
        for key, params in self.model.items():
            tmp_name = '_'.join((key, str(iter))) + '.pth'
            torch.save(params.state_dict(), osp.join(self.config['snapshot'], tmp_name))

    def print_loss(self, iter):
        iter_infor = ('iter = {:6d}/{:6d}, exp = {}'.format(iter, self.config.optim.num_steps, self.config.note))
        to_print = ['{}:{:.4f}'.format(key, self.loss_dict[key].item()) for key in self.loss_dict.keys()]
        loss_infor = '  '.join(to_print)
        print(iter_infor +'  '+ loss_infor)
        if self.config.log.tensorboard and self.writer is not None:
            for key in self.loss_dict.keys():
                self.writer.add_scalar('train/'+key, self.loss_dict[key], iter)

