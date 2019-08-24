import os, sys
import os.path as osp
from shutil import copyfile
import tqdm


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def path_list(path):
    return os.listdir(path)

def move(frm, to, file_name):
    mkdir(to)
    copyfile(osp.join(frm, file_name), osp.join(to, file_name))

def txt_read(path):
    with open(path) as f:
        lines = f.readlines()
    result = []
    for l in lines:
        l.rstrip()
        result.append(l)
    return result

def compose_2level_folder(path):

    result = {}
    cnt = 0
    with tqdm.tqdm(total = len(path_list(path))) as pbar:
        for root, dirs, files in os.walk(path):
            for i, dir_ in enumerate(dirs):
                result[dir_]=path_list(osp.join(root, dir_))
                cnt+=len(osp.join(root, dir_))
                pbar.update(1)
    print('Traversing Finished, {} folfers and {} files total.'.format(len(path_list(path)), cnt))
    return result
 
