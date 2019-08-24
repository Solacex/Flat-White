import numpy as np

import os,sys
import os.path as osp
from .file_iterator import *
'''
class ImageFolder(object):

    dataset format:
       |->Folder
       |  -> ID
       |    ->images

    def __init__(folder_path):
    def define_class:
    def iterate():
'''
class VideoFolderByVideo(object):
    '''
    dataset format:
       |->Folder
       |  -> Video ID
       |    ->video frames


    '''
    def __init__(self,root, class2id=None):
        self.root      = root
        self.vid2frame = compose_2level_folder(root)

    def map(self):
        return self.vid2frame

'''
class VideoFolderByID(object):

    dataset format:
       |->Folder
       |  -> Video class ID
       |    ->video frames



    def __init__(folder_path):
    def iterate():
'''
