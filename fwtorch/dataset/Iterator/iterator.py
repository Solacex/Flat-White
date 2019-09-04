from base_iterator import *
import utils
import os.path as osp

class TxtIterator(Iterator):
    def compose(self, data_dir, txt_path):
        self.txt = utils.txt_read(txt_path)
        if not isinstance(data_dir, str):
            self.iters = {}
            self.txt.sort()
            for i, name in enumerate(data_dir):
                self.iters[i] = [osp.join(name, file_name) for file_name in self.txt]
        else:
            self.iters = [osp.join(data_dir, file_name) for file_name in self.txt ]



#x = TxtIterator(('123', 'asd'), '/home/guangrui/segmentation_DA/dataset/cityscapes_list/train.txt')
#print(x.iters[0])
