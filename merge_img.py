#-*- coding: utf-8 -*-
import numpy as np
from PIL import Image

def make_arrays(nb_rows, img_height, img_width):
    if nb_rows:
        dataset = np.ndarray((nb_rows, img_height, img_width), dtype=np.float32)
        labels = np.ndarray(nb_rows, dtype=np.int32)
    else:
        dataset, labels = None, None
    return dataset, labels

def merge_datasets(path, img_height,img_width):
    '''
       func: 将一个文件夹内的各种图片合并到一个numpy数组中, 且生成对应的labels
       para:
           path: 数据集的路径  img_hight: 图片的高度  img_width: 图片的宽度
       return values:
           dataset: 数据集 labels: 标签
       Author: zhaozhichao
    '''
    classes = [item for item in os.listdir(path) if os.path.isdir(path + "/" + item)]
    classes_num = len(classes)
    count = 0
    for item in classes:
        count += len(os.listdir(path + '/' + item))
    dataset, labels = make_arrays(count, img_height, img_width)

    data_index = 0
    class_index = 0
    for item in classes:
        print("The class is: " + item + ", and class index is: " + str(class_index))
        for image_name in os.listdir(path + '/' + item):
            try: #read the Image
                img = np.array(Image.open(path+'/'+item + '/' + image_name))
                dataset[data_index,:,:] = img
                labels[data_index] = class_index
                data_index += 1
            except IOError as e:
                print(e, '- it\'s ok, skipping.')
        class_index += 1
    print("The dataset shape is:" + str(dataset.shape) + ", and the labels shape is:" + str(labels.shape))
    return dataset,labels
path = "notMNIST_small"
dataset,labels = merge_datasets(path,28,28)
