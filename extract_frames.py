import cv2
import os

def extract_frames_1fps(input_dir, output_dir_base):
    # Check if input directory exists
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    # Loop through each video file in the input_videos folder
    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            continue

        video_path = os.path.join(input_dir, filename)
        video_name = os.path.splitext(filename)[0]
        output_dir = os.path.join(output_dir_base, video_name)
        os.makedirs(output_dir, exist_ok=True)

        print(f"🎞 Processing: {filename}")
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        interval = int(fps) if fps > 0 else 1  # Avoid division by zero

        frame_num = 0
        saved_frame_count = 0

        while True:
            success, frame = cap.read()
            if not success:
                break
            if frame_num % interval == 0:
                frame_path = os.path.join(output_dir, f"frame_{saved_frame_count:04d}.jpg")
                cv2.imwrite(frame_path, frame)
                saved_frame_count += 1
            frame_num += 1

        cap.release()
        print(f"✅ Extracted {saved_frame_count} frames to {output_dir}")

if __name__ == "__main__":
    # ✅ Your actual paths
    input_videos_folder = r"C:\Users\HARSHITHA\Desktop\datacenteriq\input_videos"
    frames_output_folder = r"C:\Users\HARSHITHA\Desktop\datacenteriq\frames"

    extract_frames_1fps(input_videos_folder, frames_output_folder)
