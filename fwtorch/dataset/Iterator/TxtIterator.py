import os, path
import utils
import sys
import os.path as osp
class TxtIterator(object):
    def __init__(self, data_dir, txt_path):
        self.txt = utils.txt_read(txt_path)
    
        if not isinstance(data_dir, str):
            self.path = {}
            self.txt.sort()
            for i, name in enumerate(data_dir):
                self.path[i] = [osp.join(name, file_name) for file_name in self.txt]
        else:
            self.path = [osp.join(data_dir, file_name) for file_name in self.txt ]

x = TxtIterator(('/home/guangrui/data/visda17_seg/cityscapes/','/home/guangrui/data/visda17_seg/gta5/'),  '/home/guangrui/segmentation_DA/dataset/gta5_list/train.txt')
