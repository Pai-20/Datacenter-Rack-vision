from ultralytics import YOLO
import os
import cv2

# Load the pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Set your paths
input_dir = r"C:\Users\HARSHITHA\Desktop\datacenteriq\frames"
output_dir = r"C:\Users\HARSHITHA\Desktop\datacenteriq\outputs\overlays"
os.makedirs(output_dir, exist_ok=True)

# Loop through all images in frames folder
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        image_path = os.path.join(input_dir, filename)
        results = model(image_path)  # Run inference
        annotated = results[0].plot()  # Annotated frame with boxes

        # Save output
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, annotated)
        print(f"✅ Saved: {output_path}")

print("🎯 Detection complete. Check the 'overlays' folder.")
