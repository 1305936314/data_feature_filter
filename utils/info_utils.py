import numpy as np
import os
import re
from .imageio import imread

__all__ = ["key2func", "ImageFold2PathList", "get_img_info"]


def get_size(img_path):
    return os.path.getsize(img_path)


def get_grad(img):
    img_height, img_width = img.shape[:2]
    img_dy = img[:img_height-1] - img[1:]
    img_dx = img[:, :img_width-1] - img[:, 1:]
    img_gradient = np.mean(np.abs(img_dx)) + np.mean(np.abs(img_dy))
    return img_gradient


def key2func(key, info):
    keydict = dict()
    keydict["size"] = lambda x: get_size(x["path"])
    keydict["grad"] = lambda x: get_grad(x["img"])
    info[key] = keydict[key](info)
    return info


def ImageFold2PathList(foldpath, suffix):
    img_list = []
    for img_name in os.listdir(foldpath):
        if re.search(suffix, img_name) is None:
            continue
        img_list.append(foldpath + '/' + img_name)
    print("Load imgs in {} SUCCESS ...".format(foldpath))
    return img_list


def get_img_info(img_path, cfg):
    img = imread(img_path)
    img_height, img_width = img.shape[:2]
    img_info = dict()
    img_info['img'] = img
    img_info['path'] = img_path
    img_info["height"] = img_height
    img_info["width"] = img_width
    keys = [x for x in cfg]

    for key in keys:
        if key in img_info:
            continue
        img_info = key2func(key, img_info)
    return img_info
