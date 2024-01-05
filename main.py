from ultralytics import YOLO
import cv2
import os
import argparse

path = os.path.dirname(os.path.realpath(__file__))
images_dir = os.path.join(path, "images")
extracted_dir = os.path.join(path, "extracted")
model = YOLO("yolov8n.pt")

def create_image_from_bbox(image_path, bbox, output_path):
    image = cv2.imread(image_path)
    x, y, x2, y2 = map(int,bbox.xyxy[0])
    cropped_image = image[y:y2, x:x2]
    cv2.imwrite(output_path, cropped_image)

def detect(image_path):
    results = model(image_path)
    return results

def extract_objects_from_image(images_dir=images_dir, image_file_name="", confidence=None, desired_classes=[]):
    path_to_image = images_dir + "/" + image_file_name
    results = detect(path_to_image)
    detected_objects = []
    for result in results:
        boxes = result.boxes
        class_labels = result.names
        for box in boxes:
            confident = float(box.conf) >= confidence if confidence is not None else True
            checked = int(box.cls) in desired_classes if desired_classes is not [] else True
            if checked and confident:
                detected_objects.append({"box": box, "class_name": class_labels[int(box.cls)]})

    for i, object in enumerate(detected_objects):
        if not os.path.exists(extracted_dir):
            os.makedirs(extracted_dir)
        if not os.path.exists(extracted_dir + "/" + image_file_name.split(".")[0]):
            os.makedirs(extracted_dir + "/" + image_file_name.split(".")[0])
        create_image_from_bbox(path_to_image, object['box'], extracted_dir + "/" + image_file_name.split(".")[0] + "/" + f"{i}_{object['class_name']}_"+image_file_name)

def extract_objects_from_images_in_dir(dir, confidence=None, desired_classes=[]):
    if type(desired_classes) != list:
        if "," in desired_classes:
            desired_classes = desired_classes.split(",")
        elif " " in desired_classes:
            desired_classes = desired_classes.split(" ")
        else:
            print("Desired classes must be a list of ints or a string with a comma or space between each class id.")
            return
    try:
        desired_classes = [int(class_id) for class_id in desired_classes]
    except ValueError:
        print("Desired classes must be a list of ints or a string with a comma or space between each class id.")
        return
    if confidence is not None and confidence > 1:
        print("Confidence must be a float between 0 and 1.")
        return
    if os.path.exists(dir):
        for image_file_name in os.listdir(dir):
            if image_file_name.endswith((".jpg", ".png", ".jpeg")):
                extract_objects_from_image(image_file_name, confidence, desired_classes)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract objects from images using Ultralytics YOLOv8.')
    parser.add_argument('--dir', '-d', type=str, help='Path to directory containing images, defaults to ./images')
    parser.add_argument('--confidence', '-con', type=float, help='Confidence threshold for detection')
    parser.add_argument('--classes', '-cl', type=str, help='Classes to extract from images')
    args = parser.parse_args()
    if args.dir is not None:
        extract_objects_from_images_in_dir(args.dir, args.confidence, args.classes)
    else:
        print("Please provide a directory of images to extract objects from.")