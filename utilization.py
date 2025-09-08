import cv2
import os
import numpy as np

# ✅ Updated paths for your system
input_dir = r"C:\Users\HARSHITHA\Desktop\datacenteriq\frames"
output_dir = r"C:\Users\HARSHITHA\Desktop\datacenteriq\outputs\reports"
os.makedirs(output_dir, exist_ok=True)

# Threshold for "used" area (tweak if needed)
DARK_THRESHOLD = 100

def analyze_utilization(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return 0.0, "Unreadable"
    height, width = image.shape
    total_area = height * width

    # Invert image: dark = usage
    _, binary = cv2.threshold(image, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV)
    used_area = cv2.countNonZero(binary)

    utilization = (used_area / total_area) * 100
    status = (
        "Empty" if utilization < 10 else
        "Partially Used" if utilization < 80 else
        "Full"
    )

    return round(utilization, 2), status

# Analyze each frame (including subfolders)
report = []
for root, dirs, files in os.walk(input_dir):
    for fname in files:
        if fname.lower().endswith(".jpg"):
            path = os.path.join(root, fname)
            relative_path = os.path.relpath(path, input_dir)
            util_percent, status = analyze_utilization(path)
            report.append(f"{relative_path}: {util_percent:.2f}% → {status}")
            print(f"{relative_path}: {util_percent:.2f}% → {status}")

# Save report
report_path = os.path.join(output_dir, "rack_utilization.txt")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print(f"\n✅ Rack utilization report saved to: {report_path}")
