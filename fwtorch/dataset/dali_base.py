
import torch
from nvidia.dali.pipeline import Pipeline
import nvidia.dali.ops as ops
from .Iterator import *
import nvidia.dali.types as types

class BasePipeline(Pipeline):
    def __init__(iterator, batch_size, num_threads, device_id):
        self.input = ops.ExternalSource()#ops.FileReader(iterator[0], share_id=device_id, num_shards=num_threads) 
        self.label = ops.ExternalSource()
        self.decode = ops.ImageDecoder(device='mixed', output_type=types.RGB)
        self.label_decode = ops.ImageDecoder(device='mixed', output_type=types.msa)    

    def define_graph(self):
