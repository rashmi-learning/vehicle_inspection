


# vehicle_inspection - Assessment:1

## Description:  
### Exercise:1 Real Time Detection
### Taking any vehicle Image and predicting its position such as front, front_left, front_right rear, rear_right, rear_left.
- Task:  Train a real time model that takes any image as input and identify which of these six above categories the image belongs to.

## Dataset:
- The dataset is provided in the assessment document.

## Approach: 
To get the desired output; these are the following steps:

1. Understanding the Dataset:
- The dataset consists of multiple folders with some images and its annotation in json format.Since the annotation is done using VIA annotation tool, no class info is given beforehand.
- Fetching the number of classes from the json annotation across all folders. It has 178 classes which has been listed into a yaml file.
- Since I am planning to train a object detector, I decided to go with YOLO and converted the annotation to YOLO format.

2. Approach to finding the category of a vehicle belongs:
- Training the object detector: 
  - trained a yolov5 object detector for that we divided the dataset into train-val-test as 80-10-10. The test images are kept for testing the trained model accuracy.
  - convert the trained model to tflite.
  - Writing a script to inference with tflite.
- Writing the logic to get a class category: Since the most of the classes does not play any role in deciding vehicle position. Filtered out all the classes which are unnecessary and written a logic based on the important classes to decide a vehicle position.

## Files Description:

1. car_data.yaml:  consist of all the classes the vehicles annotated for.
2. via_to_yolo.py: takes VIA annoatation and converts it to YOLO format.
3. test_predict.py : takes images and predicts the category of each vehicle wrt class detected by the object detector and saves the result to csv.


## Getting started
Clone the Github repository:

```bash
git clone https://github.com/rashmi-learning/vehicle_inspection.git
cd vehicle_inspection
```
#### Pip
```bash
pip install -r requirements.txt

```
#### Running the inference
```bash
python test_predict.py --source <input file / input folder> --conf 0.25 --model best_car_part-fp16.tflite
```
Example run:
```bash
python test_predict.py --source images/ --model model/best_car_part-fp16.tflite
```

This will generate a output folder with respect to each classification category and a csv file that lists all the images category along with confidence score.


## Scope of Improvement
The current approach is giving only 80% of accuracy as it is confused for the classes which appeared left/right both side of vehicle such as leftwa/rightwa so there is a scope of improvement. 

The second best approach could be to get higher accuracy:
- First create category wise data using the annotation classes.
- Train a classification model rather than object detection to classify between six classes.



## Acknowledgments
* [Yolov5 Implementation](https://github.com/ultralytics/yolov5.git)
* [TFLite Conversion](https://www.tensorflow.org/lite/models/convert)
