# Object Detection
This repository is the project 2 for NCTU course IOC5008: Selected Topics in Visual Recognition using Deep Learning.

0. [Introduction](#Introduction)
1. [How To Use](#How-To-Use)
2. [Result](#Result)
3. [Reference](#Reference)

## Introduction
The purpose of this project is to detect house numbers in street view images. The dataset we used in this project is SVHN dataset, which includes 33402 training images and 13068 testing images. Not only the accuracy of the model is essential, the reference speed is important as well.

## How To Use
1. Follow the [README](https://github.com/AlexeyAB/darknet#yolo-v4-v3-and-v2-for-windows-and-linux) step by step
    + `make` darknet
    + download weights `yolov4.conv.137`
    + modify network config in `yolov4-custom.cfg`
2. Note that the number of classes should be 10, i.e., number 0 to 9. 
3. Download training and testing dataset [HERE](https://drive.google.com/drive/u/1/folders/1Ob5oT9Lcmz7g5mVOcYH3QugA7tV3WsSl), and unzip them.
4. Run `create_train.py`. This script will generate `train.txt` which includes all images' name and path. Also, it'll create independent `txt` files with label information in it for every training image. Then you should move all datas needed for training to correct path mentioned in [README](https://github.com/AlexeyAB/darknet#yolo-v4-v3-and-v2-for-windows-and-linux).
5. Now you can train your custom yolov4 model.
6. To test the accuracy using testing images, you should first run `create_test.py`. It'll generate `test.txt`, which includes all testing images' name and path. Then you can run darknet with your trained weights to test the accuracy.
7. After finish running, use `postprocess.py` to convert the output format to fit TA's requirement.



## Result
Best mAP so far: 0.43944
## Reference
+ [data parsing](https://github.com/pavitrakumar78/Street-View-House-Numbers-SVHN-Detection-and-Classification-using-CNN/blob/master/construct_datasets.py)
+ [darknet](https://github.com/AlexeyAB/darknet)
