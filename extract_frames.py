import cv2
import os
import argparse
import rarfile
import shutil

def extract_frames(video_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打开视频文件
    vidcap = cv2.VideoCapture(video_path)
    
    success, image = vidcap.read()
    count = 0

    while success:
        # 将视频帧保存到文件夹中，格式为 frame000.jpg, frame001.jpg, ...
        frame_filename = os.path.join(output_folder, f"frame{count:03d}.jpg")
        cv2.imwrite(frame_filename, image)
        success, image = vidcap.read()
        count += 1
    
    vidcap.release()
    print(f"共提取了 {count} 帧")

def create_rar(output_folder, archive_name):
    # 创建RAR文件
    with rarfile.RarFile(archive_name, 'w') as rf:
        for root, _, files in os.walk(output_folder):
            for file in files:
                rf.write(os.path.join(root, file), arcname=file)
    print(f"已保存为 {archive_name}")

def main():
    parser = argparse.ArgumentParser(description="Extract frames from video and save to RAR file")
    parser.add_argument('--file', required=True, help='Path to the video file')
    parser.add_argument('--save_file', required=True, help='Path to the output RAR file')

    args = parser.parse_args()

    video_path = args.file
    save_file = args.save_file
    
    output_folder = 'frames_temp'

    # 提取帧
    extract_frames(video_path, output_folder)
    
    # 创建RAR文件
    create_rar(output_folder, save_file)
    
    # 删除临时文件夹
    shutil.rmtree(output_folder)

if __name__ == "__main__":
    main()
