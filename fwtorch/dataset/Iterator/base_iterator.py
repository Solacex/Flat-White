import os, sys

class Iterator(object):
    def __init__(self, *args, **kwargs):
        self.compose(*args, **kwargs)
        self.index = 0
        self.len = len(self.iters)
    def __iter__(self):
        return self
    def get_item(self, index):
        if isinstance(self.iters, dict):
            keys = self.iters.keys()
            result = (self.iters[key][index] for key in keys)
            return result
        else:
            return self.iters[index]
    def __next__(self):
        try:
            result = self.get_item[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return index
    def compose():
        pass


