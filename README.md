
# Batch Image Object Detection


This tool is meant to batch process a folder of images utilizing Ultralytics' YOLOv8, cropping out images of detected objects.




## Requirements

Python 3.10+

Pip

Will Install via Pip:

    Ultralytics
## Installation

```
  git clone https://github.com/arthurstreeter/BatchImageParser.git
  
  Run included setup.bat

```

This will create a virtual environment in the directory, also create the images and extracted directories that are used by default. If you'd like, you can copy the images you want to parse into the image folder, or simply pass the directory to the cli.
    
## Running Tests


To run with default paths, no confidence or class filters, simply run the executable


run.bat


To run via command line from the repo's directory:

```bash
  run.bat --help
  run.bat --directory=C:/Directory/To/Images
  run.bat --confidence=.6 --classes=0,4,32
```


## Identifiable Classes of Objects

The YOLO trained data can identify the following objects, and here is their respective Class ID's:

```json
{
    "0": "person",
    "1": "bicycle",
    "2": "car",
    "3": "motorcycle",
    "4": "airplane",
    "5": "bus",
    "6": "train",
    "7": "truck",
    "8": "boat",
    "9": "traffic light",
    "10": "fire hydrant",
    "11": "stop sign",
    "12": "parking meter",
    "13": "bench",
    "14": "bird",
    "15": "cat",
    "16": "dog",
    "17": "horse",
    "18": "sheep",
    "19": "cow",
    "20": "elephant",
    "21": "bear",
    "22": "zebra",
    "23": "giraffe",
    "24": "backpack",
    "25": "umbrella",
    "26": "handbag",
    "27": "tie",
    "28": "suitcase",
    "29": "frisbee",
    "30": "skis",
    "31": "snowboard",
    "32": "sports ball",
    "33": "kite",
    "34": "baseball bat",
    "35": "baseball glove",
    "36": "skateboard",
    "37": "surfboard",
    "38": "tennis racket",
    "39": "bottle",
    "40": "wine glass",
    "41": "cup",
    "42": "fork",
    "43": "knife",
    "44": "spoon",
    "45": "bowl",
    "46": "banana",
    "47": "apple",
    "48": "sandwich",
    "49": "orange",
    "50": "broccoli",
    "51": "carrot",
    "52": "hot dog",
    "53": "pizza",
    "54": "donut",
    "55": "cake",
    "56": "chair",
    "57": "couch",
    "58": "potted plant",
    "59": "bed",
    "60": "dining table",
    "61": "toilet",
    "62": "tv",
    "63": "laptop",
    "64": "mouse",
    "65": "remote",
    "66": "keyboard",
    "67": "cell phone",
    "68": "microwave",
    "69": "oven",
    "70": "toaster",
    "71": "sink",
    "72": "refrigerator",
    "73": "book",
    "74": "clock",
    "75": "vase",
    "76": "scissors",
    "77": "teddy bear",
    "78": "hair drier",
    "79": "toothbrush"
}
```