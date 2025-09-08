import cv2
import os

# ✅ Your actual system paths
input_dir = r"C:\Users\HARSHITHA\Desktop\datacenteriq\frames"
output_dir = r"C:\Users\HARSHITHA\Desktop\datacenteriq\outputs\reports"
os.makedirs(output_dir, exist_ok=True)

EDGE_THRESHOLD = 3000  # You can adjust this based on visual results

def check_cleanliness(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_count = cv2.countNonZero(edges)
    status = "Messy" if edge_count > EDGE_THRESHOLD else "Clean"
    return edge_count, status

# Recursively walk through all subfolders and analyze images
report = []
for root, dirs, files in os.walk(input_dir):
    for fname in files:
        if fname.lower().endswith(".jpg"):
            path = os.path.join(root, fname)
            relative_path = os.path.relpath(path, input_dir)
            edge_count, status = check_cleanliness(path)
            report.append(f"{relative_path}: {edge_count} edges → {status}")
            print(f"{relative_path}: {edge_count} edges → {status}")

# Save report
output_file = os.path.join(output_dir, "cable_cleanliness.txt")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print(f"\n✅ Cable report saved to: {output_file}")
