import json
import os
import cv2
import glob


def via_to_yolo(via_path, image_dir, class_names):
    with open(via_path, "r") as f:
        data = json.load(f)

    for filename, annot in data.items():
        if "regions" not in annot:
            continue

        # get image width and height
        # if isinstance(annot["size"], int):
        #     width, height = 0, 0
        # else:
        #     width, height = annot["size"]["width"], annot["size"]["height"]

    

        # create YOLO label file
        label_path = os.path.join(image_dir, os.path.splitext(filename)[0] + ".txt")
        img = cv2.imread(image_dir + filename)
        H, W =  img.shape[:2]
        # print('w, h', W, H)
        # print(1/0)
        with open(label_path, "w") as label_file:
            for region in annot["regions"]:
                label = (region['region_attributes']['identity'])
                print('check_label..', label)
                shape = region["shape_attributes"]
                if shape["name"] == "polygon":
                    points = [(shape["all_points_x"][i], shape["all_points_y"][i])
                              for i in range(len(shape["all_points_x"]))]
                    x_min = min(point[0] for point in points)
                    y_min = min(point[1] for point in points)
                    x_max = max(point[0] for point in points)
                    y_max = max(point[1] for point in points)

                    # normalize coordinates
                    x_center = (x_min + x_max) / (2 * W)
                    y_center = (y_min + y_max) / (2 * H)
                    box_width = (x_max - x_min) / W
                    box_height = (y_max - y_min) / H

                    # print('jfdljsgewjg[ejwg[jewvowbdovbwodbi')

                    # print( list(class_names))

                    label_index = list(class_names).index(label)

                    print(label_index)
                    

                    # write label to file
                    label_file.write(f"{label_index} {x_center:.6f} {y_center:.6f} "
                                      f"{box_width:.6f} {box_height:.6f}\n")
            # print(1/0)


if __name__ == "__main__":
    
    DATA_FOLDER = 'exercise_1'

    class_names = []
    for path in  glob.glob(DATA_FOLDER + '/*'):
        print(path)
    
        via_path = path + '/via_region_data.json'
        image_dir = path + '/'
        # Load VIA annotations from JSON file
        with open(via_path) as f:
            via_data = json.load(f)
        
        # Get all unique class names from the annotations
        for image_name, image_data in via_data.items():
            for region in image_data['regions']:
                name = region['region_attributes']['identity']
                if name not in class_names:
                    class_names.append(region['region_attributes']['identity'])

        # # Print the class names
        print(class_names)
        # print(1/0)
        via_to_yolo(via_path, image_dir, class_names)

    for i in class_names:
        with open('classes.txt', 'a+') as class_file:
            class_file.write(i)
            class_file.write('\n')

    
        

