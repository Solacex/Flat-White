import torch.optim as optim

class optimizer(object):
    def __init__(self, optim_dict, optim_config):
        self.optims = optim_dict
        self.config = optim_config
        self.names = [key for key in self.optims.keys()]
        print('Initialize Optimizers: '+ ' '.join(self.names))

    def zero_grad(self):
        for key in self.names:
            self.optims[key].zero_grad()
    def step(self):
        for key in self.names:
            self.optims[key].step()

    def adjust_lr(self, iter):
        pass

