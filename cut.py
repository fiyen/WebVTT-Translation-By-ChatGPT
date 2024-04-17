import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Cut a video into n parts.')
    parser.add_argument('--video', type=str, required=True,
                        help='The path to the video file.')
    parser.add_argument('--n', type=int, required=True,
                        help='The number of parts to split the video into.')
    args = parser.parse_args()

    video_path = args.video
    parts_num = args.n
    
    if not os.path.isfile(video_path):
        raise ValueError(f"{video_path} is not a valid video file")

    # Get video duration
    duration = float(subprocess.check_output(f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}", shell=True))
    
    # Calculate split timings
    splits = [(i * duration / parts_num, (i + 1) * duration / parts_num) for i in range(parts_num)]
    
    # Split the video using ffmpeg
    for i, split in enumerate(splits):
        output_path = os.path.splitext(video_path)[0] + f"_part{i+1}.mp4"
        subprocess.call(f"ffmpeg -i {video_path} -ss {split[0]} -to {split[1]} -c copy {output_path}", shell=True)
        print(f"Part {i+1} saved to {output_path}")

if __name__ == '__main__':
    main()
