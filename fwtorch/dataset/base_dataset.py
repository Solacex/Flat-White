import torch
from nvidia.dali.pipeline import Pipeline
import nvidia.dali.ops as ops
import nvidia.dali.types as types
class BaseDoublePipe(Pipeline):
    def __init__(self, batch_size, device_id, shuffle, mean, std, num_threads=4):
        self.input = ops.ExternalSource()
        self.label = ops.ExternalSource()
        self.decode = ops.ImageDecoder(device = "mixed", output_type = types.RGB)
        self.decode_label = ops.ImageDecoder(device = 'mixed'. output_type=types.)
class CommonPipeline(Pipeline):
    def __init__(self, batch_size, num_threads, device_id):
        super(CommonPipeline, self).__init__(batch_size, num_threads, device_id)

        self.decode = ops.ImageDecoder(device = "mixed", output_type = types.RGB)
        self.resize = ops.Resize(device = "gpu",
                                 image_type = types.RGB,
                                 interp_type = types.INTERP_LINEAR)
        self.cmn = ops.CropMirrorNormalize(device = "gpu",
                                            output_dtype = types.FLOAT,
                                            crop = (227, 227),
                                            image_type = types.RGB,
                                            mean = [128., 128., 128.],
                                            std = [1., 1., 1.])
        self.uniform = ops.Uniform(range = (0.0, 1.0))
        self.resize_rng = ops.Uniform(range = (256, 480))

    def base_define_graph(self, inputs, labels):
        images = self.decode(inputs)
        images = self.resize(images, resize_shorter = self.resize_rng())
        output = self.cmn(images, crop_pos_x = self.uniform(),
                          crop_pos_y = self.uniform())
        return (output, labels)
