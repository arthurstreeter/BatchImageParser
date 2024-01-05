from ultralytics import YOLO
import cv2
import os
import argparse
import json
import time


path = os.path.dirname(os.path.realpath(__file__))
images_dir = os.path.join(path, "images")
extracted_dir = os.path.join(path, "extracted")
supported_images = (".jpg", ".png", ".jpeg")

def create_image_from_bbox(image_path, bbox, output_path):
    image = cv2.imread(image_path)
    x, y, x2, y2 = map(int,bbox.xyxy[0])
    cropped_image = image[y:y2, x:x2]
    cv2.imwrite(output_path, cropped_image)

def detect(image_path):
    model = YOLO("yolov8n.pt")
    results = model(image_path)
    return results

def extract_objects_from_image(images_dir, image_file_name, confidence, desired_classes):
    path_to_image = images_dir + "/" + image_file_name
    results = detect(path_to_image)
    detected_objects = []
    for result in results:
        boxes = result.boxes
        class_labels = result.names
        for box in boxes:
            confident = float(box.conf) >= confidence
            checked = int(box.cls) in desired_classes if len(desired_classes) > 0 else True
            if checked and confident:
                detected_objects.append({"box": box, "class_name": class_labels[int(box.cls)]})

    for i, object in enumerate(detected_objects):
        if not os.path.exists(extracted_dir):
            os.makedirs(extracted_dir)
        if not os.path.exists(extracted_dir + "/" + image_file_name.split(".")[0]):
            os.makedirs(extracted_dir + "/" + image_file_name.split(".")[0])
        create_image_from_bbox(path_to_image, object['box'], extracted_dir + "/" + image_file_name.split(".")[0] + "/" + f"{i}_{object['class_name']}_"+image_file_name)

def extract_objects_from_images_in_dir(dir, confidence, desired_classes):
    if type(desired_classes) != list and desired_classes != None:
        if "," in desired_classes:
            desired_classes = desired_classes.split(",")
        elif " " in desired_classes:
            desired_classes = desired_classes.split(" ")
        elif type(desired_classes) == str and len(desired_classes) <= 2:
            desired_classes = [int(desired_classes)]
        else:
            print("Desired classes must be a list of ints or a string with a comma or space between each class id.")
            return
    try:
        desired_classes = [int(class_id) for class_id in desired_classes] if desired_classes != None else []
    except ValueError:
        print("Desired classes must be a list of ints or a string with a comma or space between each class id.")
        return
    
    if confidence is not None and confidence > 1:
        print("Confidence must be a float between 0 and 1.")
        return
    if confidence is None:
        confidence = 0.00

    if dir is None:
        dir = images_dir

    if os.path.exists(dir):
        print("Checking directory: " + dir)
        directory = os.listdir(dir)
        compatible_images_found = False
        for image_file_name in directory:
            if image_file_name.endswith(supported_images):
                compatible_images_found = True
                print("Found compatible images in directory: " + dir)
                break
        if directory == [] or directory == None:
            print("No images found in directory: " + dir)
            return
        if not compatible_images_found:
            print("No supported images found in directory: " + dir)
            return
        for image_file_name in directory:
            print("Extracting objects from image: " + image_file_name)
            if image_file_name.endswith(supported_images):
                extract_objects_from_image(dir, image_file_name, confidence, desired_classes)




def main():
    parser = argparse.ArgumentParser(description='Extract objects from images using Ultralytics YOLOv8.')
    parser.add_argument('--dir', '-d', type=str, help='Path to directory containing images, defaults to ./images')
    parser.add_argument('--confidence', '-c', type=float, help='Confidence threshold for detection')
    parser.add_argument('--classes', '-i', type=str, help='Classes to extract from images')
    args = parser.parse_args()

    extract_objects_from_images_in_dir(dir=args.dir, confidence=args.confidence, desired_classes=args.classes)
    

if __name__ == "__main__":
    main()