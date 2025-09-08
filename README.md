📡 Datacenter Rack Vision

An AI-powered computer vision system to analyze datacenter videos for rack utilization and cable cleanliness.
This project extracts frames from client-provided videos, runs object detection, and generates structured reports for monitoring datacenter health.

🔹 Features

🎥 Video-to-Frames: Extracts frames (1 fps) from datacenter surveillance videos.

🤖 Rack & Equipment Detection: YOLOv8 baseline detection with custom label set.

📊 Rack Utilization Analysis: Calculates utilization % (Empty / Partial / Full).

🧹 Cable Cleanliness Analysis: Edge detection scoring (Clean vs Messy).

📑 Automated Reports: Generates overlays, JSON, CSV, and TXT summaries.

🛠 Annotation Workflow: Dataset preparation with Roboflow and CVAT.

🔹 Project Structure
datacenteriq/
├── input_videos/       # Raw client videos
├── frames/             # Extracted frames (1 fps)
├── models/             # YOLO model weights
├── outputs/
│   ├── overlays/       # Annotated frames
│   └── reports/        # JSON/CSV/TXT reports
├── scripts/            # Python scripts for detection & analysis
└── README.md           # Documentation

🔹 Custom Labels
rack, server, switch, patch_panel, cable_bundle, power_strip, 
monitor, blank_panel, port_block, loose_cable, damaged_hardware

🔹 Tech Stack

Python 3.12

OpenCV – Frame extraction, edge detection

Ultralytics YOLOv8 – Object detection

FFmpeg – Video preprocessing

Roboflow / CVAT – Dataset annotation

Pandas, JSON, CSV – Report generation

🔹 Example Workflow

Place input video in input_videos/.

Run frame extraction:

python scripts/extract_frames.py


Run YOLOv8 detection:

python scripts/detect_racks.py


Analyze utilization:

python scripts/analyze_utilization.py


Analyze cable cleanliness:

python scripts/analyze_cleanliness.py


Check results in outputs/overlays and outputs/reports.

🔹 Deliverables

Extracted frame datasets (shared with client as ZIP).

Annotated overlays for racks & equipment.

Rack utilization and cable cleanliness reports.

Research on advanced detection models (YOLOv7/9, Faster R-CNN, SSD, DETR).

🔹 Future Work

Train custom YOLOv8 model with annotated dataset.

Improve cable detection using segmentation models.

Integrate dashboard for real-time monitoring.

Deploy pipeline on cloud (Azure/AWS) for scalability.

✍️ Developed during AI/ML Internship Project — DatacenterIQ
