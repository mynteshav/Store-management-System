import cv2
import os
import csv
import pandas as pd

def select_roi(image):
    r = cv2.selectROI("Select ROI", image, False)
    cv2.destroyAllWindows()
    return r

def extract_rgb(image, roi):
    x, y, w, h = roi
    cropped_image = image[y:y + h, x:x + w]
    r, g, b = cv2.mean(cropped_image)[:3]
    return int(r), int(g), int(b)

def save_data(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Filename', 'R', 'G', 'B'])
        writer.writerows(data)
    print("Data saved successfully!")
image_dir = 'colorpic.jpg'
csv_file = pd.read_csv("C:\\Users\\tesha\\Downloads\\colors.csv")
color_data = []
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_dir, filename)
        image = cv2.imread(image_path)
        roi = select_roi(image)
        r, g, b = extract_rgb(image, roi)
        color_data.append([filename, r, g, b])
save_data(csv_file, color_data)
