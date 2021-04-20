# examples about how to use coco api


# explanation: image_id and annotation id
**each image has a unique id: image_id**  
**each annotation has a unique id: id**  
**each image might have several annotation items. so each image includes several annotation id. this is the reason why <code>COCO.imgToAnns[val['id']]</code> might have several items**  
**each annotation item(id) must belong to a certain image.**  

# explanation: COCO class
**for imgs dict in COCO class, there are many images(dict) in the dict. the key of each dict in imgs dict is the image_id**
**for anns dict in COCO class, there are many annotation items(dict) in the dict. the key of each dict in anns dict is the annotation id**


# save_coco_json_header() function in the code
1) this function load coco json file.
2) you could debug this function and review the data in variable <code>all_coco_data</code>
3) this fucntion could save the header of coco json for as an example for you to understand what the header of coco is.

# coco_json() function in the code
the data structure in coco json.
```python
 coco_dict = {
        "info": info,  # dict
        "licenses": [license],  # list ，a few dicts in the list
        "images": [image],  # list ，a few dicts in the list
        "annotations": [annotation],  # list ，a few dicts in the list
        "categories": category # list ，a few dicts in the list
    }
```

# coco_image_example() function in the code
the code shows how to read 1 image and its annotation from coco and show them.



# data structure of coco json
the following picture shows the data structure of coco json. it explains image_id and annotation_id.
<p align="left"><img width="800" src="https://github.com/ardeal/coco_api_example/blob/master/coco_json_explanation.png"></p>














