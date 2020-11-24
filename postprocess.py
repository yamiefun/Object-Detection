import json
import cv2


# convert relativa coor to absolute coor
def convert_coor(filename, rel_coor):
    img_name = f'darknet/{filename}'
    center_x = rel_coor['center_x']
    center_y = rel_coor['center_y']
    width = rel_coor['width']
    height = rel_coor['height']

    img = cv2.imread(img_name)
    img_h = img.shape[0]
    img_w = img.shape[1]

    center_x *= img_w
    center_y *= img_h
    width *= img_w
    height *= img_h

    y1 = round(center_y-height/2)
    y2 = round(center_y+height/2)
    x1 = round(center_x-width/2)
    x2 = round(center_x+width/2)
    return (y1, x1, y2, x2)


def main():
    res = None
    with open("result.json") as f:
        res = json.load(f)

    ret = []
    for img in res:
        print(img['filename'])
        dic = {}
        bbox = []
        score = []
        label = []
        objs = img['objects']
        for obj in objs:
            coor = convert_coor(img['filename'], obj['relative_coordinates'])
            bbox.append(coor)
            score.append(obj['confidence'])
            lbl = 10 if obj['name'] == '0' else int(obj['name'])
            label.append(lbl)
        dic['bbox'] = bbox
        dic['score'] = score
        dic['label'] = label

        ret.append(dic)

    with open("submission.json", "w") as f:
        json.dump(ret, f)


if __name__ == "__main__":
    main()
