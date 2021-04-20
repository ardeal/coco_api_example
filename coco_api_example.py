
import os
import json


from pycocotools.coco import COCO
import matplotlib.pyplot as plt
import cv2


def save_coco_json_header():
    coco_json = r"D:\datasets\coco\images\instances_train2014.json"
    with open(coco_json) as f:
        all_coco_data = json.load(f)
    info = all_coco_data['info']
    license = all_coco_data['licenses']
    json.dump({'info':info, 'licenses':license}, open('json_coco_header.json', 'w'))

    return

def coco_json():

    info = dict()
    license = [dict()]
    image = [dict()]
    annotation = [dict()]
    category = [dict()]

    coco_dict = {
        "info": info,  # dict
        "licenses": [license],  # list ，a few dicts in the list
        "images": [image],  # list ，a few dicts in the list
        "annotations": [annotation],  # list ，a few dicts in the list
        "categories": category # list ，a few dicts in the list
    }
    print(coco_dict)

    return

def coco_image_example():
    cocodataset = COCO(r"D:\datasets\coco\images\instances_train2014.json")
    image0_id = cocodataset.imgs[57870]['id']
    for key, val in cocodataset.imgs.items():
        image_dir = r'D:\datasets\coco\images\train2014'
        imageinfo =  cocodataset.loadImgs(val['id'])
        image = cv2.imread(os.path.join(image_dir, imageinfo[0]['file_name']))

        plt.imshow(image)
        plt.axis('off')
        anns = cocodataset.imgToAnns[val['id']]
        cocodataset.showAnns(anns)
        plt.show()


        aaaaaa = 0


if __name__ == '__main__':

    # ------------------------->
    # save_coco_json_header()
    coco_image_example()


    aaaaaaaaaaaaaaaaa=0

