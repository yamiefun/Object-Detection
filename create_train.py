import numpy as np
import cv2
import os
import pandas as pd
import h5py


def get_name(index, hdf5_data):
    name = hdf5_data['/digitStruct/name']
    return ''.join([chr(v[0]) for v in hdf5_data[name[index][0]].value])


def get_bbox(index, hdf5_data):
    attrs = {}
    item = hdf5_data['digitStruct']['bbox'][index].item()
    for key in ['label', 'left', 'top', 'width', 'height']:
        attr = hdf5_data[item][key]
        values = [hdf5_data[attr.value[i].item()].value[0][0]
                  for i in range(len(attr))] if len(attr) > 1 else [attr.value[0][0]]
        attrs[key] = values
    return attrs


def img_bbox_data_constructor(mat_file):
    f = h5py.File(mat_file,'r') 
    all_rows = []
    print('image bounding box data construction starting...')
    bbox_df = pd.DataFrame([],columns=['height','img_name','label','left','top','width'])
    for j in range(f['/digitStruct/bbox'].shape[0]):
        img_name = get_name(j, f)
        row_dict = get_bbox(j, f)
        row_dict['img_name'] = img_name
        all_rows.append(row_dict)
        bbox_df = pd.concat([bbox_df,pd.DataFrame.from_dict(row_dict,orient = 'columns')])
    bbox_df['bottom'] = bbox_df['top']+bbox_df['height']
    bbox_df['right'] = bbox_df['left']+bbox_df['width']
    print('finished image bounding box data construction...')
    return bbox_df


def create_yolo_training_data(df, img_folder):
    for i in range(1, 32403):
        print("Creating txt for {:5d}.png.".format(i))
        file_name = f'{img_folder}/{str(i)}.txt'
        img_name = f'{str(i)}.png'
        with open(file_name, "w") as f:
            labels = df.loc[df['img_name']==img_name]
            for j in range(len(labels)):
                # cv2 image shape: (h, w, c)
                img = cv2.imread(img_folder+"/"+img_name)
                img_h = img.shape[0]
                img_w = img.shape[1]
                obj_clss = int(labels.loc[j]['label'])%10
                x_center = ((labels.loc[j]['left']+labels.loc[j]['right'])/2)/img_w
                y_center = ((labels.loc[j]['bottom']+labels.loc[j]['top'])/2)/img_h
                width = labels.loc[j]['width']/img_w
                height = labels.loc[j]['height']/img_h
                line = f'{obj_clss} {x_center} {y_center} {width} {height}\n'
                f.write(line)


def create_train_txt():
    with open('train.txt', "w") as f:
        for i in range(1, 32403):
            img_name = f'{str(i)}.png'
            line = f'data/obj/{img_name}\n'
            f.write(line)


if __name__ == "__main__":
    img_folder = "train"
    mat_file_name = "digitStruct.mat"
    # create dataframe for training data
    img_bbox_data = img_bbox_data_constructor(os.path.join(img_folder,mat_file_name))

    create_yolo_training_data(img_bbox_data, img_folder)

    create_train_txt()
